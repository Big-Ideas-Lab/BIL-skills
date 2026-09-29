#!/usr/bin/env python3
"""Validator for the hypothesis-assessment skill package.

Checks structure, frontmatter, referenced files, machine-local paths, the
four-axis requirement, and the explicit ban on a composite score.
Standard library only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = ROOT / "SKILL.md"
MANIFEST = ROOT / "skill.json"

REQUIRED_SECTIONS = (
    "## When to Use",
    "## Procedure",
    "## Pitfalls",
    "## Verification",
)
REQUIRED_AXES = (
    "scientific risk",
    "execution risk",
    "time to evidence",
    "potential impact",
)
PATH_LINK = re.compile(r"`((?:references|templates|scripts|agents|design-system)/[^`]+)`")
BANNED = (
    re.compile(r"/Users/"),
    re.compile(r"/home/"),
    re.compile(r"~/\.hermes"),
    re.compile(r"\.hermes/profiles"),
    re.compile(r"/tmp/"),
)


def fail(message: str) -> None:
    raise AssertionError(message)


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        fail("SKILL.md must start with '---' at byte 0")
    end = re.search(r"\n---\s*\n", text[3:])
    if end is None:
        fail("SKILL.md frontmatter is not closed with '\\n---\\n'")
        raise AssertionError("unreachable")
    block = text[3 : end.start() + 3]
    fields = {}
    for line in block.splitlines():
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
    description = fields["description"]
    if len(description) > 60:
        fail(f"description is {len(description)} chars; the standard is 60 or fewer")
    if not description.endswith("."):
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
        "name",
        "version",
        "lanes",
        "modes",
        "axes",
        "composite_score",
        "hypothesis_classes",
        "outputs",
        "references",
        "templates",
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
    for key in ("references", "templates"):
        for rel in manifest[key]:
            if not (ROOT / rel).exists():
                fail(f"skill.json lists a missing {key} file: {rel}")
    return manifest


def check_axes(text: str, manifest: dict) -> None:
    lowered = text.lower()
    if [a.lower() for a in manifest["axes"]] != list(REQUIRED_AXES):
        fail("skill.json axes must be the four agreed axes, in order")
    for axis in REQUIRED_AXES:
        if axis not in lowered:
            fail(f"SKILL.md does not name the {axis!r} axis")
    if "cannot" not in lowered and "never" not in lowered:
        fail("SKILL.md must state the prohibition on collapsing the axes")


def check_no_composite_score(text: str, manifest: dict) -> None:
    if manifest["composite_score"] is not False:
        fail("skill.json composite_score must be false")
    lowered = text.lower()
    for phrase in ("never produce a single composite score", "no composite score"):
        if phrase in lowered:
            return
    fail("SKILL.md must explicitly forbid a composite score")


def check_modes_and_classes(text: str, manifest: dict) -> None:
    if sorted(manifest["modes"]) != ["assess-supplied", "generate-then-assess"]:
        fail("skill.json modes must be assess-supplied and generate-then-assess")
    lowered = text.lower()
    for mode in manifest["modes"]:
        if mode not in lowered:
            fail(f"SKILL.md does not name the {mode!r} mode")
    if "shortlist" not in lowered:
        fail("SKILL.md must scope the hypothesis classes to the shortlist")
    for rel in ("references/hypothesis-classes.md",):
        if not (ROOT / rel).exists():
            fail(f"missing required reference: {rel}")


def main() -> int:
    try:
        check_frontmatter()
        text = check_sections()
        check_links(text)
        check_no_machine_paths(text)
        manifest = check_manifest(text)
        check_axes(text, manifest)
        check_no_composite_score(text, manifest)
        check_modes_and_classes(text, manifest)
    except AssertionError as exc:
        print(f"FAIL {ROOT.name}: {exc}")
        return 1
    print(f"OK   {ROOT.name}: frontmatter, sections, four axes, no composite score, modes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
