# BIL-skills

A private, **BIG IDEAs Lab–internal** collection of reusable skills for the lab's research and presentation workflows. The package is opinionated for BIL members and is not maintained as a general-purpose public skill catalog.

Repository access does not expand the permitted use of Duke University or BIG IDEAs Lab names, logos, or other institutional marks. See [`TRADEMARKS.md`](./TRADEMARKS.md).

## Design system

The lab's HTML design system is the canonical reference surface for every BIL artifact — foundations, components, and the fixed-stage slide layouts in one page:

```bash
cd skills/productivity/presentation-slides
python3 -m http.server 8000
# then open http://localhost:8000/design-system/index.html
```

A public live link is pending Duke brand review: the catalog bundles institutional marks, and publication of those marks needs approval. See [`TRADEMARKS.md`](./TRADEMARKS.md).

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

Authorized BIG IDEAs Lab members with repository access can copy the skills into a project with the Skills installer:

```bash
npx skills@latest add Big-Ideas-Lab/BIL-skills
```

Choose `presentation-slides` when prompted. The root `skills/` layout is compatible with the Skills installer workflow.

Install the three `research/` skills together when you want the composite report: `research-topic-report` declares explicit dependencies on the other two.

## Development

The slide skill is local, editable, and dependency-free. Open `design-system/index.html` for the recovered canonical workspace; start generation from `slide-templates/template-manifest.json` and its fixed-stage template. PowerPoint/PPTX is not the target medium.

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

The code and written skill instructions are MIT-licensed; each skill carries its own `LICENSE` file. Institutional names, logos, and marks are excluded from that license and remain subject to their owners' policies. See [`TRADEMARKS.md`](./TRADEMARKS.md).
