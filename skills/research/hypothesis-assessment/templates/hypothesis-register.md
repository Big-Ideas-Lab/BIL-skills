# Hypothesis register

> Template. Replace every `<>` placeholder. One block per hypothesis. Delete guidance lines before delivery.
> Mode: `<generate-then-assess | assess-supplied>` · Lane: `<routine | decision-grade>`

## Input

**Research direction (fixed input):** `<the direction this assessment assumes, not chooses>`
**Question:** `<the question being tested>`
**Inferential boundary:** `<what the data observe directly versus what needs labels or causal assumptions>`

## Hypothesis H`<n>`

| Field | Value |
|---|---|
| Class | `<focal | rival | null | artifact/confounding | high-upside>` |
| Title | `<short name>` |
| Claim | `<one sentence, under 180 characters>` |
| Prediction | `<the expected pattern, with unit and window>` |
| Decisive comparison | `<the comparison that separates this from its alternatives>` |
| Falsifier | `<what observation would count against it>` |
| Minimum evidence | `<the smallest informative dataset or experiment>` |
| Claim state | `<hypothesis | rival | null | unsupported>` |

**Axes**

| Axis | Rating | Rationale |
|---|---|---|
| Scientific risk | `<Low | Moderate | High>` | `<one line>` |
| Execution risk | `<Low | Moderate | High>` | `<one line>` |
| Time to evidence | `<Short | Medium | Long>` | `<one line>` |
| Potential impact | `<Low | Moderate | High>` | `<one line>` |

**Alternative explanations** *(decision-grade, shortlisted hypotheses)*

- Rival mechanism: `<mechanism and the observation that separates it>`
- Null or redundancy: `<the strongest existing metric this must beat>`
- Artifact or confounding: `<named mechanism and detection path>`

## Trade-off summary

`<Dominance relationships and the non-dominant trade-offs. Do not compute a composite score.>`

**Most uncertain axis:** `<axis>` — `<the measurement that would most reduce that uncertainty>`

## Critic pass *(decision-grade)*

- Independence: `<independent fresh context | same-context — labeled honestly>`
- Findings: `<prioritized critique>`
- Preserved dissent: `<objections not adopted, recorded verbatim>`

## Unresolved questions

- `<what remains unknown and who could resolve it>`
