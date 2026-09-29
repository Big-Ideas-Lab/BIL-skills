---
name: literature-evidence-synthesis
description: Find, verify, and synthesize scientific evidence.
disable-model-invocation: false
argument-hint: "What scientific question or claim needs an evidence brief?"
---

# Literature evidence synthesis

Turn a scientific question into an inspectable evidence package: an **evidence brief**, an **evidence table**, a **claim-to-source map**, and a **screening flow**. The skill governs retrieval, screening, source verification, and provenance. It does not pick a research direction and does not assess hypotheses — hand those to `hypothesis-assessment`.

Consensus MCP is the required discovery route in both lanes. It is a discovery layer only: snippets, abstracts, and library metadata never verify a claim.

Laya is the required first-pass screener at **both** the title/abstract and full-text stages. Its decisions stand without human confirmation, and every one of them is logged with its criterion and supporting span.

## When to Use

- A literature-dependent, causal, clinical, quantitative, or novelty claim could change a research decision.
- A lab member asks for an evidence brief, evidence table, claim-to-source map, screening flow, gap map, or novelty check.
- A manuscript, grant section, or slide needs cited claims grounded in retrievable sources.

Don't use for: casual orientation with no cited claim, hypothesis scoring (use `hypothesis-assessment`), grammar or style passes, or assembling a topic-level report (use `research-topic-report`).

## Lanes

| Lane | Use for | Required before finishing |
|---|---|---|
| **routine** | bounded questions, orientation that still needs citations, a single claim check | Consensus MCP query, Laya screen at both stages, per-claim source locator, honest access limits |
| **decision-grade** | anything that changes a research decision, protocol, or a claim that will appear as established | everything in routine, plus an independent search route, a frozen screening protocol, the sentinel and audit safeguards, and full-text verification of every verified claim |

Escalate to decision-grade without asking when the question sets a research or clinical direction, enters a manuscript, or supports a go/no-go decision. Otherwise recommend the lane and let the requester choose. Never silently expand a routine request into a decision-grade review.

## Procedure

1. **Route the lane.** State the decision the answer could change and the lane you selected. Completion criterion: the lane and its escalation reason are written down.
2. **Query Consensus MCP.** Run the official endpoint `https://mcp.consensus.app/mcp` (search tool only) and record every query verbatim with its timestamp and returned candidates. If the endpoint is unreachable, unconfigured, or unauthenticated, **stop and disclose it**; do not substitute a different route and call the requirement met. Completion criterion: the query log shows at least one Consensus query per research question, or a disclosed blocker.
3. **Add an independent route (decision-grade).** Query at least one route that is not Consensus — a bibliographic database, a registry, a preprint server, or a citation-chaining pass. Consensus may not be the sole search route for decision-grade work. Completion criterion: at least two distinct routes appear in the search ledger.
4. **Freeze eligibility criteria before screening.** Write inclusion and exclusion criteria down, then apply them to every deduplicated record. Never implement eligibility as a preselected DOI/PMID/PMCID allowlist; identifier lists are regression fixtures only. Completion criterion: criteria are timestamped before the first screening decision.
5. **Screen title/abstract with Laya.** Run the pinned Laya build at the title/abstract stage into `promote_full_text`, `exclude_title_abstract`, or `uncertain_retrieve`, and record one log row per record carrying `decision`, `criterion_id`, `supporting_span`, `confidence`, model identity, and input length. See `references/laya-screening.md` for the pinned identity and the required decision record. A fall-through decision is `uncertain_retrieve`, never exclusion. Completion criterion: every deduplicated record has a logged decision naming a criterion and a supporting span.
6. **Run the screening safeguards.** The sentinel regression must pass, every target-term exclusion is audited, and all uncertain records plus a reproducible sample of exclusions are independently rescreened with the disagreement rate reported. A sentinel failure invalidates the screen regardless of the rest. Completion criterion: sentinels pass and the audit results are reported.
7. **Retrieve, then screen full text with Laya.** Retrieve full text for advanced records, then run the same pinned Laya build at the full-text stage into `include_core`, `include_contrast`, `exclude_full_text`, or `awaiting_full_text`, applying the full-text gates. Log every decision the same way and record the truncation policy, `input_chars`, and `truncated` per record. For each verified record capture item identity, DOI/PMID/PMCID, source type, peer-review state, full-text locator, version, hash, and timestamp, and grade the evidence (see `references/evidence-grading.md`). An inaccessible paper stays `awaiting_full_text` — it is not excluded and cannot verify a claim. Completion criterion: every full-text decision names its gate or criterion, and every claim presented as verified has accessible full text and a positive verification record.
8. **Record evaluation metrics comparably.** For any performance comparison, capture task, event unit, reference standard and its uncertainty, matching window or tolerance, split unit, validation type, comparator, threshold-selection procedure, metric definition, numerator, denominator, aggregation level, uncertainty, and failure handling. Compare numbers only within compatible strata; otherwise show them side by side and label them non-comparable. Completion criterion: no ranking combines incompatible protocols.
9. **Build the four artifacts** from `templates/evidence-brief.md`, `templates/evidence-table.csv`, `templates/claim-source-map.csv`, and `templates/prisma-flow.md`, with the screening log in `templates/screening-log.csv`. Label each claim's epistemic status — evidence, synthesis, inference, speculation, mixed, or unknown — and abstain locally where support is missing or contradictory. Completion criterion: every displayed claim resolves to a source record and a verification state, and the screening-flow counts satisfy every reconciliation rule.
10. **Report the screen's basis.** Put Laya's pinned identity, its measured performance, the truncation policy with the truncated count, the sentinel outcome, and the audited disagreement rate in the limitations section. A reader must be able to see which records advanced on a model decision and what that model's measured behaviour is. Completion criterion: the limitations section carries all five items.

## Deliverables

| Artifact | Template | Purpose |
|---|---|---|
| Evidence brief | `templates/evidence-brief.md` | readable synthesis: question, lane, findings, disagreements, limitations |
| Evidence table | `templates/evidence-table.csv` | one row per included source with grading and comparability fields |
| Claim-to-source map | `templates/claim-source-map.csv` | one row per decision-relevant claim with locator and verification state |
| Screening flow | `templates/prisma-flow.md` | PRISMA-like diagram and reconciled counts, with exclusion reasons and Laya attribution |
| Screening log | `templates/screening-log.csv` | one row per record per stage: decision, criterion, supporting span, confidence, model identity |

## Pitfalls

- Treating Consensus results, abstracts, or metadata as claim verification.
- Making Consensus the only search route for decision-grade work.
- Excluding records by default so screening uncertainty becomes false certainty.
- Logging a model decision without a criterion and a supporting span. The decision is then unreproducible and unauditable.
- Reading Laya's `confidence` as a probability of correctness. It is uncalibrated; measured ECE on this task family ran 0.09–0.28.
- Reporting the screen's agreement with a prior screen as evidence of correctness. The failure mode that matters is a **false negative** — an eligible record excluded before anyone reads it.
- Screening a truncated full text and then declaring a gate verdict that depends on the omitted material.
- Silently converting an evidence brief into a full review, or implying exhaustive coverage from scoping.
- Pooling preprints, conference papers, registries, and grey literature as equivalent support, or letting volume substitute for quality.
- Ranking metrics computed on incompatible event units, splits, or tolerance windows.
- Reporting a claim as established when its source is `awaiting_full_text`.
- Letting a retriever, vector index, or agent summary become the canonical literature store.

## Verification

Before declaring the package finished:

- [ ] Lane stated, with the Consensus query log and (decision-grade) a second search route.
- [ ] Eligibility criteria frozen before screening and applied to every deduplicated record.
- [ ] No inclusion produced by an identifier allowlist; no exclusion produced by a default.
- [ ] Every record carries a logged Laya decision with `criterion_id`, `supporting_span`, model identity, and input length.
- [ ] Sentinel eligible papers pass, and the exclusion audit plus residual false-negative risk are reported.
- [ ] The truncation policy is recorded with its truncated count, and no gate verdict rests on omitted text.
- [ ] Every verified claim has accessible full text and a source locator.
- [ ] Cross-paper metrics are compared only within compatible strata.
- [ ] The screening flow exists, uses the real counts, satisfies every reconciliation rule, and never hides `awaiting_full_text`.
- [ ] Laya's pinned identity and measured performance appear in the limitations section.
- [ ] Contradictory evidence, inaccessible sources, and empty states are visible.
- [ ] All four artifacts exist and every claim links to a source record.

Run `python3 scripts/validate.py` from this skill directory to check the package structure, the Consensus requirement, the Laya screening requirement, and the screening-flow deliverable.

## References

- `references/consensus-and-search-routes.md` — Consensus MCP setup, scoping, and the independent-route requirement.
- `references/laya-screening.md` — pinned Laya identity, both screening stages, the decision record, truncation policy, safeguards, and measured performance.
- `references/evidence-grading.md` — grading dimensions and epistemic labels.
- `references/evaluation-comparability.md` — the metric-capture contract for cross-paper comparison.
- `references/decision-grade-gates.md` — the full gate list, sentinel pattern, and false-negative accounting.
