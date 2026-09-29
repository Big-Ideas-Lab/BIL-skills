---
name: research-topic-report
description: Build a neutral hypothesis portfolio report for a topic.
disable-model-invocation: false
argument-hint: "Which research topic or direction needs a hypothesis portfolio report?"
---

# Research topic report

Turn a **defined research topic** into a neutral hypothesis-portfolio report: an offline, self-contained HTML artifact for group discussion. It orchestrates two component skills rather than reimplementing them:

- `literature-evidence-synthesis` — evidence brief, evidence table, claim-to-source map.
- `hypothesis-assessment` — hypothesis register and risk–impact matrix.

It then adds an internal **independent skeptic pass** and renders the report. Critique and revision are stages of this skill, not a separately invocable skill.

**The report is neutral.** It presents the portfolio, the trade-offs, and the open questions. It never recommends "pursue X". The group or PI makes that call.

## When to Use

- Bill or a lab member names a research topic or direction and wants a discussion-ready portfolio.
- A group meeting needs one artifact covering evidence, hypotheses, trade-offs, and unknowns.
- A direction needs rival, null, and confound explanations laid out before any commitment.

Don't use for: choosing a research direction, an evidence brief alone (use `literature-evidence-synthesis`), hypothesis scoring alone (use `hypothesis-assessment`), or a slide deck (use `presentation-slides`). The research direction is an **input** — if the topic is not yet defined, settle that first.

## Prerequisites

This skill orchestrates two sibling skills and does not replace them. Install all three so the dependencies resolve:

```bash
npx skills@latest add billchen0/BIL-skills
```

Also required: a configured Consensus MCP server (see `literature-evidence-synthesis`). Python 3.9+ for `scripts/build_report.py`; the builder needs no third-party packages. If a sibling skill is missing from the checkout, install it or copy its folder next to this one.

## Lanes

| Lane | Use for | Required before finishing |
|---|---|---|
| **routine** | an internal discussion artifact or early exploration | evidence brief, hypothesis register, 4-axis matrix, unresolved questions, sourced render |
| **decision-grade** | an artifact that will anchor a commitment, milestone, or external review | everything in routine, plus decision-grade literature gates, falsifiers and minimum evidence, the five hypothesis classes on the shortlist, and a fresh-context skeptic pass |

## Procedure

1. **Fix the topic and scope.** Record the research direction, the question set, and the inferential boundary. Completion criterion: the topic is stated as input, with what is explicitly out of scope.
2. **Run the literature stage.** Invoke `literature-evidence-synthesis` at the matching lane. Consensus MCP is required; decision-grade additionally requires an independent search route and full-text verification. If Consensus is unavailable, disclose it in the report rather than proceeding silently. Completion criterion: the three literature artifacts exist with provenance.
3. **Run the hypothesis stage.** Invoke `hypothesis-assessment` in `generate-then-assess` when no hypothesis set exists, otherwise `assess-supplied`. Produce the register and the four-axis matrix. Completion criterion: every hypothesis carries four ratings with rationale and no composite score.
4. **Add explanation classes and gates** for shortlisted hypotheses at the lane's requirements — rival, null, artifact/confounding, falsifier, and minimum evidence. Completion criterion: every shortlisted hypothesis has all five where the lane requires them.
5. **Run the internal skeptic pass.** Follow `references/skeptic-pass.md`: the critic starts from fresh context, stays blind to any preferred option, and reports dissent verbatim. Never let the critic silently rewrite the artifact. If only same-context critique is available, label it. Completion criterion: the skeptic section lists prioritized findings, with independence labeled honestly.
6. **Assemble the report data** into the structure of `templates/report-data.example.json`. Every claim carries a source locator and a verification state; every hypothesis carries its matrix row. Completion criterion: no displayed claim lacks a source or a state.
7. **Render the report** with `scripts/build_report.py`, which embeds the stylesheet and data so the output is one self-contained `.html` file with no network requests. See `references/offline-html-contract.md`. Completion criterion: the rendered file loads offline with no external references.
8. **Verify the render visually.** Inspect the desktop and mobile widths side by side with `DESIGN.md`. Source inspection is not proof of visual quality. Completion criterion: the layout contract in `DESIGN.md` holds at both widths, or the gap is reported.
9. **Report neutrally.** Confirm the artifact contains no recommendation, no composite score, and no unsupported claim. Completion criterion: an explicit neutrality check passes and the unresolved questions are visible.

## Deliverables

| Artifact | Source | Purpose |
|---|---|---|
| Neutral hypothesis portfolio (HTML) | `scripts/build_report.py` + report data | discussion artifact for the group |
| Report data (JSON) | `templates/report-data.example.json` | machine-readable input, re-renderable when evidence changes |
| Evidence and hypothesis records | component skills | provenance behind every displayed claim |

## Pitfalls

- Adding a recommendation, a "recommended option" badge, or a winner column. The report is neutral by contract.
- Inventing a composite risk-adjusted score; the four axes stay separate.
- Reimplementing screening, grading, or scoring here instead of invoking the component skills.
- Citing a paper from a Consensus snippet without source verification.
- Letting the skeptic pass quietly rewrite text so the objection disappears.
- Shipping a report that loads fonts, scripts, or images over the network, so it breaks offline.
- Restyling the report into fixed 1920×1080 slide stages instead of a scrolling document.
- Padding with prose. Omit any sentence that does not carry evidence, a trade-off, or an open question.

## Verification

Before delivering:

- [ ] Topic and scope stated as fixed input, with exclusions.
- [ ] Both component skills ran at the stated lane; Consensus disclosure is present if blocked.
- [ ] Three literature artifacts, hypothesis register, and 4-axis matrix all present.
- [ ] Every claim has a source locator and verification state; every hypothesis has a matrix row.
- [ ] No recommendation and no composite score anywhere in the rendered report.
- [ ] Falsifiers, minimum evidence, and rival/null/artifact explanations present where the lane requires.
- [ ] Skeptic section present with independence labeled honestly.
- [ ] Rendered HTML is a single self-contained file with no external references.
- [ ] Desktop and mobile renders inspected against `DESIGN.md`.

Run `python3 scripts/validate.py` from this skill directory to check the package structure, skill dependencies, and offline HTML contract.

## References

- `references/report-contract.md` — required sections, neutrality rules, and content limits.
- `references/skeptic-pass.md` — the internal independent critic procedure and labeling rules.
- `references/offline-html-contract.md` — self-containment rules for the rendered artifact.
- `DESIGN.md` — how the report reuses BIL tokens and typography, plus report layout rules.
