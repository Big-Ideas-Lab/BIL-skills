---
name: hypothesis-assessment
description: Generate and assess hypothesis options on risk and impact.
disable-model-invocation: false
argument-hint: "Which hypotheses should we assess, or which topic needs candidate hypotheses?"
---

# Hypothesis assessment

Generate candidate hypotheses when needed, then assess them on four visible axes: **scientific risk**, **execution risk**, **time to evidence**, and **potential impact**. The output is a hypothesis register plus a risk–impact matrix that exposes trade-offs.

The research direction is an **input**. It is defined upstream of literature work; this skill does not choose a direction, and it does not replace `literature-evidence-synthesis`.

## When to Use

- A lab member has candidate hypotheses and wants them compared before committing effort.
- A topic or evidence brief needs genuinely different candidate hypotheses generated before assessment.
- A proposed mechanism, endpoint, or analysis needs a falsifier and a minimum-evidence statement.
- A shortlist needs rival, null, and artifact/confounding explanations made explicit.

Don't use for: choosing a research direction, retrieving or verifying literature (use `literature-evidence-synthesis`), producing a topic-level report (use `research-topic-report`), or confirming a hypothesis portfolio already accepted by the group.

## Modes

| Mode | Entry condition | Output |
|---|---|---|
| **assess-supplied** | the requester already has hypotheses | register plus matrix over the supplied set |
| **generate-then-assess** | the requester has a topic, question, or evidence brief but no hypothesis set | a divergent candidate set, then the same register and matrix |

Ask which mode applies only when it is genuinely ambiguous. A request phrased "here are our candidate mechanisms, rank them" is assess-supplied. "What should we test here?" is generate-then-assess.

## Lanes

| Lane | Use for | Required before finishing |
|---|---|---|
| **routine** | triage, a quick read on which idea is worth a meeting, early brainstorming | the four axes scored ordinally with a one-line rationale each |
| **decision-grade** | committing effort, a protocol, a grant aim, or a manuscript claim | everything in routine, plus falsifiers, minimum evidence, rival/null/artifact explanations, and an independent critic pass |

## Procedure

1. **Fix the input.** Restate the research direction, question, and inferential boundary you are assessing against. Separate what the data directly observe from what would need labels, causal assumptions, or external validation. Completion criterion: the direction is stated as fixed input, not as a choice this skill makes.
2. **Choose the mode** and, for `generate-then-assess`, generate candidates before scoring anything. Generate mechanisms that differ in kind, not paraphrases — see `references/hypothesis-generation.md`. Completion criterion: no two candidates share the same mechanism.
3. **State each hypothesis as a testable claim.** Name the predicted pattern, the comparison, and the observation that would count against it. Completion criterion: every row has a prediction and an observable outcome.
4. **Score the four axes** with ordinal ratings and a one-line justification per axis. Use `references/risk-impact-axes.md` for the axis definitions and anchors, and `templates/risk-impact-matrix.csv` for the record. Completion criterion: every hypothesis has four ratings, each with a written rationale.
5. **Do not collapse the axes.** Never produce a single composite score, weighted total, or composite ranking. Present the matrix and call out Pareto-dominant options — hypotheses that are no worse on any axis and clearly better on at least one. Completion criterion: no composite score appears anywhere in the output.
6. **Add the explanation classes (decision-grade).** For each shortlisted hypothesis, state the rival mechanism, the null or redundancy explanation, and the artifact/confounding explanation. These apply to the shortlist, not to every generated idea. Completion criterion: each shortlisted hypothesis names its rival, null, and artifact alternatives.
7. **State falsifiers and minimum evidence (decision-grade).** For each shortlisted hypothesis, name the decisive comparison, the smallest informative dataset or experiment, and the result that would falsify it. Completion criterion: every shortlisted hypothesis has a checkable falsifier and a minimum-evidence statement.
8. **Run an independent critic pass (decision-grade).** Use a fresh context that has not seen the requester's or generator's preferred option, then report its disagreements instead of averaging them away. If a fresh context is unavailable, label the pass as same-context and say so. Completion criterion: the critic's dissent is recorded verbatim, not resolved.
9. **Report trade-offs honestly.** Lead with the matrix, not a winner. Name what remains unknown, which axis is most uncertain, and which single measurement would most reduce uncertainty. Completion criterion: the reader can see the trade-off without reading a narrative.

## Deliverables

| Artifact | Template | Purpose |
|---|---|---|
| Hypothesis register | `templates/hypothesis-register.md` | per-hypothesis claim, prediction, falsifier, minimum evidence, classes |
| Risk–impact matrix | `templates/risk-impact-matrix.csv` | ordinal ratings and rationale for the four axes |

## Pitfalls

- Inventing a single risk-adjusted score that hides a decisive trade-off.
- Generating paraphrases and calling them rival mechanisms.
- Treating "high impact" as permission to skip feasibility, identifiability, or time-to-evidence.
- Assessing outcome associations before the measurement itself is validated.
- Naming algorithm-defined events by causal names the labels cannot support.
- Forcing the five hypothesis classes onto every brainstormed idea instead of the shortlist.
- Letting a same-context critic pass masquerade as an independent one.
- Ranking hypotheses by the requester's preferred direction rather than the stated axes.

## Verification

Before declaring the assessment ready:

- [ ] Research direction and inferential boundary restated as fixed input.
- [ ] Mode stated; candidates generated before any scoring in `generate-then-assess`.
- [ ] Every hypothesis has a prediction and a checkable falsifier.
- [ ] All four axes rated with written rationale; no composite score anywhere.
- [ ] Pareto-dominant options identified and the most uncertain axis named.
- [ ] Decision-grade: rival, null, and artifact explanations present for every shortlisted hypothesis.
- [ ] Decision-grade: minimum-evidence statements are concrete and non-circular.
- [ ] Critic disagreements preserved, with the pass labeled independent or same-context.

Run `python3 scripts/validate.py` from this skill directory to check the package structure and the four-axis requirement.

## References

- `references/risk-impact-axes.md` — axis definitions, ordinal anchors, and Pareto guidance.
- `references/hypothesis-generation.md` — divergent generation procedure for `generate-then-assess`.
- `references/hypothesis-classes.md` — focal, rival, null, artifact/confounding, and high-upside definitions.
