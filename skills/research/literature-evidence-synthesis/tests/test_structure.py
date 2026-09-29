import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

import validate


class LiteratureEvidenceSynthesisTests(unittest.TestCase):
    def test_package_validator(self):
        self.assertEqual(validate.main(), 0)

    def test_frontmatter_description_within_limit(self):
        fields = validate.check_frontmatter()
        self.assertLessEqual(len(fields["description"]), 60)
        self.assertTrue(fields["description"].endswith("."))

    def test_consensus_is_required_in_both_lanes(self):
        text = validate.SKILL_MD.read_text(encoding="utf-8")
        manifest = validate.check_manifest(text)
        validate.check_consensus(text, manifest)
        self.assertEqual(manifest["consensus_mcp"]["lanes"], ["routine", "decision-grade"])

    def test_deliverable_templates_exist(self):
        for rel in (
            "templates/evidence-brief.md",
            "templates/evidence-table.csv",
            "templates/claim-source-map.csv",
        ):
            self.assertTrue((validate.ROOT / rel).exists(), rel)

    def test_decision_grade_requires_independent_route(self):
        manifest = validate.check_manifest(validate.SKILL_MD.read_text(encoding="utf-8"))
        joined = " ".join(manifest["decision_grade_requires"]).lower()
        self.assertIn("independent search route", joined)
        self.assertIn("full-text", joined)

    def test_no_machine_local_paths(self):
        validate.check_no_machine_paths(validate.SKILL_MD.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
