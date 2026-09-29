# Decision-grade gates

The routine lane is proportionate: query Consensus, read what you cite, state the limits. The decision-grade lane adds the gates below. Escalate without asking when the answer sets a research or clinical direction, enters a manuscript, or supports a go/no-go decision.

## Gate list

1. **Two routes minimum.** Consensus MCP plus at least one independent route, both recorded in the search ledger. If Consensus is unavailable, disclose the blocker rather than substituting a route.
2. **Frozen protocol.** Write the question, eligibility criteria, and stopping rule down before screening begins, with a timestamp. A protocol written after screening is a description, not a gate.
3. **Stopping rule.** State what makes the review complete: date cutoff, journal coverage, saturation, or a record budget. "Until we stop finding things" is not a stopping rule.
4. **Non-default screening.** Every deduplicated record carries one of `promote_full_text`, `exclude_title_abstract`, `uncertain_retrieve`, or `duplicate`. Fall-through is `uncertain_retrieve`.
5. **No identifier allowlist.** Eligibility is never implemented as a preselected DOI/PMID/PMCID list. Known eligible papers are sentinel **regression fixtures**, not the inclusion mechanism.
6. **Exclusion evidence.** Every exclusion names the criterion and quotes the title/abstract span that supports it.
7. **Sentinel regression.** Known eligible papers must be retrieved and not excluded. A failure here invalidates the screen regardless of how many records were processed.
8. **Exclusion audit.** Audit every exclusion containing target-task or target-input terminology, and independently rescreen all uncertain records plus a reproducible random sample of exclusions.
9. **False-negative accounting.** Report the audited disagreement rate and the estimated residual false-negative risk. Do not report zero risk.
10. **Full-text gate.** Every claim presented as verified has accessible full text and a source locator. Inaccessible sources stay `awaiting_full_text`.
11. **Comparability gate.** Cross-paper metrics are compared only within compatible strata; incompatible numbers are shown side by side and labelled.
12. **Disagreement preservation.** Contradictory findings are reported separately, never averaged into a consensus that no source states.

## High-recall promotion triggers

Promote a record to full text when either is true, even if the title screening would otherwise exclude it:

- The abstract states that the target modality is the **only algorithmic input**.
- The title names the **target task and target modality** directly.

These two triggers exist because the most common review failure is losing a paper that matches the target exactly but describes it in unfamiliar vocabulary.

## Minimum record set

| Record | Contents |
|---|---|
| Search ledger | one row per query, per route |
| Screening log | one row per deduplicated record with decision, criterion, and quoted span |
| Exclusion audit | audited rows, disagreement, adjudication, residual risk |
| Evidence records | item identity, identifiers, class, locator, verification state, grading |
| Claim records | claim text, epistemic label, source, locator, verification state |
| Limitations | coverage gaps, inaccessible sources, stopping-rule caveats |

## Reporting rule

If a gate could not be satisfied, say which gate and why. A decision-grade review with one disclosed gap is usable. A review that reports full coverage while skipping the sentinel or comparability gate is not.
