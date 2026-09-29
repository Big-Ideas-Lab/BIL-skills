# Internal skeptic pass

Critique and revision are **stages of this skill**, not a separately invocable workflow. The purpose is to find the defects that the author of the artifact cannot see, before the group relies on the artifact.

## Independence

Independent means the critic did not participate in producing the artifact and does not know which hypothesis or direction the requester prefers.

| Setup | Label | Acceptable for |
|---|---|---|
| Fresh context, no prior exposure to the draft or the preferred option | `independent` | decision-grade |
| Fresh context that has seen the draft but not the preference | `independent (draft-visible)` | decision-grade, note the exposure |
| Same context that produced the artifact | `same-context` | routine lane; never presented as independent |

Give the critic only: the artifact, the report contract, the evidence records, and the claim-to-source map. Do not give it the author's rationale. If a fresh context is unavailable, say so in the report instead of implying independence.

## Critic brief

Ask the critic to work in this order and return findings, not a rewrite:

1. **Claim support.** Is every decision-relevant claim supported by a verified source at the stated locator? List any claim that is not.
2. **Alternative explanations.** Which hypotheses lack a testable rival, null, or artifact explanation?
3. **Falsifiability.** Which hypotheses have no observation that could count against them?
4. **Comparison integrity.** Are any metrics being compared across incompatible event units, splits, or tolerance windows?
5. **Inferential overreach.** Where does the artifact upgrade an observation into a mechanism, a correlation into a cause, or an algorithm-defined event into a clinical event?
6. **Coverage honesty.** Are coverage gaps, inaccessible sources, or stopping-rule caveats missing?
7. **Neutrality.** Does anything in the artifact imply a preferred option?
8. **Framing stability.** Would the conclusions change if the topic were phrased differently? Name any conclusion that is fragile to framing.

## Output format

The critic returns three prioritized groups plus an explicit judgment:

- **Blocking defects** — an unsupported claim, a false certainty, a neutrality breach, an unverified comparison. Must be fixed before the artifact is used.
- **High-impact improvements** — omissions that weaken a defensible artifact.
- **Optional notes** — polish, wording, structure.
- **Judgment** — `pass` or `fail`, with the blocking count.

Order matters: a critic that leads with wording while an unsupported claim sits in the evidence table has failed the task.

## Revision rules

1. Never let the critic rewrite the artifact. It reports; the author revises.
2. Fix blocking defects first, then high-impact improvements.
3. Optional notes are adopted only if they do not dilute the artifact.
4. Record every finding and whether it was adopted.
5. **Preserve dissent verbatim.** An objection that is not adopted stays in the report under "Preserved dissent" with its reasoning. Averaging it away destroys the record.
6. If a blocking defect cannot be fixed within the lane's scope, mark the artifact as not ready and say which defect blocks it. Do not soften the wording and ship it.

## Re-critique

After blocking defects are fixed, a re-critique is required in the decision-grade lane when:

- a new claim was added;
- a comparison stratum changed;
- a hypothesis was added or re-rated;
- the critic's judgment was `fail`.

A re-critique may use the same critic; it is still labelled with its independence status.
