#!/usr/bin/env python3
"""Validator for the literature-evidence-synthesis skill package.

Checks structure, frontmatter, referenced files, machine-local paths, and the
mandatory Consensus MCP requirement in both lanes. Standard library only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = ROOT / "SKILL.md"
MANIFEST = ROOT / "skill.json"
SCREENING_REFERENCE = ROOT / "references" / "laya-screening.md"

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


def fail(message: str) -> NoReturn:
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
    for key in ("name", "version", "lanes", "consensus_mcp", "outputs", "references", "templates"):
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


def check_consensus(text: str, manifest: dict) -> None:
    consensus = manifest["consensus_mcp"]
    if consensus.get("required") is not True:
        fail("Consensus MCP must be required")
    for lane in ("routine", "decision-grade"):
        if lane not in consensus.get("lanes", []):
            fail(f"Consensus MCP must be required in the {lane} lane")
    if "Consensus" not in text:
        fail("SKILL.md must document the Consensus MCP requirement")
    lowered = text.lower()
    if "discovery" not in lowered:
        fail("SKILL.md must state that Consensus is a discovery layer, not verification")
    if consensus.get("endpoint") not in text:
        fail("SKILL.md must name the official Consensus endpoint")
    if "independent" not in lowered:
        fail("SKILL.md must require an independent search route for decision-grade work")


def check_outputs(text: str, manifest: dict) -> None:
    expected = {"evidence brief", "evidence table", "claim-to-source map", "screening flow"}
    if set(manifest["outputs"]) != expected:
        fail(f"skill.json outputs must be exactly {sorted(expected)}")
    lowered = text.lower()
    for name in expected:
        if name not in lowered:
            fail(f"SKILL.md does not name the {name!r} deliverable")


def check_screening(text: str, manifest: dict) -> None:
    screening = manifest.get("screening")
    if not isinstance(screening, dict):
        fail("skill.json must declare a screening block")
    if screening.get("screener") != "Laya" or screening.get("required") is not True:
        fail("Laya must be the required screener")
    if sorted(screening.get("stages", [])) != ["full_text", "title_abstract"]:
        fail("Laya must screen at both the title_abstract and full_text stages")
    if screening.get("human_confirmation_required") is not False:
        fail("screening.human_confirmation_required must be false: decisions stand without confirmation")
    if not SCREENING_REFERENCE.exists():
        fail("references/laya-screening.md is missing")
    # The identity pin lives in the reference file only, so the version is
    # stated once. SKILL.md names the screener and links the reference.
    reference_text = SCREENING_REFERENCE.read_text(encoding="utf-8")
    model = screening.get("model") or {}
    for key in ("package", "version", "weights", "weights_revision"):
        if not model.get(key):
            fail(f"screening.model is missing {key!r}")
        if model[key] not in reference_text:
            fail(f"references/laya-screening.md must pin the model's {key!r}: {model[key]}")
    if "Laya" not in text:
        fail("SKILL.md must name Laya as the screener")
    for field in ("criterion_id", "supporting_span", "confidence"):
        if field not in text:
            fail(f"SKILL.md must require the screening decision field {field!r}")
    if "uncalibrated" not in text.lower():
        fail("SKILL.md must state that the screening confidence is uncalibrated")
    reference = "references/laya-screening.md"
    if reference not in manifest.get("references", []):
        fail("skill.json must list the Laya screening reference")
    if f"`{reference}`" not in text:
        fail("SKILL.md must link the Laya screening reference")


def main() -> int:
    try:
        check_frontmatter()
        text = check_sections()
        check_links(text)
        check_no_machine_paths(text)
        manifest = check_manifest(text)
        check_consensus(text, manifest)
        check_outputs(text, manifest)
        check_screening(text, manifest)
    except AssertionError as exc:
        print(f"FAIL {ROOT.name}: {exc}")
        return 1
    print(
        f"OK   {ROOT.name}: frontmatter, sections, links, Consensus requirement, "
        "Laya screening at both stages, deliverables"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
