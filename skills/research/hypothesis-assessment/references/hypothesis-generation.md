# Hypothesis generation

Use this procedure only in the `generate-then-assess` mode, and always before scoring anything. Generating after scoring anchors every idea to the first one you rated.

## Order of operations

1. Fix the question, the inferential boundary, and what the data can observe.
2. Generate candidates broadly, without rating them.
3. Check that the set is genuinely diverse (diversity test below).
4. State each candidate as a testable claim with a prediction.
5. Only then begin axis rating.

## Divergence moves

Deliberately vary the mechanism, not the wording. Useful moves:

- **Invert** the assumed direction: what if the association runs the other way, or is absent?
- **Swap the unit**: person-level versus event-level versus day-level explanation of the same pattern.
- **Change the mediator**: the signal is real but routed through a different mechanism.
- **Change the cause of the pattern**: measurement, sampling, or processing produces it rather than physiology or behaviour.
- **Widen the population**: does the effect hold in a subgroup that the current framing excludes?
- **Narrow the population**: is the effect carried by a small identifiable subset?
- **Add the time dimension**: does the effect exist only in one ordering or lag?
- **Add the dose dimension**: does the effect depend on magnitude, or only on presence?
- **Test the baseline**: is the proposed signal better than an existing, simpler metric?
- **Test the horizon**: does the claim depend on a follow-up window that has not been observed?

## Diversity test

Before rating, check the candidate set:

- Do any two hypotheses share the same mechanism? If so, they are one hypothesis with two phrasings — merge them.
- Does the set include at least one explanation that is not about the mechanism the requester proposed? If not, keep generating.
- Does the set include at least one explanation that would be **falsified by the same measurement** as another? If so, the second is not independent.
- Is any candidate unfalsifiable as stated? Rewrite it or drop it.

## Common failure patterns

| Pattern | Symptom | Fix |
|---|---|---|
| Paraphrase set | Every candidate is the proposed mechanism with different words | Apply the inversion and rival-cause moves |
| One-cause set | All candidates are mechanisms; none is measurement or sampling | Add artifact and confounding candidates |
| Aggregated claim | "X is associated with Y in general" | Specify population, unit, and window |
| Unfalsifiable claim | No observation could count against it | Name the decisive comparison |
| Compound claim | Two mechanisms in one sentence | Split into separate candidates |
| Direction-free claim | Does not say which way the effect goes | State the expected pattern |

## Output of this stage

A candidate list, each with:

- a one-line claim;
- the predicted pattern;
- the observation that would count against it;
- the unit and window the claim is about.

Do not rate, rank, or shortlist at this stage. Rating is a separate step with its own record.

## Interaction with literature work

Generation benefits from the evidence brief but should not be limited to what the searched literature reports. A hypothesis worth testing is often one that no included paper has stated. Mark clearly which candidates are suggested by evidence and which are not yet grounded.
