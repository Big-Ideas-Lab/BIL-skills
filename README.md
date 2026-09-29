# BIL-skills

A small collection of reusable skills for Bill's research and lab workflows.

## Included skills

- [`presentation-slides`](./skills/productivity/presentation-slides/SKILL.md): create and reuse an HTML-first design system and fixed 16:9 HTML slide library for research updates, methods discussions, results, and decisions.
- [`literature-evidence-synthesis`](./skills/research/literature-evidence-synthesis/SKILL.md): find, verify, and synthesize scientific evidence into an evidence brief, evidence table, and claim-to-source map. Consensus MCP discovery is required in both lanes.
- [`hypothesis-assessment`](./skills/research/hypothesis-assessment/SKILL.md): generate and/or assess hypotheses on scientific risk, execution risk, time to evidence, and potential impact, with no composite score.
- [`research-topic-report`](./skills/research/research-topic-report/SKILL.md): orchestrate the two skills above into a neutral hypothesis-portfolio report as one self-contained HTML file.

## Repository layout

This repository follows the category-and-skill layout used by the reference skills repository:

```text
skills/
  productivity/
    README.md
    presentation-slides/
      SKILL.md
      agents/openai.yaml
      DESIGN.md
      design-system/
      slide-templates/
      scripts/
      tests/
  research/
    README.md
    literature-evidence-synthesis/
    hypothesis-assessment/
    research-topic-report/
```

Each skill is self-contained. Read its `SKILL.md` first, then use its supporting files and scripts.

## Installation

To copy the skills into a project with the Skills installer:

```bash
npx skills@latest add billchen0/BIL-skills
```

Choose `presentation-slides` when prompted. The root `skills/` layout is compatible with the Skills installer workflow.

Install the three `research/` skills together when you want the composite report: `research-topic-report` declares explicit dependencies on the other two.

## Development

The slide skill is local, editable, and dependency-free. Open `design-system/index.html` for the recovered canonical workspace; start generation from `slide-templates/template-manifest.json` and its fixed-stage template. The Reddit CGM deck is provenance, and PowerPoint/PPTX is not the target medium.

The research skills are instruction-and-template packages. Each ships `scripts/validate.py` and `tests/` that run with the standard library only:

```bash
cd skills/research/research-topic-report && python3 scripts/validate.py && python3 -m unittest discover -s tests
```

`research-topic-report` renders a self-contained HTML report with no third-party packages:

```bash
cd skills/research/research-topic-report
python3 scripts/build_report.py --data templates/report-data.example.json --out preview/example-report.html
```

## License

MIT. Each skill carries its own `LICENSE` file.
