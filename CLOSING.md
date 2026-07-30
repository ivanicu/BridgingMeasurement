# Closing statement

> ## ⚠ CORRECTED 2026-07-29 after an independent audit found sixteen defects, one of them fatal to a headline
> **A wall this document called part of the deliverable does not exist.** CoVal *has* within-cell
> replication — 18,384 assessments over **18,269** distinct (prompt, rater) cells, 111 replicated,
> max 5 — so **test–retest reliability is estimable and is 0.8446** on 605 comparable pairs. The
> falsifying arithmetic sat in one sentence of the ledger. See [`LEDGER.md`](LEDGER.md) entry 26.
> Also corrected here: an MDE quoted as if it were the test's when it is the best-performing cell's;
> a universal ("not one pair…") the ledger had already narrowed two entries earlier; a "demonstrated"
> that has no artifact; a retraction count with no receipt; and eleven number or scope errors. **Every
> correction is inline and this banner is the record of what the document said.**

**Programme:** collective-alignment measurement. **Closed 2026-07-29**, on a pre-registered kill that
fired. 26 ledger entries, 114 rounds. ⚠ **The retraction count is UNRESOLVED**: this document said
**14**, with no list and no receipt; the sibling README says "eleven of twelve CoVal retractions";
`RETRACTIONS.md` carries 224 entries and its own stale self-count. The ledger has 8 `Killed.` blocks
plus 1 `Withdrawn.`, but blocks retract several claims each, so a claim-level count exceeds 25 and an
entry-level count is ~19–20. **No number is quoted here until one is counted under a stated rule** —
and a document whose headline transferable content is its own error count may not get that count wrong.

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

**And *which* compilation step earns it is decomposed, not confounded.** r33's own verdict says the
share is *not* decomposed — rewrite, merge, dedup, compatibility selection and truncation are
confounded there — but **r44 decomposed it**: the polarity-rewrite step alone is **+0.0733**, larger
than the entire full→core total of **+0.0662** which later stages partly give back, and
**compatibility selection is a real second term at +0.0149** over a size-matched random choice of the
same number of criteria. So *which items survive* carries signal too, and claim 1 is a statement about
the dominant step rather than the only one.

**2 · Compilation improves agreement with nearly everyone.** μ falls **0.06870**, and absolute error is
lower under core in **6 of 6** percentile bins of the Oldham axis (see claim 3 for their
sizes), including the worst-served bin
(**0.5313 → 0.5021**).

**3 · It redistributes the *size* of that improvement**, from **−0.1038** at the best-served 5% to
**−0.0292** at the worst, monotone across six **percentile** bins (n = 51/202/253/253/202/50 — *not*
equal-count, and the two endpoint figures come from the two smallest bins). **The gradient's sign is
not identified by binning on either arm alone** — full's α gives −0.043 → −0.077 while core's α runs
**−0.161 → +0.016**, a gradient that *crosses zero*: opposite signs from the same data (Oldham 1962).
Only the mean-of-arms axis is admissible. (An earlier version quoted −0.133 → −0.032 for core's axis;
that pair was an un-persisted separate computation the ledger records as overstated, and the
artifact's own numbers make the point more strongly.)

**4 · A rater-attached component is real.** On the excess-over-count-preserving-floor scale:
**+0.00184 to +0.00225**, estimand-invariant across **three** estimands on the excess scale
(weighted 0.00184, unweighted 0.00209, moment-corrected 0.00225 — a fourth, an independently built
U-statistic, agrees on the contrast to within 4% but has no excess-scale value), 95% CI over prompts
**[+0.00114, +0.00275]**, flat under low-*n* exclusion, and **not reducible to which prompts a rater
met** — exposure covariates remove **22.0%** against a permuted-covariate floor of **2.6%
[1.3%, 4.7%]**, well inside the pre-registered kill threshold of 50%.

**5 · That component has no demographic subject on the cells that could be tested.** Across six axes at
**100% coverage of the release** (1,012 annotator records; **1,011 raters carry cells** in the analysis
population), 47 group cells: **30 cleared** a pre-registered floor of 20 raters and **17 did not**. The
largest |t| on the departure-from-the-arithmetic-line estimand is **1.83** (p = 0.0669); **0 survive**
BH at q = 0.05, and none survives uncorrected either. The positive control plants a one-armed group
effect and recovers it at **89.9% retention, t 4.89**.

**The power is per-cell, and the document previously quoted one cell as if it were the test.**
MDE ≈ **g 0.0114** at the largest cells (n ≈ 500), **median 0.017** across the 30, rising to **0.057**
at the smallest tested cell (age 65+, n = 22) — so **all 30 exceed 0.0114**. Against the gain gradient
of 0.075 across the full Oldham range, an extreme-bin *indicator* effect is ≈ 0.04, giving roughly
**3.4× headroom at the best-powered cells and none at the worst**. The earlier phrasing — "seven times
smaller… would have been detected", and "the null is not underpowered" as a property of the test — is
**withdrawn**. The negative control is **not** a permutation: 200 synthetic groups matched on size
**and** mean own-error give a band of **[−0.00814, +0.00697]** with the real group at **+0.00289**,
inside it — established at one group size (n = 528), not across the range. And the purge it rests on
**over**-recovers, 117% at g = 0.04 and 131% at g = 0.02, which makes any MDE derived from it
optimistic.

**The 17 untested cells are the ones a fairness audit exists for**, and this document previously did not
say so: every **non-binary** rater (17), every **never-user** of generative AI (14), "not sure/no
answer" on AI concern (14), ten countries, "some high school" (1). In coverage terms the hole is small —
96 rater-memberships, 0.0–3.7% per axis — but the anonymity claim is **over the 30 cells that cleared
the floor**, not over the population.

> **The ontology this leaves.** A compilation audit's object is not harm and not accuracy — it is the
> **distribution of a benefit**. And that distribution can be real, measurable, attached to particular
> people, and **still have no describable character** — at least across the demographic axes this
> release can test at usable power. "Who is disadvantaged by this rule" can have a true answer that
> names nobody. Impact assessments, demographic audits and subgroup fairness reports are built on the
> premise that a real disparity has a nameable subject; here one does not, on 30 of 47 cells.

**6 · TWO walls on this release, not three.** No presentation-order field → the case component cannot
be called discretion. `coval_core` items carry `['criterion']` and nothing else → **the compiler has no
provenance.** Both verified against the object.

> **⛔ The third wall was never verified and is FALSE.** This document claimed "no within-cell
> replication → the rater×prompt interaction and test–retest reliability are unidentified". **111 of
> 18,269 (rater, item) cells carry 2–5 assessments** (0.6% of the release), 57 of 111 give a *different*
> world ranking, and every prompt line holds exactly four responses — so these are re-rankings of the
> same four texts. **Test–retest agreement IS estimable: intra-rater pairwise concordance 0.8446 on 605
> comparable pairs**, against core at 0.666 and full at 0.596 on the same metric. The *interaction* half
> of the wall probably survives on power at n = 111; the *reliability* half does not survive at all.
> There are no timestamps, so this is order-free replicate agreement rather than a temporal retest, and
> no interval was computed. **D9** that the replication exists; **D6** that these are deliberate
> re-ratings; **D6, low precision** that 0.8446 is "the" reliability.

---

## The methods result, which is the largest thing here

**7 · Regressing a paired difference of two rules' per-rater error on a rater-level covariate produces
a coefficient set by the rules' *accuracy gap*, not by what distinguishes the rules.** On 7,275 cells
across 7 arm pairs from 5 arms: **not one pair is statistically distinguishable from the accuracy-gap
line** — one of seven exceeds a single standard error, **none exceeds two**, and the largest
departure is **|z| = 1.58**; residual sd **0.00743**, mean |resid| **0.00636**, mean se **0.00858**. A
never-compiled arm gives a **larger** coefficient (**+0.06156**) than the compiled one (**+0.03955**);
an arm with almost no gap gives none (**+0.00041**, t 0.06).

*The mechanism:* any covariate raising **both** arms' errors yields a differential proportional to their
gap, because the more accurate arm has more advantage to lose. *The remedy:* an accuracy-matched
comparator, or an Oldham-type purge that is **positive-controlled** — ours retains **117%** of a planted
one-armed effect at t 5.48 and detects g = 0.02 at t 2.99.

**8 · A permutation null answers *did the pairing matter*, never *why*.** A within-prompt permutation of
whole score profiles returns **p_perm 0.0000 on synthetic data containing no values at all**, and a
generator whose only input is "probability the rater ranks randomly" was reported to reproduce **77%**
of the effect it was supposed to protect. ⚠ **That generator is not in the package** — the figure is an
independent navigator's report, not an artifact, and by this programme's own rule ("every round persists
its vectors") it should not have been written as "demonstrated".

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
| instances where the **falsifying or resolving material was already in hand** (the ledger's own ordinal counter, now at 13 with wall #1) | **13** |
| field-level novelty claims that died | **UNVERIFIED at "6 of 6"** — asserted in a navigator quote, never enumerated; the sibling README says *five* |
| times a permutation null was placed in the load-bearing gate position | **3** |
| total retractions | **UNRESOLVED — see the note at the top; no defensible count exists yet** |

Not one was caught by pre-registration, positive controls, or three-valued verdicts. Every one was
caught by reading a primary source, by re-reading the programme's own prior output, or by an independent
navigator **building the world the diagnostics could only price** — and dispatched adversaries did catch
several (entries 2 and 4 open with an adversary's kills), but by *reading a source*, never by the
apparatus. The
apparatus disciplines what happens *after* committing to a design; the failures happened at
**assertion** and at **direction-choice**, upstream of anywhere it applies.

---

## What this document does NOT claim

- Any **unverified** sentence of the form *"nobody has measured X"* or *"X requires a different
  dataset."* The two remaining walls are verified against the object; the third was not, and it was
  false.
- *"Compilation returns least to the raters whose own stated values sit furthest from the consensus"* —
  **retracted**, and not revivable through the per-arm levels.
- *"Compilation decouples error from cases **and couples it to people**"* — the second verb is wrong.
  **Winners and smaller winners, not winners and losers.**
- *"Particular raters are systematically worse served"* — killed twice. α is re-centred within arm and
  cannot carry an absolute claim.
- That the polarity story is either confirmed or refuted. x2 alone is **+0.03110** (se **0.01801**,
  t 1.73) on one population; purged it is **+0.01702** (se 0.01984, t 0.86). A larger figure of
  +0.03644 (t 2.79) on the other population exists only as ledger prose, in **no artifact**.
  **UNVERIFIED in both directions**; re-promoting it would be the mirror of the error.
- That any finding transfers to Community Notes via `raterParams` "with no new data collection."
- That the methods result (**7**) is **novel**. A bounded search of Crossref and DBLP over ~18 queries
  did not find it; the nearest neighbours are the Oldham/change-score-versus-baseline literature and
  Cleary-model differential validity, neither of which is the two-rules-difference confound. **"Not
  found in a bounded search"** is the ceiling. Six of six novelty claims here have died.
- ⛔ **RETRACTED.** This document claimed four objects were counted and all four had max count per
  (rater, item) = 1. **CoVal's max is 5.** PRISM's is 1 and I verified it (0 of 8,011 conversations with
  more than one rater). **DICES-350 and DICES-990 were never counted here** — no DICES data is on disk
  and the release names appear in no artifact. Status: PRISM ✓, CoVal ✗ **false**, DICES **UNVERIFIED**.
- That the anonymity result (**5**) generalises beyond this release. It is a statement about the only
  release carrying both the compilation contrast and the demographics.

---

## Why nothing else opens

| site | status | verified |
|---|---|---|
| **DICES** | already published on this estimand | GRASP, [arXiv 2311.05074](https://arxiv.org/abs/2311.05074), NAACL 2024 — in-group/cross-group cohesion on race, gender, age and intersections. ⚠ Reported by a navigator; **the arXiv id and venue are UNVERIFIED here** (no network was used). The claim that it has no within-cell replication is likewise **UNVERIFIED** — no DICES data is on disk |
| **PRISM** | cannot form the estimand | 0 of 8,011 conversations have more than one distinct `user_id`; items are participant-private, so rater and item effects are not separable |
| **Community Notes** | one aggregation rule | there is no paired contrast `d` to regress; construct one and it differs in accuracy, reproducing the artifact in **7** |

---

## What is now open, and who decides it

**The closure rested on three walls; one is false.** A test–retest reliability of **0.845 at n = 111**
is a real instrument on a small population, and the reliability half of wall #1 is gone. Whether that
**reopens the programme is a direction question**, and direction in this programme deliberately does not
live with the executor — it is recorded here, not decided. What can be said without deciding it: the
anonymity result (**5**) and the methods result (**7**) are untouched by wall #1's fall, and the
per-arm-levels refusal in the ledger's entry 24 still stands but on a **narrower** argument than was
published — that x1 and the ranking share a common cause, not that no instrument exists.

---

**The package** (reachable and current at the time of writing: HTTP 200, and local `HEAD` ==
`origin/main` == `4b77e3bb`): [CoValCrossroad](https://github.com/ivanicu/CoValCrossroad) — 114 rounds in 12
campaigns, every round's question, finding and caveats in its README, and every retraction annotated in
place rather than deleted. **The diary:** [`LEDGER.md`](LEDGER.md), 26 entries, one per belief update.
**The machines:** three mechanical gates in [`assurance/`](assurance), each attacked before being
trusted, each shipping with the statement of what it cannot do.
