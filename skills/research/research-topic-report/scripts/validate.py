#!/usr/bin/env python3
"""Validator for the research-topic-report skill package.

Checks structure, frontmatter, referenced files, skill dependencies, design-token
parity with the BIL design system, neutrality rules, and the offline HTML
contract by actually building the example report. Standard library only.
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = ROOT / "SKILL.md"
MANIFEST = ROOT / "skill.json"
TOKENS = ROOT / "design-system" / "tokens.json"

REQUIRED_SECTIONS = (
    "## When to Use",
    "## Procedure",
    "## Pitfalls",
    "## Verification",
)
PATH_LINK = re.compile(r"`((?:references|templates|scripts|agents|design-system)/[^`]+)`")
BANNED = (
    re.compile(r"/Users/"),
    re.compile(r"/home/"),
    re.compile(r"~/\.hermes"),
    re.compile(r"\.hermes/profiles"),
    re.compile(r"/tmp/"),
)
# Token parity: the report reuses these exact decisions from the presentation system.
CANONICAL_COLORS = {
    "#012169", "#003A70", "#00539B", "#E8F1FA", "#F4F8FC",
    "#FFFFFF", "#111318", "#3F4650", "#68717D", "#D9DEE5",
    "#EDF0F4", "#F7F8FA",
}
CANONICAL_FONTS = ("Source Serif 4", "Inter", "IBM Plex Mono")


def fail(message: str) -> None:
    raise AssertionError(message)


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        fail("SKILL.md must start with '---' at byte 0")
    end = re.search(r"\n---\s*\n", text[3:])
    if end is None:
        fail("SKILL.md frontmatter is not closed with '\\n---\\n'")
        raise AssertionError("unreachable")
    fields = {}
    for line in text[3 : end.start() + 3].splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            fail(f"unparseable frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def check_frontmatter() -> dict:
    text = SKILL_MD.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    for key in ("name", "description"):
        if not fields.get(key):
            fail(f"frontmatter missing {key!r}")
    if fields["name"] != ROOT.name:
        fail(f"frontmatter name {fields['name']!r} does not match directory {ROOT.name!r}")
    if len(fields["description"]) > 60:
        fail(f"description is {len(fields['description'])} chars; the standard is 60 or fewer")
    if not fields["description"].endswith("."):
        fail("description must end with a period")
    return fields


def check_sections() -> str:
    text = SKILL_MD.read_text(encoding="utf-8")
    for heading in REQUIRED_SECTIONS:
        if heading not in text:
            fail(f"SKILL.md is missing required section {heading}")
    return text


def check_links(text: str) -> None:
    for target in sorted(set(PATH_LINK.findall(text))):
        if not (ROOT / target).exists():
            fail(f"SKILL.md references a missing file: {target}")


def check_no_machine_paths(text: str) -> None:
    for pattern in BANNED:
        match = pattern.search(text)
        if match:
            fail(f"machine-local path in SKILL.md: {match.group(0)}")


def check_manifest(text: str) -> dict:
    if not MANIFEST.exists():
        fail("skill.json is missing")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for key in (
        "name", "version", "lanes", "depends_on_skills", "recommendation",
        "outputs", "report_sections", "design", "references", "templates", "scripts",
    ):
        if key not in manifest:
            fail(f"skill.json missing key {key!r}")
    if manifest["name"] != ROOT.name:
        fail("skill.json name does not match the directory name")
    if manifest["lanes"] != ["routine", "decision-grade"]:
        fail("skill.json lanes must be routine and decision-grade")
    for lane in manifest["lanes"]:
        if lane not in text:
            fail(f"SKILL.md never names the {lane!r} lane")
    for key in ("references", "templates", "scripts"):
        for rel in manifest[key]:
            if not (ROOT / rel).exists():
                fail(f"skill.json lists a missing {key} file: {rel}")
    return manifest


def check_skill_dependencies(manifest: dict, text: str) -> None:
    for name in manifest["depends_on_skills"]:
        if name not in text:
            fail(f"SKILL.md does not name its dependency {name!r}")
        # Search both the flat layout (skills/<name>/) and the category layout
        # (skills/<category>/<name>/) so the check works however the repo is checked out.
        candidates = sorted(ROOT.parent.glob(f"{name}/SKILL.md")) + sorted(
            ROOT.parent.glob(f"*/{name}/SKILL.md")
        )
        if not candidates:
            fail(
                f"dependency {name!r} is absent from this checkout; install it with "
                "'npx skills@latest add billchen0/BIL-skills' or copy the sibling folder"
            )
        for found in candidates:
            manifest_path = found.parent / "skill.json"
            if not manifest_path.exists():
                continue
            sibling = json.loads(manifest_path.read_text(encoding="utf-8"))
            if sibling.get("name") != name:
                fail(f"sibling manifest for {name!r} is inconsistent")
            break


def check_neutrality(manifest: dict, text: str) -> None:
    if manifest["recommendation"] is not False:
        fail("skill.json recommendation must be false")
    lowered = text.lower()
    for phrase in ("neutral", "never recommends"):
        if phrase not in lowered:
            if "neutral" not in lowered:
                fail("SKILL.md must state that the report is neutral")
            if "never recommend" not in lowered:
                fail("SKILL.md must state that no option is recommended")
            return
    if "no composite" not in lowered and "composite score" not in lowered:
        fail("SKILL.md must forbid a composite score in the report")


def check_tokens() -> None:
    if not TOKENS.exists():
        fail("design-system/tokens.json is missing")
    tokens = json.loads(TOKENS.read_text(encoding="utf-8"))
    text = TOKENS.read_text(encoding="utf-8")
    missing = sorted(c for c in CANONICAL_COLORS if c not in text)
    if missing:
        fail(f"tokens.json is missing canonical BIL color values: {missing}")
    font_text = " ".join(tokens.get("font", {}).get("sans", []))
    display_text = " ".join(tokens.get("font", {}).get("display", []))
    mono_text = " ".join(tokens.get("font", {}).get("mono", []))
    for name in CANONICAL_FONTS:
        joined = display_text + font_text + mono_text
        if name not in joined:
            fail(f"tokens.json is missing canonical BIL font {name!r}")
    if tokens.get("layout", {}).get("sticky_nav") is not True:
        fail("the report layout contract must keep the sticky section nav")
    if "report-layout" not in tokens.get("meta", {}).get("scope", []):
        fail("tokens.json must declare report-layout scope separate from slide layouts")


def check_html_has_no_slide_stage() -> None:
    """The report is a scrolling document; it must not import slide-stage layout."""
    layout_anti_patterns = (
        re.compile(r"\.slide-stage"),
        re.compile(r"width:\s*1920px"),
        re.compile(r"1920\s*[x×]\s*1080", re.I),
        re.compile(r"transform:\s*scale\("),
    )
    for rel in ("templates/style.css", "DESIGN.md"):
        content = (ROOT / rel).read_text(encoding="utf-8")
        for pattern in layout_anti_patterns:
            match = pattern.search(content)
            if match:
                fail(f"{rel} reuses slide-stage layout: {match.group(0)}")


def check_card_grid_contract() -> None:
    """Cards must flow row-wise in an equal-width grid, not a balanced column flow."""
    css = (ROOT / "templates" / "style.css").read_text(encoding="utf-8")
    hypotheses_rule = css.split(".hypotheses {")[1].split("}")[0]
    if "display: grid" not in hypotheses_rule:
        fail("the hypothesis portfolio must use a CSS grid")
    if "minmax(0, 1fr)" not in css:
        fail("the card grid must use minmax(0, 1fr) so content cannot widen a column")
    if "column-count" in css:
        fail("the card grid must not use multi-column flow (it produces uneven columns)")
    chip_rule = css.split(".chip {")[1].split("}")[0]
    if "white-space: nowrap" not in chip_rule or "flex: 0 0 auto" not in chip_rule:
        fail("axis chips must not break a value mid-word")
    design = (ROOT / "DESIGN.md").read_text(encoding="utf-8")
    if "CSS grid" not in design:
        fail("DESIGN.md must record the card grid contract")


def load_builder():
    """Load scripts/build_report.py as a module without relying on importlib specs."""
    path = ROOT / "scripts" / "build_report.py"
    namespace = {"__name__": "build_report", "__file__": str(path)}
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), namespace)
    module = types.ModuleType("build_report")
    module.__dict__.update(namespace)
    return module


def check_offline_build() -> str:
    builder = load_builder()
    data = json.loads((ROOT / "templates" / "report-data.example.json").read_text(encoding="utf-8"))
    document = builder.build(data)
    findings = builder.check_offline(document)
    if findings:
        fail(f"offline contract violations in the example render: {findings[:3]}")
    lowered = document.lower()
    if "recommended option" in lowered:
        fail("the example render contains a recommended option")
    if "<details" not in document or "<summary" not in document:
        fail("hypothesis cards must use native details/summary")
    if document.count("<section class=\"section\"") != len(data["sections"]):
        fail("rendered section count does not match the report data")
    if "--blue-900: #012169" not in document:
        fail("the embedded stylesheet is missing the canonical BIL tokens")
    return document


def check_offline_build_cli() -> None:
    builder = load_builder()
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "report.html"
        code = builder.main(
            ["--data", str(ROOT / "templates" / "report-data.example.json"), "--out", str(out)]
        )
        if code != 0:
            fail(f"build_report.py exited {code}")
        if not out.exists() or out.stat().st_size < 4000:
            fail("build_report.py did not write a substantial artifact")


def main() -> int:
    try:
        check_frontmatter()
        text = check_sections()
        check_links(text)
        check_no_machine_paths(text)
        manifest = check_manifest(text)
        check_skill_dependencies(manifest, text)
        check_neutrality(manifest, text)
        check_tokens()
        check_html_has_no_slide_stage()
        check_card_grid_contract()
        check_offline_build()
        check_offline_build_cli()
    except AssertionError as exc:
        print(f"FAIL {ROOT.name}: {exc}")
        return 1
    print(
        f"OK   {ROOT.name}: frontmatter, dependencies, neutrality, token parity, "
        "offline build"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
