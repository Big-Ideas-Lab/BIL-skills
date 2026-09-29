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
| 03 | Evidence table | one row per source: discovery route, verification state, comparison stratum, limitation |
| 04 | Claim-to-source map | one row per decision-relevant claim: source, locator, epistemic label, verification state |
| 05 | Hypothesis portfolio | one card per hypothesis with four axis chips and a claim state |
| 06 | Risk–impact matrix | ordinal ratings with rationale per axis, plus dominance notes |
| 07 | Falsifiers and minimum evidence | decisive comparison, smallest informative test, falsification condition |
| 08 | Unresolved questions and disagreements | open items, contested sources, preserved dissent |
| 09 | Skeptic pass | blocking defects, high-impact improvements, optional notes, independence label |
| 10 | Provenance and method | how the report was produced, retained records, lane |

Sections may be merged only if the resulting section still carries all required content. Never drop the claim-to-source map or the skeptic section.

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
