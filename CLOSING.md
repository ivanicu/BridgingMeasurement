# Closing statement

**Programme:** collective-alignment measurement. **Closed 2026-07-29**, on a pre-registered kill that
fired. 25 ledger entries, 114 rounds, **14 retractions**.

The stopping condition was written before the last round ran: *no demographic group departing from the
arithmetic line after Benjamini-Hochberg, while the positive control still recovers a planted effect →
the redistribution is anonymous, "identifiable subgroup" leaves the claim permanently, and it is not to
be reopened on another dataset.* Both conditions were met. This document claims what the programme is
entitled to claim and names what it is not.

---

## What the programme found

**1 · Compilation moved polarity out of the ratings and into the wording.** Applying the human ratings
to CoVal-core changes its pairwise concordance by **exactly 0.0 to fifteen digits** —
`0.656254647418647` under equal, sign, and signed-magnitude weighting alike — while `full` needs those
ratings to climb from **0.5899** to **0.6831**. A control that cannot be improved on: the compiled
rubric has no ratings to apply because the direction is already in the sentence.

**2 · Compilation improves agreement with nearly everyone.** μ falls **0.06870**, and absolute error is
lower under core in **6 of 6** equal-count bins of the Oldham axis, including the worst-served bin
(**0.5313 → 0.5021**).

**3 · It redistributes the *size* of that improvement**, from **−0.1038** at the best-served 5% to
**−0.0292** at the worst, monotone across six bins. **The gradient's sign is not identified by binning
on either arm alone** — full's α gives −0.043 → −0.077 and core's α gives −0.133 → −0.032, *opposite
signs from the same data* (Oldham 1962). Only the mean-of-arms axis is admissible.

**4 · A rater-attached component is real.** On the excess-over-count-preserving-floor scale:
**+0.00184 to +0.00225**, estimand-invariant across four estimands, 95% CI over prompts
**[+0.00114, +0.00275]**, flat under low-*n* exclusion, and **not reducible to which prompts a rater
met** — exposure covariates remove **22.0%** against a permuted-covariate floor of **2.6%
[1.3%, 4.7%]**.

**5 · That component has no subject, and the null is not underpowered.** Across six demographic axes at
**100% coverage** (1,012 of 1,012 annotators, 47 group cells), **30 cells** cleared a pre-registered
floor of 20 raters; the largest |t| on the departure-from-the-arithmetic-line estimand is **1.83**
(p = 0.0669) and **0 survive** BH at q = 0.05. The positive control plants a one-armed group effect and
recovers it at **89.9% retention, t 4.89**, with **MDE ≈ g 0.0115** — against a redistribution whose own
spread is ≈ **0.075**. An effect *seven times smaller than the thing being explained* would have been
detected. The negative control is **not** a permutation: 200 synthetic groups matched on size **and**
mean own-error give a band of **[−0.00814, +0.00697]**, so a group differing only in noisiness lands on
the line.

> **The ontology this leaves.** A compilation audit's object is not harm and not accuracy — it is the
> **distribution of a benefit**. And that distribution can be real, measurable, attached to particular
> people, and **still have no describable character**. "Who is disadvantaged by this rule" can have a
> true answer that names nobody. Impact assessments, demographic audits and subgroup fairness reports
> are built on the premise that a real disparity has a nameable subject; here one does not.

**6 · Three walls on this release, each verified against the object rather than assumed.** No
within-cell replication → the rater×prompt interaction and test–retest reliability are unidentified.
No presentation-order field → the case component can never be called discretion. `coval_core` items
carry `['criterion']` and nothing else → **the compiler has no provenance.**

---

## The methods result, which is the largest thing here

**7 · Regressing a paired difference of two rules' per-rater error on a rater-level covariate produces
a coefficient set by the rules' *accuracy gap*, not by what distinguishes the rules.** On 7,275 cells
across 7 arm pairs from 5 arms: **not one pair departs from the accuracy-gap line by more than its own
noise** — residual sd **0.00743**, mean |resid| **0.00636**, against a mean standard error of
**0.00858**; one of seven exceeds a single se and the largest departure is **|z| = 1.58**. A
never-compiled arm gives a **larger** coefficient (**+0.06156**) than the compiled one (**+0.03955**);
an arm with almost no gap gives none (**+0.00041**, t 0.06).

*The mechanism:* any covariate raising **both** arms' errors yields a differential proportional to their
gap, because the more accurate arm has more advantage to lose. *The remedy:* an accuracy-matched
comparator, or an Oldham-type purge that is **positive-controlled** — ours retains **117%** of a planted
one-armed effect at t 5.48 and detects g = 0.02 at t 2.99.

**8 · A permutation null answers *did the pairing matter*, never *why*.** Demonstrated, not asserted:
a within-prompt permutation of whole score profiles returns **p_perm 0.0000 on synthetic data
containing no values at all**, and a generator whose only input is "probability the rater ranks
randomly" reproduces **77%** of the effect it was supposed to protect.

**9 · A two-hashseed reproducibility gate certifies determinism, not currency.** It compares two fresh
runs of the same file *to each other*, never to disk. One round's committed JSON was not the output of
its committed code, and the ledger quoted a positive-control value that appears in no output.

**10 · The raw variance of fitted rater means is the component *plus* `var_resid × E[1/n_i]`** — at
these counts, **0.00416**, i.e. most of the raw number.

---

## The programme's own base rate

Offered as the most transferable content in this document.

| | count |
|---|---|
| claims of the form *"X is unavailable / requires a different dataset / nobody has done X"* that died **with the falsifying material already on disk** | **12** |
| field-level novelty claims that died | **6 of 6** |
| times a permutation null was placed in the load-bearing gate position | **3** |
| total retractions | **14** |

Not one was caught by pre-registration, positive controls, three-valued verdicts, or a post-hoc
adversary. Every one was caught by reading a primary source, by re-reading the programme's own prior
output, or by an independent navigator **building the world the diagnostics could only price**. The
apparatus disciplines what happens *after* committing to a design; the failures happened at
**assertion** and at **direction-choice**, upstream of anywhere it applies.

---

## What this document does NOT claim

- Any sentence of the form *"nobody has measured X"* or *"X requires a different dataset."*
- *"Compilation returns least to the raters whose own stated values sit furthest from the consensus"* —
  **retracted**, and not revivable through the per-arm levels.
- *"Compilation decouples error from cases **and couples it to people**"* — the second verb is wrong.
  **Winners and smaller winners, not winners and losers.**
- *"Particular raters are systematically worse served"* — killed twice. α is re-centred within arm and
  cannot carry an absolute claim.
- That the polarity story is either confirmed or refuted. x2 alone is **+0.03110** (se 0.01984 → t 1.73)
  on one population and +0.03644 (t 2.79) on the other, and purged it is **+0.01702** (t 0.86).
  **UNVERIFIED in both directions**; re-promoting it would be the mirror of the error.
- That any finding transfers to Community Notes via `raterParams` "with no new data collection."
- That the methods result (**7**) is **novel**. A bounded search of Crossref and DBLP over ~18 queries
  did not find it; the nearest neighbours are the Oldham/change-score-versus-baseline literature and
  Cleary-model differential validity, neither of which is the two-rules-difference confound. **"Not
  found in a bounded search"** is the ceiling. Six of six novelty claims here have died.
- That within-cell replication is absent from public rater data **generally**. Four objects were
  counted — CoVal, DICES-350, DICES-990, PRISM — and all four have max count per (rater, item) = 1.
  **That is the scope of the claim.**
- That the anonymity result (**5**) generalises beyond this release. It is a statement about the only
  release carrying both the compilation contrast and the demographics.

---

## Why nothing else opens

| site | status | verified |
|---|---|---|
| **DICES** | already published on this estimand | GRASP, [arXiv 2311.05074](https://arxiv.org/abs/2311.05074), NAACL 2024 — in-group/cross-group cohesion on race, gender, age and intersections. And it does not break wall #1: max count per (rater, item) = 1 in both DICES-350 and DICES-990 |
| **PRISM** | cannot form the estimand | 0 of 8,011 conversations have more than one distinct `user_id`; items are participant-private, so rater and item effects are not separable |
| **Community Notes** | one aggregation rule | there is no paired contrast `d` to regress; construct one and it differs in accuracy, reproducing the artifact in **7** |

---

**The package:** [CoValCrossroad](https://github.com/ivanicu/CoValCrossroad) — 114 rounds in 12
campaigns, every round's question, finding and caveats in its README, and every retraction annotated in
place rather than deleted. **The diary:** [`LEDGER.md`](LEDGER.md), 25 entries, one per belief update.
**The machines:** three mechanical gates in [`assurance/`](assurance), each attacked before being
trusted, each shipping with the statement of what it cannot do.
