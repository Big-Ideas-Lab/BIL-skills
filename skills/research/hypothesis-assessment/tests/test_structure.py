import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

import validate


class HypothesisAssessmentTests(unittest.TestCase):
    def test_package_validator(self):
        self.assertEqual(validate.main(), 0)

    def test_frontmatter_description_within_limit(self):
        fields = validate.check_frontmatter()
        self.assertLessEqual(len(fields["description"]), 60)
        self.assertTrue(fields["description"].endswith("."))

    def test_four_axes_present(self):
        manifest = validate.check_manifest(validate.SKILL_MD.read_text(encoding="utf-8"))
        self.assertEqual(
            manifest["axes"],
            [
                "scientific risk",
                "execution risk",
                "time to evidence",
                "potential impact",
            ],
        )

    def test_composite_score_is_forbidden(self):
        text = validate.SKILL_MD.read_text(encoding="utf-8")
        manifest = validate.check_manifest(text)
        validate.check_no_composite_score(text, manifest)
        self.assertFalse(manifest["composite_score"])

    def test_classes_scoped_to_shortlist(self):
        manifest = validate.check_manifest(validate.SKILL_MD.read_text(encoding="utf-8"))
        self.assertIn("shortlist", manifest["hypothesis_classes_apply_to"])

    def test_both_modes_documented(self):
        text = validate.SKILL_MD.read_text(encoding="utf-8").lower()
        self.assertIn("assess-supplied", text)
        self.assertIn("generate-then-assess", text)

    def test_no_machine_local_paths(self):
        validate.check_no_machine_paths(validate.SKILL_MD.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
