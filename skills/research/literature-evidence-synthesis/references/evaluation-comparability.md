# Evaluation comparability

When two papers report performance numbers, the numbers are only comparable if the evaluation protocols match. Capture the fields below for every method you intend to compare, and refuse to rank across incompatible strata.

## Metric capture fields

| Field | Meaning |
|---|---|
| `task` | The prediction or detection task, stated in the paper's own terms |
| `event_unit` | What one scoring event is: event, episode, day, window, person, cohort |
| `reference_standard` | Ground truth source and its own uncertainty |
| `matching_rule` | Time window or tolerance used to match a detection to a reference event |
| `split_unit` | What was split: event, day, person, or cohort |
| `validation` | Internal, external, or both |
| `comparator` | The baseline the number was computed against |
| `threshold_procedure` | How the operating point was chosen; if on the test set, say so |
| `metric_name` | The exact metric as named by the authors |
| `metric_definition` | Formula or formal definition, not the acronym |
| `numerator` | What counted in the numerator |
| `denominator` | What counted in the denominator |
| `aggregation` | Micro, macro, or per-subject average |
| `uncertainty` | Confidence interval, standard deviation, or participant distribution |
| `failure_handling` | How abstentions, missing data, and failures were treated |

## Compatibility strata

Two numbers may be placed in the same comparison only if `task`, `event_unit`, `matching_rule`, `split_unit`, `metric_definition`, and `aggregation` all agree. Everything else — comparator choice, threshold procedure, validation type — must at least be stated next to the number.

If the strata differ:

- Display the metrics side by side in the evidence table.
- Label the row group `non-comparable`.
- Never compute a ranking, a mean, or a "best" designation across it.

## Common traps

- **Event-unit drift.** One paper scores per detected excursion, another per person-day. A higher number is not a better method.
- **Tolerance drift.** A generous matching window inflates detection rates without improving the detector.
- **Threshold selected on test data.** Report it as such; it is not a held-out result.
- **Split leakage.** Windows or events from the same person on both sides of the split.
- **Aggregation mismatch.** Micro-averaged and macro-averaged scores answer different questions.
- **Silent abstention.** A method that abstains on hard cases and is scored only on accepted cases has not been evaluated on the same task.
- **Absent uncertainty.** A point estimate without an interval from a small cohort is not evidence of superiority.

## Reporting rule

An evidence table may honestly contain "not comparable" rows. That is a finding, not a failure of the review.
