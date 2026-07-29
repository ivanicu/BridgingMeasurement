# PRIOR-ART LEDGER — Community Notes / bridging-based ranking

**Retrieved 2026-07-29 (UTC).** Source: arXiv API, five queries — `"community notes"`, `"birdwatch"`,
`"bridging-based ranking" OR "bridging algorithm"`, `"crowdsourced fact-checking"`,
`"crowd fact-check" OR "community fact-checking"`. 102 unique entries; ~65 on-topic; **34 read**.
Raw sweep persisted at `priorart/arxiv_sweep_2026-07-29.json`.

> ## SCOPE OF THIS LEDGER, STATED FIRST
> **Every row below is read from an ABSTRACT, not a full text.** So each row is D6 for *"this paper
> claims X"* and **D3 at best for what it actually established** — an abstract states a result, it
> does not expose the design that would let anyone judge it. **No row here may be used as a floor to
> clear or a null to cite until the full text is read.** Two other sources are unqueried: Semantic
> Scholar returned HTTP 429 and OpenAlex now requires payment, so **non-arXiv venues (CSCW, CHI,
> ICWSM, Nature/Science family, PNAS) are systematically under-represented** — and this field
> publishes heavily there. This ledger is a first pass, and its own biggest gap is venue coverage.

---

## The finding that changes the plan

**The field is far more crowded than CoVal, and three of the five queue items are already occupied.**

| our planned item | status after this sweep | evidence |
|---|---|---|
| **1** reproduce the algorithm | **routine** — several groups already reimplement or modify it | 2511.02615 simulates it; 2604.11224 rebuilds and extends it |
| **2** does the score read note TEXT? *(our r109 transplant, the seed hypothesis)* | **⛔ ALREADY THE PREMISE OF A PAPER** — not a finding | 2604.11224's entire motivation is that the current factorization separates ideology from quality **without reading content**, and proposes making it quality-sensitive |
| **3** is bridging real or a factorization artifact? | **heavily worked from three directions** | 2506.15168 (undermoderates polarizing content **by design**), 2601.22201 (limited by overt political signalling), 2511.02615 + 2607.01824 (manipulable) |
| **4** layer separation, TIME as a layer | **partly occupied** | 2601.14002 (how evaluations change **after** display), 2602.08970 (hyperactive minority alters stability) |
| **5** S_pre / H_fresh / τ_c | **the only clearly open one**, and τ_c is done **in simulation** only | 2511.02615 and 2604.11224 intervene on simulated raters, not on the deployed record |

**Consequence for the queue: item 2 must be deleted, not demoted.** Running it would reproduce a
published paper's *motivation* as if it were our result — the exact failure this phase exists to
prevent.

---

## The ledger

Grouped by what each line of work settles. **F** = a floor we must clear. **Q** = a question we must
not re-ask. **O** = leaves something open we could take.

### A · Foundation and system description

| id | year | claim | verdict |
|---|---|---|---|
| [2210.15723](https://arxiv.org/abs/2210.15723) | 2022-10 | **The founding paper.** Matrix factorization selects annotations that appeal *broadly across heterogeneous user groups*; claims both informativeness and spread reduction | **F** — every bridging claim is measured against this. Must read in full: it is the only place the estimand is defined |
| [2104.07175](https://arxiv.org/abs/2104.07175) | 2021-04 | First descriptive study of Birdwatch: who writes, who rates, what gets flagged | **Q** — descriptive baseline, settled |
| [2510.09585](https://arxiv.org/abs/2510.09585) | 2025-10 | Four-year descriptive investigation, Birdwatch → Community Notes | **Q** — the descriptive layer is done. Read for data vintages, not for questions |
| [2509.15434](https://arxiv.org/abs/2509.15434) | 2025-09 | Framework for "Crowdsourced Context Systems" as a general class beyond X | **O** — a framework, not a measurement. Our M(N,A,R,P,T) decomposition may be finer |

### B · Does it work? (effect on spread — the most crowded cell)

| id | year | claim | verdict |
|---|---|---|---|
| [2409.08781](https://arxiv.org/abs/2409.08781) | 2024-09 | Difference-in-differences: notes **reduce** spread of misleading posts | **Q** |
| [2404.02803](https://arxiv.org/abs/2404.02803) | 2024-04 | ~285k notes, DiD: context **halves** retweets | **Q** |
| [2502.13322](https://arxiv.org/abs/2502.13322) | 2025-02 | Notes reduce engagement **and** diffusion of false information | **Q** |
| [2307.07960](https://arxiv.org/abs/2307.07960) | 2023-07 | Did the *roll-out* reduce engagement? | **Q** |
| [2205.13673](https://arxiv.org/abs/2205.13673) | 2022-05 | Diffusion of community-fact-checked misinformation | **Q** |
| [2505.10254](https://arxiv.org/abs/2505.10254) | 2025-05 | Community fact-checks do **not** break follower loyalty | **Q** |
| [2409.08829](https://arxiv.org/abs/2409.08829) | 2024-09 | Notes trigger **moral outrage** in replies | **Q** |

> **Do not enter this cell.** Six independent DiD studies, converging. Any effect-size question we
> asked would be a seventh.

### C · Bias, manipulation, and the bridging property itself

| id | year | claim | verdict |
|---|---|---|---|
| [2506.15168](https://arxiv.org/abs/2506.15168) | 2025-06 | **1.9M notes / 135M ratings.** The system **undermoderates polarizing content BY DESIGN** — bridging requires cross-partisan support, so the most polarized content is least noteable | **F, and the most important row here.** This is the strongest existing version of "the bridging property has a structural cost" |
| [2601.22201](https://arxiv.org/abs/2601.22201) | 2026-01 | Collective-intelligence benefit **limited by overt political signalling** | **F** |
| [2511.02615](https://arxiv.org/abs/2511.02615) | 2025-11 | Systematic evaluation of the algorithm on **simulated** raters; quantifies rater bias and manipulation | **F + O** — simulation validates against its own generative assumptions. **What it cannot do is validate on the deployed record** |
| [2607.01824](https://arxiv.org/abs/2607.01824) | 2026-07 | **Coordinated** manipulation of the bridging mechanism, framed across X/Meta/TikTok/Google | **F** — newest; must read |
| [2603.18053](https://arxiv.org/abs/2603.18053) | 2026-03 | **"Consensus-based auditing"**: rewarding raters for agreeing with the final aggregate. Analyses the consequences of that design | **F + O** — closest existing work to a *measurement-validity* critique. The circularity it names is the same family as our proxy-ledger |
| [2602.08970](https://arxiv.org/abs/2602.08970) | 2026-02 | A **hyperactive minority** alters note stability | **F** |
| [2510.00650](https://arxiv.org/abs/2510.00650) | 2025-10 | Threats to sustainability; who the community actually is | **F** |
| [2406.12444](https://arxiv.org/abs/2406.12444) | 2024-06 | Source credibility of the sources notes cite | **Q** |

### D · Timeliness, participation, supply/demand

| id | year | claim | verdict |
|---|---|---|---|
| [2510.12559](https://arxiv.org/abs/2510.12559) | 2025-10 | 1.8M notes: participation inequality, consensus formation, timeliness | **Q** |
| [2603.11120](https://arxiv.org/abs/2603.11120) | 2026-03 | **Effort aversion** among raters — a previously untested mechanism | **F** |
| [2602.06005](https://arxiv.org/abs/2602.06005) | 2026-02 | 1.1M fact-checks + requests: does **supply meet demand**? | **Q** |
| [2509.09956](https://arxiv.org/abs/2509.09956) | 2025-09 | 98,685 requested posts: what the Request function changes | **Q** |
| [2604.17042](https://arxiv.org/abs/2604.17042) | 2026-04 | Request **alerts** and note diversity/visibility | **Q** |
| [2512.19947](https://arxiv.org/abs/2512.19947) | 2025-12 | Participation and dependence on professional fact-checking **across languages** | **O** — the non-English layer is thin everywhere |
| [2601.14002](https://arxiv.org/abs/2601.14002) | 2026-01 | **Consensus stability**: how evaluations change *after* a note becomes visible | **F** — this is our "time layer", already opened |

### E · Algorithm modification and LLM-written notes

| id | year | claim | verdict |
|---|---|---|---|
| [2604.11224](https://arxiv.org/abs/2604.11224) | 2026-04 | **Quality-sensitive** matrix factorization for sample efficiency and manipulation resistance | **⛔ kills our item 2.** Its premise is that the deployed MF is content-blind |
| [2411.06116](https://arxiv.org/abs/2411.06116) | 2024-11 | **Supernotes** — synthesise consensus notes; 91% of eligible posts show none | **F** |
| [2506.24118](https://arxiv.org/abs/2506.24118) | 2025-06 | **X's own position paper**: LLMs write, humans rate | **F** — read for the platform's stated estimand |
| [2604.02592](https://arxiv.org/abs/2604.02592) | 2026-04 | **Field** evaluation of LLM-written notes on X | **F** |
| [2605.16566](https://arxiv.org/abs/2605.16566) | 2026-05 | Characterizing AI fact-checkers' contributions | **Q** |
| [2507.08110](https://arxiv.org/abs/2507.08110) | 2025-07 | AI feedback + engagement with counterarguments | **Q** |

### F · Comparison with professionals, and helpfulness determinants

| id | year | claim | verdict |
|---|---|---|---|
| [2502.14132](https://arxiv.org/abs/2502.14132) | 2025-02 | **Can notes replace professional fact-checkers?** | **F** |
| [2208.09214](https://arxiv.org/abs/2208.09214) | 2022-08 | Crowd vs experts | **Q** |
| [2503.10560](https://arxiv.org/abs/2503.10560) | 2025-03 | **References to unbiased sources increase helpfulness** | **F + O** — one of the few papers treating helpfulness as an *outcome to be explained*. Its determinants are content features, so it presumes content matters to *raters* even though it cannot matter to the *scorer* |
| [2510.24810](https://arxiv.org/abs/2510.24810) | 2025-10 | A dataset for exploring helpfulness of fact-checking **explanations** | **O** — a labelled resource we could use |
| [2601.14105](https://arxiv.org/abs/2601.14105) | 2026-01 | Rhetoric of persuasion, professional vs community | **Q** |
| [2305.09519](https://arxiv.org/abs/2305.09519) | 2023-05 | How the crowd **selects targets** | **Q** |

### G · Theory of bridging

| id | year | claim | verdict |
|---|---|---|---|
| [2301.09976](https://arxiv.org/abs/2301.09976) | 2023-01 | **Bridging systems**: open problems across ranking, recommenders, governance | **F** — the normative framing. Read for what *it* says is unsolved |
| [2410.12699](https://arxiv.org/abs/2410.12699) | 2024-10 | Bridging-based approach to counterspeech | **Q** |
| [2311.11282](https://arxiv.org/abs/2311.11282) | 2023-11 | Individual vs **collective** misinformation tagging, effect on information diversity | **O** |

---

## WHAT NOBODY HAS ASKED

**The entire field measures the OUTPUT of the score and never validates the score AS A MEASUREMENT.**
Thirty-four papers ask whether notes reduce spread, arrive in time, are manipulable, are partisan, or
can be written by an LLM. **Not one asks what `helpfulness` is an estimate of.** There is no ground
truth for helpfulness anywhere in the system: it is a latent intercept in a factorization, defined by
the model that produces it, and the closest thing to a validity check in the literature — 2511.02615
— is a **simulation**, which can only confirm the generative assumptions it was written with. *In our
vocabulary: this instrument has never had a positive control.*

**And underneath that sits a specific, checkable, load-bearing assumption nobody has tested: the
latent viewpoint space is fitted as ONE dimension.** Every use of the word "cross-partisan" in every
paper above inherits it. If real viewpoints are two-dimensional or more, then "bridging" is defined
only on the axis that happened to be fitted, and a note that bridges factor 1 while splitting an
unfitted factor 2 is **surfaced as consensual when it is not**. That is not a manipulation story and
not a bias story — it is a *coverage* story, and it is the exact shape of what we found in CoVal
yesterday: **a proxy that is structurally blind to part of the property it is named after.** 2506.15168's
"undermoderates polarizing content by design" may be the *shadow* of this, observed through a
one-dimensional lens; if so, it has a cause nobody has named.

**Three tests follow immediately, and none of them is in the ledger above:**
1. **Fit rank 1, 2, 3, … on the same rating matrix** and ask how much rating variance the second and
   third factors carry. If factor 2 is negligible, the deployed assumption is *earned* and that is a
   publishable defence of the system. If it is not, everything downstream of "cross-partisan" needs a
   scope statement.
2. **Status counterfactual under rank:** how many notes currently shown would *not* be shown at rank 2,
   and vice versa? That is τ_c on the deployed record rather than in simulation.
3. **A positive control for helpfulness at last**: plant notes of known relative quality (2510.24810's
   labelled explanations, or 2503.10560's source-quality signal) into the real rating record and ask
   whether the algorithm recovers the planted ordering. *An instrument that has never recovered a
   known value is not a measurement.*

---

## STOP CONDITION — NOT YET MET

The phase ends when **a fresh adversarial reader, given only this ledger, can say which of our planned
experiments is already published and which is not.** That reader has not run. **Until it does, the
three tests above are candidates, not a queue** — and the venue gap (no CSCW/CHI/ICWSM/PNAS coverage)
is the most likely place a "nobody has asked" claim dies.
