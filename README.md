# Bridging Measurement

**What is a Community Notes "helpfulness" score an estimate of?**

The field has thirty-four papers on what the score *does* — reduces spread, arrives late, can be
gamed, skews partisan — and none on whether it is a valid measurement of anything. This project asks
the second question.

---

## The object

**A bridging-ranked note score is a scoped, compiled, context-indexed normative measurement program**

```
M(N, A, R, P, T)
```

| layer | what it is | why it must be validated alone |
|---|---|---|
| **N** note content | the text of the note | the deployed factorization **never reads it** — so no number from the scorer is about it |
| **A** algorithm | matrix factorization, latent viewpoint dimension, thresholds | fitted at **rank 1**; every "cross-partisan" claim in the literature inherits that choice |
| **R** rater set | who rated, how much, when they enrolled | participation is extremely unequal; a hyperactive minority moves stability |
| **P** population | the viewpoint distribution the raters are drawn from | "bridging" is only defined relative to it |
| **T** time | when the score was computed | raters enrol and drop out, the algorithm versions, and a score computed today is not the score a note was shown under |

**Never report a number about "what the crowd thinks" that is actually a number about one layer.**

---

## Status

| | |
|---|---|
| **Phase** | 0 — prior-art world model. **No experiment may start until its stop condition is met.** |
| **Prior art** | [`PRIOR_ART.md`](PRIOR_ART.md) — 102 arXiv entries, ~65 on-topic, 34 read |
| **Ledger** | [`LEDGER.md`](LEDGER.md) — the belief-update diary, entry 1 |
| **Stop condition** | an adversarial reader, given only the ledger, can say which planned experiment is already published. **Running. Not met.** |
| **Data** | none downloaded yet — deliberately. Phase 0 forbids it |

---

## What Phase 0 already cost us, which is the point

**Our seed hypothesis is dead.** Item 2 — *does the score read the note's text?* — was transplanted
from the CoVal work, where the same question found a scope error in that package's most-quoted number.
It is **already the premise of [2604.11224](https://arxiv.org/abs/2604.11224)**. Running it would have
reproduced a published paper's motivation as our result.

**Three of five queue items are occupied.** Details and the row-by-row classification are in the prior
art ledger.

---

## The two candidate questions that survived

Both are **candidates, not a queue**, until the adversary returns.

**1 · The instrument has never had a positive control.** `helpfulness` is a latent intercept in a
factorization — defined by the model that produces it, with no ground truth anywhere in the system.
The closest thing to a validity check in the literature is a *simulation*, which can only confirm the
generative assumptions it was written with.

**2 · The latent viewpoint space is fitted as ONE dimension.** If real viewpoints are 2+ dimensional,
"bridging" is defined only on the fitted axis, and a note that bridges factor 1 while splitting an
unfitted factor 2 is surfaced as consensual when it is not. **A coverage story, not a bias story** —
the same shape as the CoVal finding that a proxy can be structurally blind to part of the property it
is named after.

---

## Discipline

Carried over intact from the CoVal work, where every one of these was earned by a defect.

| rule | why |
|---|---|
| **Claim card before code** | Claim → Estimand → Is the target observed? → Alternative worlds → Intervention → Null |
| **Positive control before any null** | a zero from an instrument that has never returned non-zero is silence, not an acquittal |
| **…and a complementary control** | so a null cannot pass for the wrong reason — if both halves of a partition read chance, the partition separates nothing |
| **Mutations must be asserted to have landed** | three "attacks" in the CoVal work mutated something no code reads |
| **Three-valued verdicts** | CONFIRMED · OVERTURNED · **UNVERIFIED**. UNVERIFIED never becomes OVERTURNED; a false acquittal is permanent |
| **Significance ≠ equivalence** | reported separately, margin pre-registered. A small point estimate with a wide interval is an **ANSWERABLE MARGIN** and gets that name |
| **Conclusion strings are never hand-written** | a script's own conclusion string will say what you wanted to hear |
| **Smoke runs never reach the README** | they go to `results/_smoke/` and are labelled |
| **Every round persists its vectors** | so a later round can attack it — four CoVal rounds existed only because an earlier one saved its records |
| **Every number carries its scope** | population · instrument · baseline · regime. Eleven of twelve CoVal retractions were a correct number reported without the scope over which it held |
| **Reproducibility is a gate, not a virtue** | every round runs twice under different `PYTHONHASHSEED`, byte-identical. **Every seed being set is not the same as being seeded** — two CoVal rounds proved it. Sort any set before it can decide an order a seeded draw consumes |

**Diary discipline — one action, one commit; the git log is the narrative that cannot be compacted
away.** Format and the entry contract are in [`LEDGER.md`](LEDGER.md).

---

## Frozen

- **The "does it work" cell.** Six independent difference-in-differences studies converge on spread
  reduction. A seventh is not a contribution.
- **Item 2** (does the score read note text) — deleted, not demoted. See above.
- **Any experiment before the Phase 0 stop condition is met.**
