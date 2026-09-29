import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

import validate


class ResearchTopicReportTests(unittest.TestCase):
    def test_package_validator(self):
        self.assertEqual(validate.main(), 0)

    def test_frontmatter_description_within_limit(self):
        fields = validate.check_frontmatter()
        self.assertLessEqual(len(fields["description"]), 60)
        self.assertTrue(fields["description"].endswith("."))

    def test_dependencies_resolve(self):
        text = validate.SKILL_MD.read_text(encoding="utf-8")
        manifest = validate.check_manifest(text)
        validate.check_skill_dependencies(manifest, text)
        self.assertEqual(
            manifest["depends_on_skills"],
            ["literature-evidence-synthesis", "hypothesis-assessment"],
        )

    def test_report_is_neutral(self):
        text = validate.SKILL_MD.read_text(encoding="utf-8")
        manifest = validate.check_manifest(text)
        validate.check_neutrality(manifest, text)
        self.assertFalse(manifest["recommendation"])

    def test_token_parity_with_bil_design_system(self):
        validate.check_tokens()

    def test_render_is_self_contained(self):
        document = validate.check_offline_build()
        self.assertNotIn("http://", document)
        self.assertNotIn("https://", document)
        self.assertIn("<style>", document)
        # The only script is the declared scroll-spy; nothing else may load or run.
        self.assertEqual(document.lower().count("<script"), 1)
        self.assertIn("data-bil-spy", document)
        self.assertNotIn("src=", document.lower())

    def test_every_hypothesis_has_four_axes(self):
        data = json.loads(
            (validate.ROOT / "templates" / "report-data.example.json").read_text(encoding="utf-8")
        )
        hypotheses = [
            section for section in data["sections"] if section.get("kind") == "hypotheses"
        ][0]["body"]
        self.assertGreaterEqual(len(hypotheses), 3)
        for hyp in hypotheses:
            self.assertEqual(
                sorted(hyp["axes"]),
                [
                    "execution_risk",
                    "potential_impact",
                    "scientific_risk",
                    "time_to_evidence",
                ],
            )
            for axis in hyp["axes"].values():
                self.assertTrue(axis.get("rationale"), hyp["id"])

    def test_claim_length_limit_enforced(self):
        builder = validate.load_builder()
        data = json.loads(
            (validate.ROOT / "templates" / "report-data.example.json").read_text(encoding="utf-8")
        )
        hyp_section = [s for s in data["sections"] if s.get("kind") == "hypotheses"][0]
        hyp_section["body"][0]["claim"] = "x" * 200
        with self.assertRaises(ValueError):
            builder.build(data)

    def test_missing_axis_is_rejected(self):
        builder = validate.load_builder()
        data = json.loads(
            (validate.ROOT / "templates" / "report-data.example.json").read_text(encoding="utf-8")
        )
        hyp_section = [s for s in data["sections"] if s.get("kind") == "hypotheses"][0]
        del hyp_section["body"][1]["axes"]["potential_impact"]
        with self.assertRaises(ValueError):
            builder.build(data)

    def test_no_slide_stage_geometry(self):
        validate.check_html_has_no_slide_stage()

    def test_card_grid_contract(self):
        validate.check_card_grid_contract()
        css = (validate.ROOT / "templates" / "style.css").read_text(encoding="utf-8")
        self.assertNotIn("column-count", css)
        self.assertIn("grid-template-columns: repeat(2, minmax(0, 1fr))", css)

    def test_section_lead_renders_before_cards(self):
        builder = validate.load_builder()
        data = json.loads(
            (validate.ROOT / "templates" / "report-data.example.json").read_text(encoding="utf-8")
        )
        hyp_section = [s for s in data["sections"] if s.get("kind") == "hypotheses"][0]
        self.assertTrue(hyp_section.get("lead"), "the example should carry a chip legend lead")
        document = builder.build(data)
        lead = hyp_section["lead"][0]
        self.assertIn(lead[:40], document)
        self.assertLess(document.index(lead[:40]), document.index("article class=\"hypothesis\""))

    def test_chip_labels_are_compact(self):
        builder = validate.load_builder()
        data = json.loads(
            (validate.ROOT / "templates" / "report-data.example.json").read_text(encoding="utf-8")
        )
        document = builder.build(data)
        for short in ("Sci. risk", "Exec. risk", "Impact"):
            self.assertIn(short, document)
        stylesheet = (validate.ROOT / "templates" / "style.css").read_text(encoding="utf-8")
        self.assertIn("white-space: nowrap", stylesheet.split(".chip {")[1].split("}")[0])

    def test_no_machine_local_paths(self):
        validate.check_no_machine_paths(validate.SKILL_MD.read_text(encoding="utf-8"))

    def test_screening_flow_contract(self):
        validate.check_flow_contract()
        document = validate.check_offline_build()
        self.assertIn("Count reconciliation", document)
        self.assertIn('class="flow-box', document)

    def test_unreconciled_flow_is_disclosed_not_silent(self):
        builder = validate.load_builder()
        data = json.loads(
            (validate.ROOT / "templates" / "report-data.example.json").read_text(
                encoding="utf-8"
            )
        )
        flow = [s for s in data["sections"] if s.get("kind") == "flow"][0]
        flow["body"]["reconciliation"][0]["rhs"] = 999
        warnings = builder.flow_warnings(data)
        self.assertEqual(len(warnings), 1)
        self.assertIn("unique screened", warnings[0])
        # A disclosed disagreement still renders; it is never silently edited away.
        self.assertIn("FAIL", builder.build(data))


if __name__ == "__main__":
    unittest.main()
