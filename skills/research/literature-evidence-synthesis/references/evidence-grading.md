# Evidence grading and epistemic labels

Grade each included source on its own merits, then label each **claim** by how it is supported. Grading a source is not the same as verifying a claim.

## Source-level grading dimensions

| Dimension | Question |
|---|---|
| Design fit | Does the study design answer this question type, or a neighbouring one? |
| Bias | What systematic error could produce this result without the effect being real? |
| Directness | Is the population, exposure, outcome, and setting the one you care about? |
| Consistency | Do independent studies agree, or does this result stand alone? |
| Precision | How wide is the uncertainty, and what is the denominator? |
| Replication | Has it been reproduced independently, in another cohort or by another group? |
| Verification depth | Is there accessible full text, and did you read the part that supports the claim? |

Record each dimension explicitly. "Strong" or "weak" without a dimension attached is not a grade.

## Verification states

| State | Meaning |
|---|---|
| `full-text verified` | Accessible full text read; the locator supports the claim as stated |
| `abstract only` | Only the abstract was accessible; cannot verify a decision-relevant claim |
| `awaiting_full_text` | Relevant, but full text was not obtained; stays in the record, excluded from verification |
| `metadata only` | Index record with no abstract; discovery role only |
| `unsupported` | No source found that supports the claim as stated |

`awaiting_full_text` is a **holding state, not an exclusion**. Never let it disappear from the record, and never let it carry a claim.

## Claim-level epistemic labels

| Label | Use when |
|---|---|
| `evidence` | Directly supported by a verified source |
| `synthesis` | A reasoned combination of two or more verified sources |
| `inference` | Follows from evidence but is not itself reported |
| `speculation` | Plausible but unsupported; label explicitly if it must appear |
| `mixed` | Sources disagree; report the disagreement rather than an average |
| `unknown` | Not determined; abstain locally |

Label at the granularity that matters for a decision. Do not tag every sentence, and never leave a decision-relevant claim unlabelled.

## Evidence-class separation

Keep non-journal evidence classes distinct rather than pooling them as equivalent support:

- peer-reviewed journal articles
- preprints
- conference papers and abstracts
- registered protocols and registries
- datasets and software
- guidelines and agency documents
- grey literature and reports

Volume never substitutes for quality. Ten abstracts do not verify one claim.

## Local abstention

When support is missing or contradictory:

1. Return the portion that is supported.
2. Mark the exact boundary where support ends.
3. Abstain locally rather than generalizing.
4. Propose the smallest next step that could resolve the gap.

Never replace missing evidence with confidence.
