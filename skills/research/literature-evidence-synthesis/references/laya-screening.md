# Laya screening at both stages

Laya is the **mandatory first-pass screener** for this skill, at the title/abstract stage **and** the full-text stage. It does not replace the search, the gates, or source verification; it decides which records advance.

## Model identity (pin it, every run)

| Field | Value |
|---|---|
| Package | `laya` 0.3.21 |
| Weights | `convaiinnovations/laya` |
| Revision | `55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851` |
| Runtime | local, offline, no credentials, no per-call cost |
| Python | 3.11+ (`requires_python >=3.10`) |

Record the package version and the weights revision in the run's screening summary. A screen produced with an unpinned revision is not reproducible and must be reported as such.

## Two stages

**Stage 1 — title/abstract.** Decision space `promote_full_text | exclude_title_abstract | uncertain_retrieve`. Input is the title plus abstract.

**Stage 2 — full text.** Decision space `include_core | include_contrast | exclude_full_text | awaiting_full_text`. Input is the retrieved full text, subject to the truncation policy below. At this stage the full text gates apply: a record that fails a gate is `exclude_full_text` with the gate named as the criterion.

A record that is still inaccessible stays `awaiting_full_text`. It is never excluded and never carries a verified claim.

## Decision record (required per record, per stage)

Autonomous decisions are permitted, but an unlogged decision is not. Every Laya decision writes one row:

| Field | Meaning |
|---|---|
| `record_key` | dedup key |
| `stage` | `title_abstract` or `full_text` |
| `decision` | from that stage's decision space |
| `criterion_id` | the inclusion/exclusion criterion or gate the decision rests on |
| `supporting_span` | the verbatim span from the input that supports it |
| `confidence` | Laya's answer probability, uncalibrated — see below |
| `model` / `model_version` / `weights_revision` | identity pinning |
| `input_chars` / `truncated` | length and whether the truncation policy engaged |

An exclusion without a `criterion_id` and a `supporting_span` is a defect, not a decision.

## Truncation policy (full text)

Full texts exceed comfortable input lengths. State the policy once, before screening, and record `input_chars` and `truncated` per record. Screening a truncated full text cannot support a gate verdict that depends on the omitted material — most often G3 (implementation detail). When a gate verdict rests on content beyond the truncation point, the record is `uncertain_retrieve`, not a pass and not a fail.

## Programme-level safeguards

These are programmatic, so they run on every screen without a human in the loop.

1. **Sentinel regression.** Known-eligible fixtures must be retrieved and must not be excluded. A sentinel failure invalidates the screen regardless of how many other records processed cleanly.
2. **Target-term exclusion audit.** Audit every exclusion whose input contains target-task or target-input terminology, and rescreen a reproducible random sample of other exclusions. Report the disagreement rate.
3. **Non-default fall-through.** A record Laya cannot classify is `uncertain_retrieve`, never an exclusion. A generic default exclusion converts screening uncertainty into false certainty.
4. **Count reconciliation.** Retrieved, deduplicated, screened, promoted, retrieved-full-text, and included counts must reconcile and be reported in the screening flow.

## Confidence is uncalibrated

Laya's answer probability is not a calibrated probability. Measured expected calibration error on a scientific-literature screening corpus ran 0.092–0.281, and the checkpoint itself warns that affected confidences are uncalibrated. Record `confidence` as a diagnostic value. Do not use it to set a triage threshold, and do not describe it as a probability of correctness.

## Measured performance on this task family (disclose it)

An internal pilot scored a pinned Laya build on scientific-literature title/abstract screening. Its results are part of the basis for every screen this skill produces and belong in the review's limitations:

| Configuration | Promoted | Cohen's kappa | ECE | Promotion recall | Exclusion recall |
|---|---|---|---|---|---|
| thin criteria | 94% | 0.044 | 0.143 | 0.663 | 0.512 |
| full protocol criteria | 94% | 0.022 | 0.104 | 0.982 | 0.060 |
| multilingual, long input | 94% | 0.010 | 0.092 | 0.928 | 0.107 |
| typed decisions | 94% | 0.010 | 0.092 | 0.928 | 0.107 |

Read this honestly: given explicit criteria the model promoted roughly 94% of records, so high promotion recall came with promotion precision near 0.08. Its exclusion recall was 0.06–0.51. As a two-stage pre-screen it saved on the order of 4% of screening volume while dropping a non-trivial share of eligible records.

Consequences that follow, and that the review must state:

- **Recall, not precision, is the risk.** The failure mode to guard is a **false negative** — an eligible record excluded before anyone reads it. The sentinel regression and the target-term audit exist for exactly this.
- The screen's **agreement with any prior screen is not evidence of correctness.** Agreement is agreement.
- Every review using this screen reports the measured performance above in its limitations, plus its own sentinel and audit outcome.

## Known engineering requirements

- `predict_batch(..., sort_by_length=True)` is worth roughly 60x on this workload: the cost is padding waste from batching a short record beside a long one. It is order-safe — verified identical labels and probabilities against individual calls.
- The yes/no question type is `noul`, not `boolean`.
- Checkpoints are selected with `Router(default=...)`, not `model=...`.
- Full-pool title/abstract scoring is minutes, not hours, once sorted batching is on.
