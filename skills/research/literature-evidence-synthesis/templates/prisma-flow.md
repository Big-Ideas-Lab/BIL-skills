# Screening flow (PRISMA-like)

> Template. Replace every `<>` placeholder and every `0` with the run's real counts.
> Every number must be derivable from the search ledger, screening log, and full-text assessment.

The flow is a **required deliverable** and appears in the review as a diagram plus the counts table below. Do not hand-draw it; render it from the run's records so the diagram cannot drift from the data.

## Diagram

Render as a top-to-bottom flow with one box per stage and an exclusion branch beside each screening stage. Include the stage label, the count, and (for `n`-to-`n` transitions) the reason for the drop.

```text
Records identified (all routes, before dedup)            n = <0>
  ├─ route A (Consensus MCP)                             n = <0>
  ├─ route B (independent)                               n = <0>
  └─ ...
Duplicates removed                                       n = <0>
Records screened (unique)                                n = <0>
  ├─ advanced at title/abstract                          n = <0>
  └─ excluded at title/abstract                          n = <0>
        ├─ criterion E1 <name>                           n = <0>
        ├─ criterion E2 <name>                           n = <0>
        └─ ...
Records sought for full text                             n = <0>
  ├─ not retrieved (inaccessible)                        n = <0>
  │     ├─ paywall / 403                                 n = <0>
  │     ├─ abstract only                                 n = <0>
  │     └─ other access failure                          n = <0>
  └─ full text assessed                                  n = <0>
        ├─ included                                      n = <0>
        │     ├─ include_core                            n = <0>
        │     └─ include_contrast                        n = <0>
        └─ excluded at full text                         n = <0>
              ├─ gate G1 <name>                          n = <0>
              ├─ gate G2 <name>                          n = <0>
              ├─ gate G3 <name>                          n = <0>
              ├─ gate G4 <name>                          n = <0>
              └─ other full-text criterion               n = <0>
Records awaiting full text (not included, not excluded)  n = <0>
Studies included in the synthesis                        n = <0>
```

## Counts (machine-checked)

| Stage | Count |
|---|---|
| identified | 0 |
| duplicates removed | 0 |
| unique screened (title/abstract) | 0 |
| excluded (title/abstract) | 0 |
| promoted (title/abstract) | 0 |
| uncertain (title/abstract) | 0 |
| sought for full text | 0 |
| not retrieved | 0 |
| full text assessed | 0 |
| included (core) | 0 |
| included (contrast) | 0 |
| excluded (full text) | 0 |
| awaiting full text | 0 |
| included in synthesis | 0 |

## Reconciliation rules

1. `unique screened = excluded + promoted + uncertain` at the title/abstract stage.
2. `full text assessed + not retrieved = sought for full text`.
3. `included + excluded at full text = full text assessed`.
4. `awaiting full text` is a **visible** end state. It is summed out of neither the totals nor the included count. A record that could not be read is not an inclusion and not an exclusion.
5. Exclusion-reason counts must sum to their stage's exclusion total.

Any rule that does not balance is a reported defect. Never adjust a count to make the diagram look tidy.

## Laya attribution

State which stages Laya decided, the pinned package version and weights revision, the truncation policy with the count of truncated inputs, the sentinel outcome, and the audited disagreement rate. A reader must be able to tell which records advanced because of a model decision and which advanced after human reading.
