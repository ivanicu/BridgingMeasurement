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

## WHAT NOBODY HAS ASKED — ⛔ RETRACTED 2026-07-29, SAME DAY, BY THE ADVERSARY THIS LEDGER DISPATCHED

**The original paragraph is below, struck. It claimed (a) the helpfulness score has never been  **[UNVERIFIED — bounded search, not a positive control.]**
validated as a measurement — "this instrument has never had a positive control" — and (b) nobody has
tested whether one latent dimension is enough. Both are wrong, and the ledger's own text predicted
how.**

### The five kills

| # | pointer | what it does | what it kills |
|---|---|---|---|
| 1 | **`twitter/communitynotes` → `documentation/under-the-hood/ranking-notes.md`** (primary source, raw fetch) | Verbatim: *"for now, to avoid overfitting on our very small dataset, we only use 1-dimensional factors. We expect to increase this dimensionality as our dataset size grows significantly"* — and *"We can represent multidimensional viewpoint spaces by increasing the dimensionality of the factors, without changing the algorithm itself."* | **Rank 1 is not an unexamined default.** It is a stated, reasoned, revisitable engineering tradeoff, and the codebase already generalises to rank-k. Claim (b)'s framing is dead |
| 2 | **[2506.15168](https://arxiv.org/abs/2506.15168)** — full PDF, not the abstract | Builds an **independent multidimensional ground-truth ideology space** (Left–Right + Anti-Elite, from MP-follower networks calibrated against the Global Party Survey) and tests whether CN's single fitted axis reduces to it. **AUC 0.808 for the 1-D axis against the 2-D plane across 13 countries; the true second dimension lifts it only to 0.813.** Finds the axis *"cannot always be reduced to"* Left–Right, with anti-elite alignment in Japan and Brazil | **The dimensionality-sufficiency question is answered on real data, by a stronger design than ours** (external ground truth, not an internal refit). It also **names the mechanism** this ledger's closing paragraph said "nobody has named" |
| 3 | **`documentation/under-the-hood/guardrails.md`** (primary source) | X runs a **continuous three-part external validation programme**: professional reviewers rate whether Helpful-status notes are *accurate*; randomised survey experiments measure whether a note shifts understanding in the correct direction; surveys of random non-contributor users measure helpfulness | **Claim (a) is directly contradicted.** This is concurrent-validity checking of the score, publicly documented and ongoing |
| 4 | **[2210.15723](https://arxiv.org/abs/2210.15723)** — the founding paper, full PDF | Three waves of **randomised survey experiments (Wave 2, N=7,387)**, out-of-sample non-contributor respondents, measuring whether a selected note shifts agreement with the tweet's claim, broken down by party ID | **The sharpest kill.** A positive-control-style validation of the helpfulness construct, published 2022 — **inside the exact row this ledger flagged "must read in full" and did not read** |
| 5 | **[2604.11224](https://arxiv.org/abs/2604.11224)** | Semi-synthetic coordinated attacks injected into **45M real ratings / 365K real notes**; measures displacement of quality estimates against baseline | Partly anticipates **Test 3's mechanism** — known signal injected into the real record, recovery checked — though its "known" reference is the model's own undisturbed output, not an independent quality label. Robustness, not construct validity |

### The failure, named, because it is worse than being wrong

**I asked documents about the system instead of asking the system.** X's algorithm documentation and
its full scoring source are public. I ran five arXiv queries — *papers about Community Notes* — and
never fetched the thing itself. **The adversary's first move was to read the primary source, and it
found the answer to claim (b) in one file.**

That is constitutional door ④, verbatim: *when I want to know what a system can do, I ask the system
— the registry, the source. Never a document about it.* This ledger cited 34 documents about the
system and zero lines of the system.

**And the second failure is worse than the first.** The scope note at the top of this file says every
row is read from an abstract, and row A says of the founding paper *"must read in full: it is the
only place the estimand is defined."* **I then asserted a field-wide negative — "not one asks what
helpfulness is an estimate of" — without opening it.** The reason the claim had to fail was written
into this document, above the claim, by me. *A confession is never audited.*

### ~~The original claim~~ (struck, kept per annotate-never-rewrite)

> ~~The entire field measures the OUTPUT of the score and never validates the score AS A MEASUREMENT.
> Not one asks what `helpfulness` is an estimate of. This instrument has never had a positive control.
> And underneath sits an untested assumption: the latent viewpoint space is fitted as ONE dimension.~~

---

## WHAT ACTUALLY SURVIVES

**Three residuals the adversary could not kill, stated grudgingly in its own words, plus one question
it found that this ledger never contained.**

### S1 · The decision has never been tested, only the axis — and these are different questions  **[UNVERIFIED — bounded search, not a positive control.]**

**[UNVERIFIED — bounded search, not a positive control.]** Adversary verdict on the general form: **DEAD** — see LEDGER entry 8.

2506.15168 answers: *does CN's fitted axis recover a known ideology space?* **Roughly yes — AUC
0.808, and a true second dimension buys 0.005.**

It does **not** answer: *does fitting a second factor change which notes get shown?*

**These do not follow from one another, and the gap is mechanical.** Status is a threshold on the
**intercept**, computed after the factors absorb what they can. Adding a factor changes *what is
absorbed into the factors versus left in the intercept* — so a 0.005 AUC gain in **axis recovery** is
fully compatible with a large number of **status flips**. The mapping from "the axis is nearly
sufficient for describing ideology" to "the axis is sufficient for the decision" is **not monotone,
and nobody has computed it.**

**This is the CoVal proxy-ledger shape exactly:**

| | |
|---|---|
| **PROPERTY** | the note bridges real viewpoint divides |
| **PROXY** | positive intercept after removing **one** fitted factor |
| **IMPLICATION** | validated in the direction *"the fitted axis correlates with known ideology"* |
| **UNSOUND DIRECTION** | *"therefore the status decision is insensitive to rank"* — never tested |

**Test 2 (status counterfactual under rank) is the surviving experiment**, and the adversary marked it
**NOVEL** — no trace in arXiv, X's GitHub docs, or X's own changelog.

### S2 · Who validates the validator?

**The adversary's find, and it is not in any of the 34 rows.** Killing claim (a) does not settle the
matter, it *forks* it. X's guardrails programme is X-designed, X-run, uses partnered reviewers and
X-authored survey instruments, and publishes **no raw accuracy / informativeness / helpfulness
numbers, no pre-registration, and no outside replication.**

So *"the score has ground-truth validation"* splits into:
- **validated and independently inspectable**, versus
- **validated, but only X has ever seen the number.**

**A live, decision-relevant fork, present in none of the 34 papers and none of this ledger's rows.**

### S3 · The two half-anticipated tests, and what remains of them

- **Test 1** (internal rank-2/3 refit of the deployed matrix + variance decomposition): 2506.15168 is
  close *in spirit* but uses an externally constructed space, not a refit of the same matrix. **The
  literal design was not found — but after S1 it is no longer the interesting version.** It is now a
  *sub-step* of Test 2, not a question of its own.
- **Test 3** (externally-labelled known-quality notes planted into the real record): not found. The
  closest analogues use different "known" references. **Survives, weakened** — and only worth running
  once S2 tells us whether an external label is even available to plant.

---

## CORRECTIONS TO THE ROWS ABOVE

| row | was | correction |
|---|---|---|
| **A** 2210.15723 | `F` — "must read in full" | **The F-tag is right and was ignored.** Not a mislabel: a claimed global negative resting on a primary source this ledger itself flagged as unread |
| **C** 2506.15168 | filed under bias/manipulation, "structural cost" | **False openness.** It also runs a genuine dimensionality-sufficiency test against independent ground truth with a quantitative answer. Material already *in* this ledger bore directly on the claim the ledger called open |
| **E** 2604.11224 | `⛔ kills our item 2` | **Possibly wrong, and in our favour — which is why it needs checking.** QSMF's per-rater scalar is estimated from the ratings matrix alone, explicitly as peer prediction "without external ground truth", so it may not read note text either. **Item 2 is UNVERIFIED, not closed.** D6 from the abstract; re-check the full method before re-opening or re-closing |

---

## ⛔ THE FRAMING IS RETRACTED — 2026-07-29, second adversary, same day

**"The field measures these as content-moderation products, not as collective-alignment
procedures" is indefensible as stated.** An entire strand treats the aggregation step itself as the
object of study, in venues the arXiv-only sweep could not see.

| pointer | venue | what it does | what it kills |
|---|---|---|---|
| **10.1145/3491102.3502004** — Jury Learning | **CHI 2022** | *"Supervised ML today resolves label disagreements implicitly using majority vote, which overrides minority groups' labels"* — and builds an architecture that keeps minority positions addressable | **Discarded disagreement, outright** |
| **10.52202/075280-2321** — DICES | **NeurIPS 2023** | encodes rater votes as **distributions across demographics** *"to allow for in-depth explorations of different aggregation strategies"* | **Kills it for one of the very exemplars this project named as a target** |
| **10.18653/v1/2024.emnlp-main.1029** — D3CODE | **EMNLP 2024** | 4.5K sentences, 4K+ annotators, 21 countries, annotators' **moral values measured directly** on six moral foundations | **Kills "the normative judgment has never been measured"** — measured from the crowd, no expert institution required |
| **10.1145/3442188.3445901** — Jacobs & Wallach, *Measurement and Fairness* | **FAccT 2021** | imports measurement-theoretic **construct validity** into computational systems: harms arise from mismatch between an unobservable normative construct and its operationalised proxy | **This is the apparatus our claim reinvented under a new name** |
| **10.52202/079017-2557 / 10.1609/aaai.v39i27.35116** — *Axioms for AI Alignment from Human Feedback* | **NeurIPS 2024 / AAAI 2025** | frames RLHF reward learning as social-choice aggregation; proves Bradley–Terry–Luce **fails basic axioms**; builds new rules | **Kills the framing; substantially weakens decision contingency** |
| **10.1145/3774904.3792987** — *Consensus Stability of Community Notes* | **WWW 2026** | 437K notes / 35M ratings: **30.2% of displayed Helpful notes later lose status** | Partial — temporal instability, not counterfactual-rule |
| **10.18653/v1/2022.naacl-main.431** — *Annotators with Attitudes* | **NAACL 2022** | annotator identity and beliefs bias toxicity labels | Partial on individual stability — **between**-person, not within |

### The corrected claim, which is narrower and much harder to kill

**The apparatus exists and the deployed-system empirics exist. Nobody has connected them.** **[UNVERIFIED — bounded search, not a positive control.]**
Measurement theory says to check construct-vs-proxy mismatch (FAccT 2021); social choice says the
aggregation rule determines the outcome and standard rules fail axioms (NeurIPS 2024); and a separate
literature measures what Community Notes does. **No one has run the first two against the third's
decision record.** That is an application gap, not a question gap — and it is the only version of this
claim that survived contact.

### What survived, in the adversary's own grudging words

| question | verdict |
|---|---|
| **Individual stability** — within-person test–retest of the *same* person's judgment, applied to AI value elicitation | **GENUINELY ABSENT (weakly).** The adjacent literatures exist — preference-construction in survey methodology, between-annotator identity effects in NLP — but no bridge paper. **The one leg that holds** |
| **Referent circularity** — does a specific crowd system's validation chain terminate in professional experts | **PARTLY — unconfirmed rather than killed.** General platform-self-regulation critique exists; no paper traces one system's chain |
| **Decision contingency**, in its *empirical* form on a deployed system: *N% of decisions flip under a defensible alternative rule nobody argued for* | **PARTLY.** The social-choice work is axiomatic; the Community Notes work is temporal. **Nobody has run the counterfactual rule on the live record** |  **[UNVERIFIED — bounded search, not a positive control.]**

---

## SEARCH ROUTES — TESTED, NOT ASSUMED

**This is the most reusable output of two adversary runs**, and the tool is `priorart/litsearch.py`.

| route | status | working pattern |
|---|---|---|
| **Crossref** | ✅ **the workhorse.** No key. Returns DOI + **venue** + year for ACM / AAAI / ACL / NeurIPS proceedings — the field arXiv cannot give you | `api.crossref.org/works?query.bibliographic=<enc>&rows=N&select=title,DOI,issued,container-title` |
| **DBLP** | ✅ for author and topic-**name** queries. Indexes titles **literally** — a stacked multi-word phrase returns 0, and that 0 means *no literal match*, never *nothing exists* | `dblp.org/search/publ/api?q=<enc>&format=json&h=N` |
| **arXiv** | ✅ but `ti:"..."` is **brittle** — it fails silently on a paraphrased title. Use it to fetch an abstract for a title Crossref already gave exactly, never to discover | `export.arxiv.org/api/query?search_query=ti:%22<title>%22` |
| DuckDuckGo | ⛔ anti-bot block page on `html.` and `lite.`, every query | — |
| Semantic Scholar | ⛔ HTTP 429 without a key | — |
| OpenAlex | ⛔ now paid: *"Insufficient budget"* | — |

**The pattern: Crossref to DISCOVER → arXiv `ti:` for the ABSTRACT → the DOI otherwise.**
⚠ Crossref's bibliographic search needs a **specific** query — *"Measurement and Fairness"* returns
educational-assessment noise, while the full title returns the paper first. **A generic query
returning noise is not evidence of absence.**

---

## VENUE COVERAGE — STILL UNRESOLVED, AND NOW TWICE CONFESSED

The adversary could not close the gap either. **DuckDuckGo returned an anti-bot block page on both
`html.duckduckgo.com` and `lite.duckduckgo.com`** for every query attempted, confirmed by inspecting
the raw HTML. Semantic Scholar 429s without a key; OpenAlex is paid. **CHI, CSCW, ICWSM, WWW, PNAS and
the Nature/Science family remain systematically absent from a field that publishes there heavily.**

**Any novelty claim in this document is therefore UNVERIFIED, never ESTABLISHED** — including S1 and
S2. That distinction is the whole point of the three-valued verdict, and this is exactly the case it
exists for.

## STOP CONDITION — NOT YET MET

The phase ends when **a fresh adversarial reader, given only this ledger, can say which of our planned
experiments is already published and which is not.** That reader has not run. **Until it does, the
three tests above are candidates, not a queue** — and the venue gap (no CSCW/CHI/ICWSM/PNAS coverage)
is the most likely place a "nobody has asked" claim dies.
