# MEASUREMENT DESIGN — for adversarial review

**Status: UNREVIEWED. Written 2026-07-29. Nothing here has been run.** This document exists to be
attacked. Every number in it is a plan, not a result.

---

## The two questions

**Q1 · REPRESENTATION.** Collective-alignment systems claim their output *represents* the people whose
judgements were aggregated. Nobody has measured this by asking whether the output reproduces the
judgement of the individuals who supplied it. The field reports one pooled accuracy.

**Q2 · COMPILATION LOSS.** These systems *compile* a set of human judgements into a program that then
executes without an interpreter — no discretion, no "this case is different", no appeal. What does the
compilation discard, and does the discarded part carry decisions?

---

## Two principles the design rests on

**P1 — A loss is real only if restoring it changes a decision.** Saying "compression discarded
nuance" is free; every compression discards something. **The positive control for a loss measure is a
RESTORATION experiment.** If putting the discarded quantity back changes no decision, the loss is not
load-bearing and the finding is dead.

**P2 — Representation must be measured per-person, leave-one-out, and normalised by that person's own
reliability.** A pooled 0.686 is compatible with *everyone represented at 0.686* and with *70% at 0.9
and 30% at 0.2*. Those are different worlds and only the second contains people who contributed and
got nothing back. **The distribution is the finding; the mean is what hid it.**

---

## The data, and why these questions are answerable on it

| dataset | what it carries per person | why it permits leave-one-out |
|---|---|---|
| **CoVal** (`data/conversation_rubrics.jsonl`, `data/comparisons.jsonl`) | each participant contributes (a) free-text criteria, (b) −10..+10 ratings on criteria with `annotator_id`, (c) their **own ranking** of the 4 responses | inputs and the individual's own judgement are both present and separable |
| **Community Notes** (public daily TSVs) | rater id, per-note rating, note status history; the **scoring algorithm is open source and recomputable** | drop rater *i*, refit, compare to *i*'s own ratings. ~10⁵–10⁶ raters |
| **DICES** | rater votes **plus demographics**, disagreement deliberately oversampled | same estimator, then split by group |

**CoVal also carries the compiler itself**: `coval_full` (criteria + every rating) and `coval_core`
(rewritten, merged, polarity-normalised, ≤4 criteria). **Both sides of the compilation are on disk.**

---

## Q2 — three measures

### M1 · Expressivity loss — a pure count

`coval_core` is **polarity-normalised to positive form**: *"The response moralises"* + negative weight
compiles to *"Avoid moralising."* A criterion whose human ratings **split in sign** — some +8, some −7
— **cannot be expressed in a single-polarity sentence at all.**

- **Estimand:** the count of sign-split `coval_full` criteria, and their share of total weight mass.
- **Null:** permute ratings within criterion; how often does this degree of split arise by chance?
  Without it, "bimodal" is small-sample noise.
- **Why it is valid:** it does not measure whether core is *good*. It measures **what the core FORM can
  carry.** It is a count; no coder, no semantic matching, no model.
- **Pre-registered kill:** if sign-split criteria hold <5% of weight mass, this line shrinks to a
  footnote and M2/M3 are not worth running.

### M2 · Provenance loss, validated by restoration

- **Estimand:** decisions changed when the discarded disagreement is put back.
- **Procedure:** match each `coval_core` criterion to its `coval_full` ancestors; recover the discarded
  disagreement statistic (rating variance, sign split); **re-weight core by it** (down-weight
  contested); rescore; count changed pairwise decisions.
- **Positive control:** plant a synthetic criterion with **known** high disagreement — restoration must
  detect it.
- **Negative control, and it is the load-bearing one:** re-weight by a **random** quantity of the same
  magnitude. **The real restoration must move decisions significantly more than the random one** —
  otherwise the measure only shows the system is unstable under *any* perturbation.
- **Pre-registered kill:** real ≈ random ⇒ the loss is not load-bearing. Report it and close the line.

### M3 · Where the loss lands

- **Estimand:** the conditional distribution of full-vs-core disagreement given **human** disagreement
  on that pair.
- **Reading:** concentrated on high-human-disagreement pairs ⇒ the compiler flattens contested cases,
  which is a statable mechanism. Uniform ⇒ compilation is noise, not flattening.
- ⚠ CoVal r33 already measured that core **beats** full by +0.0663 at equal weights. **That was
  accuracy. This is localisation. Same data, different question** — and the overlap must be declared.

---

## Q1 — the representation estimator

For participant *i* on prompt *p*:

```
R₋ᵢ    = the aggregate rubric built from every participant EXCEPT i
repᵢ   = accuracy of R₋ᵢ against i's OWN ranking          (out-of-sample representation)
floorᵢ = accuracy of a rubric from a DIFFERENT prompt against i's ranking   (generic quality)
ceilᵢ  = accuracy of the aggregate INCLUDING i                              (i's own influence)
relᵢ   = i's own self-consistency                                           (what is achievable)
```

**Reported quantity: the DISTRIBUTION of `repᵢ` across people, and specifically the share of
participants for whom `repᵢ ≤ floorᵢ`** — people who supplied input and got back no more than a
stranger's rubric would have given them.

**Same estimator on Community Notes**: drop rater *i*, refit the open-source scorer, ask whether the
resulting note statuses agree with *i*'s own ratings. **On DICES**: identical, then split by demographic
group.

### Controls

- **Positive:** a synthetic participant whose criteria **are** the aggregate must score ≈1.0.
- **Complementary:** a random participant against a **different prompt's** aggregate must score at the
  floor. **Both are required** — an instrument that returns 0.5 for everything would pass the first
  alone.
- **Reliability normalisation:** a participant who is not self-consistent cannot be represented by
  anything. **Report `repᵢ` relative to `relᵢ`**, or misrepresentation and noise are the same number.

---

## The statistical apparatus, and the traps it is built against

| trap | why it destroys the result | the design's answer |
|---|---|---|
| wrong unit | reporting pairwise n treats 968 prompts as ~80,000 independent observations | **cluster on the person**; CoVal measured a design effect of **1.499** for prompt clustering |
| **LOO estimates are dependent** | every `R₋ᵢ` shares almost all its data with every other; naive intervals will be far too narrow | **cluster bootstrap over people** — ⚠ *and whether this is even valid under LOO dependence is the sharpest open question in this design* |
| noise read as misrepresentation | an internally inconsistent participant is unrepresentable by construction | divide by `relᵢ` |
| no floor | `rep = 0.62` sounds low until you learn generic quality gives 0.58 | per-person `floorᵢ` from a different prompt |
| significance ≠ equivalence | p>0.05 is not "no effect" | report separately, margin **pre-registered**; a small point estimate with a wide interval is an **ANSWERABLE MARGIN** and is labelled as one |
| multiplicity | demographic splits generate dozens of subgroups | pre-register which splits; everything else is exploratory and labelled |
| **the mean hides the finding** | this is the field's actual error | **report quantiles and the lower tail**; the mean is a footnote |

---

## Pre-registered failure modes — both must be acceptable or this is not an experiment

- **Q2 fails** if restoration changes **no** decisions, or changes them no more than a random
  re-weighting. Then the compilation loss is not load-bearing.
- **Q1 fails** if the `repᵢ` distribution is **unimodal and tight**. Then there is no abandoned
  minority — which is a real result and a **defence** of these systems.

---

## Sequencing

**M1 first**, because it is a pure count on data already on disk, needs no model, and **decides whether
Q2 is worth running at all.**

---

## Known weaknesses the author is already aware of (attack these too, harder)

1. **`relᵢ` may not be estimable in CoVal** — each participant ranks 4 responses once, giving 6 pairs
   from a single ordering, so there is **no within-person replication**. The proposed ceiling may not
   exist, and the whole normalisation could be unfounded.
2. **Semantic matching of core criteria to full ancestors** (M2) is a model-based step inside a design
   that otherwise avoids models. It could dominate the result.
3. **"Representation" as reproduction of a person's ranking assumes their ranking is what should be
   represented** — a person might endorse an aggregate that contradicts their ranking, on the grounds
   that others' reasons were better. **The estimator cannot see that, and it may be measuring
   agreement rather than endorsement.**
