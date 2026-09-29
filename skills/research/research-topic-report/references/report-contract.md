# Report contract

The report is a **neutral hypothesis portfolio**. It exists so a group can look at evidence, candidate hypotheses, and trade-offs in one place, then decide for themselves.

## Neutrality rules (hard)

1. No recommended option, direction, or hypothesis — not in prose, not in a badge, not in a column.
2. No "winner", "best option", "top pick", "we should pursue", or equivalent phrasing.
3. No composite score, weighted total, or single ranking number.
4. Trade-offs are presented, not resolved. Where a hypothesis dominates another, that is a factual statement about the ratings — not a recommendation.
5. The footer carries the neutrality statement.

The word "recommend" may appear only inside the footer's neutrality disclaimer. `scripts/build_report.py` prints a neutrality warning if it appears anywhere else.

## Required sections

| Order | Section | Content |
|---|---|---|
| 01 | Topic and scope | research direction as fixed input, question set, in-scope, out-of-scope, inferential boundary |
| 02 | Evidence brief | established findings, contested findings, gaps, stated limitations |
| 03 | Screening flow | PRISMA-like counts from identification to inclusion: each stage, each exclusion reason with its count, the reconciled totals, and the screener attribution |
| 04 | Evidence table | one row per source: discovery route, verification state, comparison stratum, limitation |
| 05 | Claim-to-source map | one row per decision-relevant claim: source, locator, epistemic label, verification state |
| 06 | Hypothesis portfolio | one card per hypothesis with four axis chips and a claim state |
| 07 | Risk–impact matrix | ordinal ratings with rationale per axis, plus dominance notes |
| 08 | Falsifiers and minimum evidence | decisive comparison, smallest informative test, falsification condition |
| 09 | Unresolved questions and disagreements | open items, contested sources, preserved dissent |
| 10 | Skeptic pass | blocking defects, high-impact improvements, optional notes, independence label |
| 11 | Provenance and method | how the report was produced, retained records, lane |

Sections may be merged only if the resulting section still carries all required content. Never drop the screening flow, the claim-to-source map, or the skeptic section.

## Screening flow rules

The flow is a `kind: "flow"` section. Its counts are read from the search ledger, the screening log, and the full-text assessments — never retyped from prose.

- Every stage carries a count. Every exclusion branch names each reason with its own count, and the reasons must sum to the branch total.
- The section must reconcile all four rules: unique screened = excluded + promoted + uncertain; full text assessed + not retrieved = sought for full text; included + excluded at full text = full text assessed; exclusion reasons sum to their stage total.
- A count that does not reconcile is **disclosed**, never adjusted. `scripts/build_report.py` prints a `flow reconciliation warning` to stderr for every rule that fails, and the rendered rule is marked `FAIL`.
- `awaiting_full_text` is a visible `hold` stage, not a silent omission: a record that is neither included nor excluded must be countable in the diagram.
- The attribution block names the screener, its version and weights revision, the stages it screened, whether human confirmation was required, and the sentinel-regression result.

## Content limits

- 900–1600 words of prose total, excluding tables.
- Max 120 words of prose before a table, list, or card carries the detail.
- Evidence table: one row per source. No merged cells.
- Hypothesis card claim line: max 180 characters (enforced by the builder).
- Cut any sentence that carries no evidence, trade-off, or open question. No scene-setting, no throat-clearing, no restating the topic.

## Empty and negative states

An honest empty state is required and must be visible:

- no hypotheses yet → state the register is empty and why;
- a source awaiting full text → keep the row, mark the state;
- no disagreements found → say so explicitly rather than omitting the section;
- a claim with no support → keep it, labelled `unsupported`.

Omitting an empty section implies it was populated. That is a form of overstatement.

## Lane requirements

| Requirement | routine | decision-grade |
|---|---|---|
| Consensus MCP disclosure | required | required |
| Independent search route | — | required |
| Full-text verification for verified claims | required | required |
| Four-axis ratings with rationale | required | required |
| Falsifier and minimum evidence | — | required |
| Rival / null / artifact explanations | — | required |
| Skeptic pass with independence label | recommended | required |

## What the report must never do

- Present an unsupervised clustering or pseudo-temporal ordering as an observed progression.
- Name an algorithm-defined event by a causal name the labels cannot support.
- Present a same-context critique as an independent review.
- Merge contradictory findings into a consensus no source states.
- Hide a coverage gap or an inaccessible source.
