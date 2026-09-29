# Research

BIG IDEAs Lab–internal scientific-process skills: turn a question into verified evidence, turn hypotheses into a risk–impact comparison, and assemble a neutral portfolio report for group discussion.

The three skills compose. `research-topic-report` orchestrates the other two and adds an internal independent skeptic pass; it does not reimplement their work.

| Skill | Use for | Primary outputs |
|---|---|---|
| **[literature-evidence-synthesis](./literature-evidence-synthesis/SKILL.md)** | evidence briefs, novelty checks, decision-relevant literature claims | evidence brief, evidence table, claim-to-source map |
| **[hypothesis-assessment](./hypothesis-assessment/SKILL.md)** | generating or evaluating hypotheses before committing effort | hypothesis register, risk–impact matrix |
| **[research-topic-report](./research-topic-report/SKILL.md)** | a defined research topic that needs a discussion-ready portfolio | neutral hypothesis portfolio as a self-contained HTML report |

## Conventions these skills share

- **Two lanes.** Every skill runs in a `routine` lane or a `decision-grade` lane. Escalation is mandatory when the answer sets a research or clinical direction, enters a manuscript, or supports a go/no-go decision.
- **Consensus MCP is required** for literature discovery in both lanes. Decision-grade work additionally requires at least one independent search route and full-text verification of every verified claim.
- **Consensus is discovery only.** Snippets, abstracts, and metadata never verify a claim.
- **No composite scores.** Hypothesis options are compared on separate axes with a rationale each, and Pareto relationships are stated instead of collapsed into a single number.
- **Disagreement is preserved**, not averaged away.
- **Inaccessible sources stay in the record** as `awaiting_full_text`; they are never silently excluded and never carry a claim.

## Install

These skills are privately hosted and maintained for authorized BIL lab use rather than as a general-purpose public workflow standard. Installation requires access to the private repository.

```bash
npx skills@latest add Big-Ideas-Lab/BIL-skills
```

Install all three so the composite's skill dependencies resolve. `research-topic-report` also needs a configured Consensus MCP server and Python 3.9+ for its dependency-free report builder.
