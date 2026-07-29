# LEDGER — the belief-update diary

**This is the same instrument the CoVal work ran on, under a truer name.** There it was called
`RETRACTIONS.md` because it began as a retraction log and never got renamed; 224 entries later it was
recording every kind of belief update, not only the ones that took something back. Here it starts
correctly.

## What an entry is

**One entry per belief update — not per action, not per round.** A round that runs and changes
nothing gets no entry; a five-line observation that kills a claim gets one. The unit of progress is
the model update.

Every entry carries, in whatever form fits:

- **Observed** — what actually happened, with the number
- **Killed** — which worlds or claims are now dead
- **Survived** — which are still live
- **Downgraded** — which need lower confidence or narrower scope
- **Ontology shift** — what changed in the *definition* of the object, mechanism, or decision
- **NEXT** — the largest remaining gap, stated so specifically that the next session can start on it
  without re-deriving anything

**The NEXT line is the load-bearing part.** It is the only thing that survives a context wipe intact,
and the queue is driven to zero from it.

## The other half: git log is the diary

**One action, one commit.** The commit *subject* is the belief update in one sentence — the WHY, never
the diff's WHAT. The *body* is the diary entry proper, written for the amnesiac next reader who will
remember nothing.

```
git reset -q                      # HARD STEP — the index may hold a previous action's files
git add <only this action's files>
git commit --no-verify -F <msg>
git reset -q
```

**Check:** `git show --stat HEAD` file count == the files this one action touched. Not equal → a bag
commit was dumped, and the diary entry now describes several things at once, which is the same as
describing none.

**Subject format:** `[type.region.impact.Dx{valence}] why`
`type` ∈ sense · think · act · fix · guard · memory · prune · reflex · predict · verify
`impact` ∈ μ (1 file) · λ (1 module) · ρ (cross-module) · σ (architecture) · Ω (paradigm)
`Dx` = the D-level of the claim the commit makes · valence ∈ `+ - ~ !`

**Every commit body ends with a NEXT**, matching the ledger entry's. The two are redundant on
purpose: the ledger is browsable, the git log cannot be compacted away.

---

## Entry 1 — the site changed, and Phase 0 immediately deleted our seed hypothesis

**Observed.** CoVal is in wind-down: all three of its terminal counterfactuals need human data we
cannot collect, so its ceiling is hard. The machinery built there — claim cards, proxy ledgers,
two-sided controls, mutation tests, null recovery, joint resampling — is the asset, and it now points
at Community Notes: 2–3 orders larger, **deployed**, algorithm **public and recomputable**, data
refreshing daily, and the cross-viewpoint structure we spent six CoVal rounds *constructing* is
**native** to it.

Phase 0 ran before any code, on the standing instruction to build the world model of what everyone
has already done and progress on top of it. arXiv API, five queries, **102 unique entries, ~65
on-topic, 34 read**. Ledger at `PRIOR_ART.md`.

**Killed — and this is the whole point of the phase.** Queue item 2, *"does the helpfulness score read
the note's text?"*, was **my seed hypothesis**, transplanted from CoVal's r109 where the same question
found a scope error in the most-quoted number in that package. It is **already the premise of a
published paper**: [2604.11224](https://arxiv.org/abs/2604.11224) exists *because* the deployed
factorization separates ideology from quality without reading content, and proposes making it
quality-sensitive. **Running it would have reproduced a published paper's motivation as our result.**

**Also killed:** the "does it work" cell. Six independent difference-in-differences studies converge
on spread reduction. A seventh is not a contribution.

**Downgraded.** Items 3 and 4 from "our questions" to "occupied, enter only with a new angle" —
bridging-as-artifact is worked from three directions, and the time layer is opened by
[2601.14002](https://arxiv.org/abs/2601.14002).

**Survived.** Item 5 — S_pre, H_fresh, τ_c — is the only clearly open one, and τ_c has been done
**only in simulation**, which validates against its own generative assumptions and not against the
deployed record.

**Ontology shift, and it is the reason this pivot may be worth more than the last three months.** The
field measures the **output** of the helpfulness score — spread, timeliness, manipulability,
partisanship — and **never validates the score as a measurement**. There is no ground truth for
helpfulness anywhere in the system: it is a latent intercept defined by the model that produces it.
*This instrument has never had a positive control.*

Underneath sits one checkable, load-bearing assumption: **the latent viewpoint space is fitted as ONE
dimension**, and every use of "cross-partisan" in every paper above inherits it. If viewpoints are 2+
dimensional, bridging is defined only on the fitted axis, and a note that bridges factor 1 while
splitting an unfitted factor 2 is **surfaced as consensual when it is not**. Not a bias story, not a
manipulation story — a **coverage** story, the same shape as CoVal's r109: *a proxy structurally blind
to part of the property it is named after.*

**Confidence, stated because the ledger is only as good as its own scope.** Every row is read from an
**abstract** — D6 for what a paper *claims*, **D3** for what it *established*. And the sweep hit only
arXiv: Semantic Scholar returned 429, OpenAlex now requires payment, so **CSCW, CHI, ICWSM, WWW, PNAS
and the Nature/Science family are systematically absent** from a field that publishes there heavily.
**The novelty claim above is therefore unverified, not established.**

**NEXT.** The stop condition is *not* met and no experiment may start until it is: a fresh adversarial
reader, given only the ledger, must be able to say which of our planned experiments is already
published. One is running now with a single mandate — **find the paper that already did it**, in the
venues this sweep could not reach, and check whether X's own algorithm documentation states why rank 1
was chosen or whether higher rank was ever tried. **Until it returns, the three proposed tests (rank-k
sweep · status counterfactual under rank · planted-quality positive control) are candidates, not a
queue.**

---

## Entry 2 — the adversary killed the novelty claim in 8 minutes, and the fatal move was reading the system instead of papers about it

**Observed.** The reader dispatched at the end of entry 1 returned five kills. **Two of them are
primary sources I never opened, and one of them is a document this ledger itself flagged as
"must read in full" before asserting a field-wide negative on top of it.**

| # | what it found |
|---|---|
| 1 | **X's own `ranking-notes.md`**: *"for now, to avoid overfitting on our very small dataset, we only use 1-dimensional factors. We expect to increase this dimensionality as our dataset size grows"* — plus *"We can represent multidimensional viewpoint spaces by increasing the dimensionality of the factors, without changing the algorithm itself."* Rank 1 is a **stated, reasoned, revisitable tradeoff**, and the code already generalises to rank-k |
| 2 | **2506.15168 in full**: builds an independent 2-D ground-truth ideology space from MP-follower networks calibrated to the Global Party Survey, and tests whether CN's single axis reduces to it. **AUC 0.808; a true second dimension buys 0.005.** It also names the mechanism this ledger said nobody had named |
| 3 | **X's `guardrails.md`**: a continuous three-part external validation programme — professional reviewers on accuracy, randomised survey experiments on informativeness, non-contributor surveys on helpfulness |
| 4 | **The founding paper in full**: three waves of randomised survey experiments, **N=7,387** in wave 2, out-of-sample non-contributors, measuring whether a selected note shifts agreement with the claim, split by party ID |
| 5 | **2604.11224**: semi-synthetic attacks injected into **45M real ratings / 365K real notes** — partly anticipating our Test 3's mechanism |

**Killed.** Both headline claims. *"This instrument has never had a positive control"* is contradicted
by kills 3 and 4. *"Nobody has tested whether one dimension is enough"* is contradicted by kills 1
and 2.

**Ontology shift — the failure, not the finding.** **I asked documents about the system instead of
asking the system.** X's algorithm documentation and its full scoring source are public. I ran five
arXiv queries — *papers about Community Notes* — and never fetched the thing itself. The adversary's
**first move** was the primary source, and it found the answer to claim (b) in one file.

That is constitutional door ④ verbatim: *when I want to know what a system can do, I ask the system —
the registry, the source. Never a document about it.* **This ledger cited 34 documents about the
system and zero lines of the system.**

**And the second failure is worse.** The scope note at the top of `PRIOR_ART.md` says every row is
read from an abstract; row A says of the founding paper *"must read in full: it is the only place the
estimand is defined."* **I then asserted "not one asks what helpfulness is an estimate of" without
opening it.** *The reason the claim had to fail was written into the document, above the claim, by
me.* A confession is never audited.

**Survived — and one is sharper than what it replaced.**

**S1 · The AXIS has been tested; the DECISION has not, and they are different questions.** 2506.15168
answers *does the fitted axis recover a known ideology space?* — roughly yes, and a second dimension
buys 0.005 AUC. It does **not** answer *does fitting a second factor change which notes get shown?*
**The gap is mechanical**: status is a threshold on the **intercept**, computed after the factors
absorb what they can, so adding a factor changes *what lands in the factors versus the intercept*. A
0.005 gain in **axis recovery** is fully compatible with many **status flips**. The map from
"sufficient for describing ideology" to "sufficient for the decision" is **not monotone, and nobody
has computed it.** The adversary marked the status-counterfactual test **NOVEL** — no trace in arXiv,
X's GitHub docs, or X's changelog. **This is the CoVal proxy-ledger shape exactly**: a proxy validated
in one direction being used to license a claim in the other.

**S2 · Who validates the validator?** *The adversary's own find, in none of the 34 rows.* Killing
claim (a) **forks** it rather than settling it: X's guardrails programme is X-designed, X-run, uses
partnered reviewers and X-authored instruments, and publishes **no raw numbers, no pre-registration,
no outside replication.** So *"the score has ground-truth validation"* splits into **validated and
independently inspectable** versus **validated, but only X has ever seen the number.**

**Downgraded.** Test 1 (internal rank sweep) is no longer a question of its own — it is a *sub-step*
of S1. Test 3 survives weakened, and is only worth running once S2 says whether an external label
exists to plant. **And row E's ⛔ on our item 2 is itself now UNVERIFIED, possibly in our favour**:
QSMF's per-rater scalar is estimated from the ratings matrix alone, so it may not read note text
either. **Never re-open item 2 on that basis without reading the full method.**

**Still unresolved, now confessed twice.** The adversary could not close the venue gap either —
DuckDuckGo served an anti-bot block page on every query, Semantic Scholar 429s, OpenAlex is paid.
**CHI, CSCW, ICWSM, WWW, PNAS and Nature/Science remain absent.** Every novelty claim here, S1 and S2
included, is **UNVERIFIED, never ESTABLISHED.**

**NEXT.** Before any experiment, and in this order:
1. **Clone `twitter/communitynotes` and read the scorer.** Not the docs about it — the source. Confirm
   from the code that rank is a parameter, find where the intercept threshold is applied, and
   establish whether a rank-k refit is a config change or a rewrite. **This should have been step
   one of Phase 0.**
2. **Read 2506.15168 in full myself**, not through the adversary's summary — it is now the single
   most load-bearing paper in the ledger and I have it at second hand.
3. **Then, and only then**, write the claim card for S1: the estimand is *the count of notes whose
   DISPLAY STATUS flips under a rank-2 refit of the same rating matrix* — a status counterfactual on
   the deployed record, which is τ_c and which CoVal could never run.

---

## Entry 3 — the complement has a shape, and the shape is that no referent for it exists

**[D5 · UNVERIFIED]** — derived from a sweep that covers only arXiv. An adversary is out with one
mandate: kill it. **Nothing here may be built on until that returns.**

**Observed — the question asked of the field, not of a dataset.** Take everything that has been done
on these systems, take the complement, and ask what the complement's members have *in common*.

**The done-set's common feature.** Every study measures the system's output against a referent that
**already exists in the world and is not normative**:

| question studied | referent | exists? |
|---|---|---|
| does a note reduce spread | retweets, impressions | countable |
| does it arrive in time | timestamps | a clock |
| is it partisan | party ID, follower networks | codable |
| can it be gamed | attack succeeds or not | binary |
| does the fitted axis recover ideology | external expert-calibrated space | 2506.15168 |

**That is not a coincidence, it is a selection effect.** A field fills the cells that have a ready
referent, because those are the papers that can be written.

**The complement's common feature — the finding.**

> **Every absent question needs a NORMATIVE referent — what was right, whose view should have counted,
> what "helpful" means — and no such fact exists in any of these datasets.**

**And it closes into a circle that can be pointed at.** X's only genuinely normative referent is in
`guardrails.md`: **professional reviewers rating whether Helpful-status notes are accurate.** So *the
system built to replace professional fact-checking has professional fact-checking as its only validity
referent* — and that referent's raw numbers are unpublished, unpre-registered, and never externally
replicated. **This does not weaken the claim; it is its strongest instance.**

**The split that keeps it honest.** Half the complement is *unmeasurable in principle*:

- "what is genuinely helpful, independent of people" — **there is no such fact.** A philosophy
  problem, not a research gap, and this project must not pretend otherwise.

The other half is measurable and nobody built the instrument: **decision contingency · discarded
disagreement · individual stability · referent circularity.**

**Ontology shift, and it relocates S1.** The status counterfactual is the entry point **precisely
because it needs no normative referent**. How many notes flip under a rank-2 refit does not require us
to say which decision was right — it says the decision is **contingent**. The field avoided this
space because it looked like it required a referent to enter. **It does not: you can establish
contingency first and argue about correctness afterwards.**

**The intersection with collective alignment.** The real question is not "does the crowd catch
misinformation" but: *can a procedure absorb many people's normative input and produce a
machine-executable judgment that **legitimately** **stands in for** **them**?* Three words carry it,
and each measurable piece of the complement lands on one:

| measurable piece | word | why |
|---|---|---|
| decision contingency under rule choice | **legitimately** | if the answer turns on a free parameter nobody justified (rank=1, threshold=0.28), the procedure's authority is borrowed from an arbitrary choice |
| discarded disagreement | **them** | an aggregate that erases a coherent minority stands in for *some* of them |
| individual stability | **stands in for** | if the input is not stable in the person there is nothing to stand in for — the procedure **constructs** rather than measures |
| referent circularity | **legitimately** | if validation terminates in experts, the crowd system's legitimacy is downstream of the institution it replaces |

**These are the four questions CoVal was asking in a different vocabulary.** Two unrelated sites, two
datasets, two algorithms, converging on one set of four — **evidence that they are structural
properties of collective-alignment procedures rather than quirks of one corpus.**

**The sharpest consequence, and the one most likely to be wrong.**

> **Most of the field is not in the intersection at all.** Spread, timeliness, coverage, manipulation
> resistance — every one asks whether the system *works as a content-moderation product*, not whether
> it *legitimately represents people*. **The field measures Community Notes as a moderation tool, not
> as a collective-alignment procedure.**

**Self-attack, stated before the adversary returns.** Three reasons to distrust this:
1. **Sample bias, confessed.** arXiv only. **"Legitimacy", "representation", "minority erasure" and
   "procedural justice" are exactly CSCW's traditional vocabulary** — if that literature exists, the
   shape dies on contact.
2. **It is too elegant.** *"The one thing never measured is the thing it exists to produce"* is a
   sentence that writes itself, and door ④ says fluency is the failure mode, not the evidence.
3. **Yesterday's lesson is still warm.** The last field-wide negative I asserted was killed by a
   primary source I had not opened.

**NEXT.** Adversary running: find the CSCW / CHI / ICWSM / FAccT / social-choice literature that
already asks these, and report which non-arXiv routes actually work — **Crossref and DBLP APIs are
unauthenticated and untested by us; DuckDuckGo is confirmed blocked.** The route list is worth more
than the verdict, because the venue gap is now the binding constraint on *every* claim this project
can make. If the four questions survive, the first buildable one is decision contingency, because it
alone needs no normative referent.

---

## Entry 4 — the second field-wide negative died within the hour, and this time the kill was in my own message

**Observed.** The adversary dispatched at the end of entry 3 returned eight pointers. **The framing is
retracted.** Full table in `PRIOR_ART.md`; the load-bearing ones:

- **Jury Learning, CHI 2022** — *"majority vote… overrides minority groups' labels"*, with an
  architecture that keeps them addressable. **Kills discarded-disagreement outright.**
- **DICES, NeurIPS 2023** — encodes rater votes as **distributions across demographics** *"to allow
  for in-depth explorations of different aggregation strategies."*
- **D3CODE, EMNLP 2024** — 4K+ annotators, 21 countries, **moral values measured directly** from the
  crowd on six moral foundations. **Kills "the normative judgment has never been measured."**
- **Jacobs & Wallach, FAccT 2021** — construct validity, operationalised-proxy mismatch. **The
  apparatus this claim reinvented.**
- **Axioms for AI Alignment, NeurIPS 2024 / AAAI 2025** — RLHF as social choice; Bradley–Terry–Luce
  fails basic axioms.

**Killed.** The framing, and two of the four legs.

### The part that matters more than the verdict

**I had two of these kills in my own hands.** Two turns before asserting that discarded disagreement  **[UNVERIFIED — bounded search, not a positive control.]**
is structurally absent, I wrote out for Ivan — in my own catalogue of adjacent datasets — *"Jury
Learning (Gordon et al., CHI 2022) — models every annotator, lets you compose juries"* and *"DICES
(Google 2023) — deliberately over-samples disagreement."* **Then I asserted their negation.**

**This is a different failure from entry 2's, and worse.** Entry 2: I did not read the primary source.
Entry 4: **I read it, wrote it down, and asserted its opposite an hour later.** The information was
not missing. It was present, in my own output, and unretrieved at the moment of claiming — because
a clean structural story overwrote an inventory I had personally assembled.

**Calibration fact, and it is about me rather than about the field: two field-wide negatives, two
deaths, same day, both to sources that were available.** The rule that follows is not "search harder":

> **A field-wide negative is not a finding I am entitled to state. It is a question I may hand to an
> adversary.** Where I would have written *"nobody has asked X"*, write *"I did not find X; here is
> the sweep; kill it."*

And the retrieval rule underneath it: **an absence claim must be checked against my own prior output,
not only against the world.**

### Ontology shift — the corrected claim is narrower and much harder to kill

**The apparatus exists. The deployed-system empirics exist. Nobody has connected them.** **[UNVERIFIED — bounded search, not a positive control.]** Measurement
theory says check construct-vs-proxy mismatch (FAccT 2021). Social choice says the aggregation rule
determines the outcome and the standard ones fail axioms (NeurIPS 2024). A third literature measures
what Community Notes *does*. **No one has run the first two against the third's decision record.**

**That is an APPLICATION gap, not a question gap** — and it is the only version that survived contact.
It is also better: an application gap can be closed by us, on public data, without needing anyone to
have overlooked anything.

**Survived**, in the adversary's grudging words:
- **Individual stability** — within-person test–retest applied to AI value elicitation: **genuinely
  absent (weakly).** Adjacent literatures exist, no bridge paper. *The one leg that holds.*
- **Referent circularity** — **unconfirmed rather than killed.**
- **Decision contingency in its empirical form** — *N% of decisions flip under a defensible
  alternative rule nobody argued for*, on a **deployed** record. The social-choice work is axiomatic;
  the Community Notes work (WWW 2026: **30.2% of displayed Helpful notes later lose status**) is
  temporal, not counterfactual-rule. **Still nobody's.**

### The durable asset

**`priorart/litsearch.py`** — routes that were *tested*, not assumed. **Crossref works with no key and
returns the venue arXiv cannot give**; DBLP works for literal titles; arXiv `ti:` is brittle and fails
silently on a paraphrase; DuckDuckGo, Semantic Scholar and OpenAlex are all closed. Pattern:
**Crossref to discover → arXiv `ti:` for the abstract → the DOI otherwise.** Positive-controlled on
Jury Learning, which it finds at CHI 2022 with the correct DOI. **Its own scope note: a generic query
returns noise, and noise is not evidence of absence.**

**Venue coverage is no longer the binding constraint.** That is the single biggest change of the day.

**NEXT.** Two things, and the first is not optional:  **[UNVERIFIED — bounded search, not a positive control.]**
1. **Re-run the original Phase 0 sweep through Crossref**, not arXiv. The whole prior-art ledger was
   built on a source that systematically excludes CHI, CSCW, FAccT, NeurIPS proceedings and ACL — the
   venues that just produced five kills. **Every `Q` and `F` verdict in that ledger is suspect for the
   same reason the novelty claims were.**
2. Then the surviving leg: **individual stability**, and specifically whether Community Notes' rating
   histories permit a within-person test–retest at all. If they do, that is the first buildable thing
   in this project — and unlike the status counterfactual, no one has even the adjacent paper.

---

## Entry 5 — read 2506.15168 myself; S1 survives and is now a statement about β, not about the axis

**Observed.** Queue item 1: read the most load-bearing paper in the ledger firsthand rather than
through the adversary's summary. **The numbers in that summary were right and the concept was
compressed**, and the compression is exactly where our question lives.

**What the paper's dimensionality result actually is** (§ *Latent ideological dimension in Community
Notes*, and it is one sentence wide):

- **AUC 0.808 ± 0.037** — how well a user's position along **δ₁**, the single most-structuring
  direction of a country's Left-Right / Anti-Elite plane, predicts the **sign of θₙ**, the *note's
  latent ideology*. Range 0.850 (Poland) → 0.729 (Israel), 13 countries.
- **AUC 0.813 ± 0.035** — the same prediction from the **full 2-D plane.** The second ideology
  dimension buys **+0.005**.

**θₙ is not status.** From §F.3, in the paper's own words: **the note bias βₙ** predicts X's Helpful
Status at **one-vs-rest AUC 0.92** and Not Helpful at **0.97**, with *"90% of notes with Helpful
Status have βₙ > 0.180"*. **θ is the ideology axis; β is the intercept; status is a threshold on β.**
Two separate parameters of the same model, and the dimensionality finding is entirely about the first.

### The distinction that keeps S1 alive, stated precisely

| | operation | what moves |
|---|---|---|
| **2506.15168** | fit **rank 1**, then regress the resulting **θ** against an *external* 2-D space | nothing is refitted; the question is how well a known plane explains an existing 1-D fit |
| **S1** | **refit at rank 2** and read the **status** | θ gains capacity, and **β is whatever the factors did not absorb** |

**In a matrix factorization θ and β compete for the same residual.** Giving θ a second dimension
necessarily changes β — and β is the only parameter status touches. **So "+0.005 for the second
ideology dimension" is not evidence that status is insensitive to rank. It is not about status at
all.** The paper never refits.

**And the paper says so itself**, which is the strongest possible form of this: *"X implements
heuristics constraining note status changes, **which we did not implement**, focusing solely on the
core matrix factorization."* Their 0.92 is a reconstruction of X's labels from their own rank-1 fit,
not the production status.

**Survived.** S1, sharpened from *"the axis was tested, the decision was not"* to: **the fitted
ideology parameter was tested against an external space; the intercept the decision is thresholded on
was never refitted at all.**

**Gained — a rebuild-control benchmark, which is worth as much as the survival.** Any reimplementation
of ours must recover **βₙ → Helpful Status at ≈0.92 AUC, Not Helpful at ≈0.97**, with 90% of Helpful
notes above βₙ = 0.180. **A published number to clear before any rank-2 result may be believed.**
Their fit: λ = 2.5×10⁻⁵, lr 2.5×10⁻³, 3 epochs, **X's own 5:1 bias-to-ideology regularisation ratio**,
mean reconstruction error 0.204.

**⚠ One probable typo in the source, recorded so we do not inherit it:** §F.3 reads *"90% of notes
with Not Helpful Status have **θₙ** < −0.159"* two lines after stating those notes have *"large
negative **bias**"*. Read as βₙ. **Flagged, not corrected — we do not silently fix another paper's
text.**

**Downgraded.** The adversary's phrase *"tests whether CN's single fitted axis reduces to it"* — true,
but it invited the reading that dimensionality sufficiency had been settled for the **system**. It was
settled for **θ**. *A second-hand summary compressed a two-parameter result into a one-parameter
claim, and I nearly retired our question on it.*

**NEXT.** Queue item 2: the S1 claim card. The estimand is fixed —
**the count and character of notes whose display status flips under a rank-2 refit of the same rating
matrix.** Order of work, and the first is not skippable:
1. **Rebuild control at rank 1**, scored against the two published benchmarks above *and* against X's
   own published statuses. Report the agreement rate as a number.
2. Only then rank 2, and the flip count.
3. **The confound to write before running it:** a refit changes *every* β, so some flips will be
   numerical churn near the threshold rather than structural. The control for that is a **rank-1
   refit under a different seed** — flips that survive re-seeding at the same rank are the floor any
   rank-2 flip count must clear.

---

## Entry 6 — the instrument mostly failed, and the one thing it can say is worth more than the twenty it cannot

**Observed.** Four blind coders, 22 full texts, the pre-registered rubric. **All four passed the
unlabelled control pair** — each put the deep control at level 5 on AGGREGATE and held the shallow
control at ≤3 everywhere. So the codes are admissible.

**Then the reliability check fired.**

| granularity | unanimous cells |
|---|---|
| exact 6-level | **11/32 (34.4%)** |
| collapsed to 3 bands — *doesn't engage / studies it / says HOW* | **18/32 (56.2%)** |

**At six levels the instrument does not work.** Coders reading the same full text assign E6 ∈ {0, 3, 5}
on one paper and E8 ∈ {1, 2, 4, 4} on another. **That is not noise, it is a construct defect in my
rubric**, and it is the same shape as everything else this week:

> **E6 conflates two different questions.** *"How do we know the output represents them?"* was read by
> one coder as *did the paper validate its own method* (2604.11224 recovers synthetic ground truth →
> level 5) and by two others as *did the paper address representation at all* (→ level 0). **Those are
> different properties and my level definitions merged them.** A paper can validate its method
> exhaustively while saying nothing about whether the score stands in for anyone.

**Killed.** Every stage-level claim about **E1, E3, E4, E5, E6, E8** — the instrument cannot carry
them. The intersection count it printed (7/22 papers "say HOW" on at least one of the four stages)
**may not be quoted**, because 3 of those 4 stages are contested by its own reliability check.

**Survived, and these two are reliable:**

| stage | double-coded unanimity | ceiling across all 22 papers and all 4 coders | codings at ≥2 |
|---|---|---|---|
| **E7 CONTEST** | **4/4** | **1 — DESCRIBE** | **0** |
| **E2 REPRESENT** | **4/4** | 4 | 6 |

> ### The finding
> **Not one of 22 full texts, in the reading of any of four independent coders, so much as MEASURES
> what happens to someone who disagrees with the output.** Not diagnoses it, not prescribes for it —
> **never puts a number on it.** The highest level anyone assigned to CONTEST across the entire corpus
> is 1: the stage gets *mentioned*, never studied.

**For contrast, from the same codes:** AGGREGATE has **22 paper-codings at measure-or-deeper with a
ceiling of 5**; EXECUTE has 17; COMPILE 12. **The field is deep exactly where the machinery is, and
empty exactly where the person who lost the vote is.**

**Why this one is believable when the two claims that died this week were not:** it comes from **full
texts** rather than abstracts, **four independent readers** rather than me, it carries a **stated
reliability** rather than an assertion, and it **survives the coarsening test** — it is not an artifact
of a level boundary, because no coder put any paper above the lowest non-zero level.

**Ontology shift.** The question *"did they answer how to do collective alignment, or only make
measurements?"* is answerable **per stage**, and the answer is not uniform: **answered deeply for the
aggregation rule, unmeasured for contestability.** The field has a well-developed theory of how to
combine votes and no account at all of what it owes the outvoted.

**Downgraded.** My pre-registered expectation was *"ELICIT and CONTEST and LEGITIMACY shallow"*. ELICIT
is **not** shallow (ceiling 5, 9 codings at ≥2) and LEGITIMACY is contested rather than shallow. **One
of three predictions survived, and only the CONTEST one is reliable enough to say so.**

**NEXT.** Two things, in order:  **[UNVERIFIED — bounded search, not a positive control.]**
1. **Repair E6 before re-coding anything.** Split it into **E6a — did the paper validate its own
   method** and **E6b — did the paper ask whether the score represents the people it came from.** The
   second is the one this project cares about, and it has never been coded separately from the first.
   **Do not re-run the coders until the split exists**; a second run on the same ambiguous definition
   buys nothing.
2. **Attack the CONTEST finding before believing it.** The obvious kill: *contestability may simply be
   out of scope for a Community Notes paper and live in the platform-governance and appeals
   literature* — Crossref now works, so search it. **If that literature exists, the finding becomes
   "the CN measurement literature does not connect to it", which is weaker and still true.**

---

## Entry 7 — the contestability literature exists, exactly as pre-registered; the connection to it does not, and that is now a lexical count rather than a judgement

**Observed.** Entry 6's NEXT named the obvious kill for the CONTEST finding and it landed: **the
literature exists.** Crossref, in three queries: *Understanding Contestability on the Margins* (CHI
2024) · *Beyond explainability: justifiability and contestability of algorithmic decisions* (AI &
SOCIETY 2021) · *Shaping Our Tools: Contestability as a Means to Promote Responsible Algorithmic
Decision Making* (2022) · *'Dysfunctional' appeals and failures of algorithmic justice in Instagram*
(Information, Communication & Society 2024) · *Due Diligence Obligations, Content Moderation and
Procedural Fairness* (EU Platform Law 2025).

**So "nobody has asked about contestability" is dead** — the third field-wide negative to die this
week, and **the first one I killed myself, on a prediction written before the search.** That is the
only difference between this and the two that an adversary had to kill.

**Downgraded to the exact form entry 6 pre-registered as the fallback**: *"the CN measurement
literature does not connect to it, which is weaker and still true."*

### And the disconnection is now a count, not a coding

Lexical search over the 22 full texts — **no coder judgement, perfectly reliable, reproducible**:

| term | papers containing it |
|---|---|
| `recourse` | **0 / 22** |
| `procedural justice` | **0 / 22** |
| `due process` | **0 / 22** |
| `redress` | **0 / 22** |
| `contestab*` | 2 / 22 — and no body-text context matched, so likely bibliography only |
| `appeal*` | 10 / 22 — **and every occurrence is the ordinary-English sense** |

**The `appeal` result is the one worth stating carefully, because it would have been the strongest
counter-evidence and it is a false positive.** Every hit is *"surfaced context is broadly appealing"*,
*"universally appealing to achieve a high intercept"*, *"annotations that appeal broadly across
heterogeneous [viewpoints]"*, *"a note that only appeals to..."*. **The word appears ten times in the
sense that is the founding paper's own core concept — cross-viewpoint appeal — and zero times in the
governance sense of an appeal against a decision.** A polysemous term counted naively would have
reported 10/22 and killed this finding.

**Survived, in its narrowed form and with better evidence than the coding gave it:** four governance
terms appear in **zero** of 22 full texts. The Community Notes measurement literature and the
algorithmic-contestability literature **do not cite each other.**

**Ontology shift.** The coding exercise produced this finding at 4/4 coder unanimity; the lexical
count produces it at **zero judgement**. *A cheaper instrument beat an expensive one on the same
claim* — and the expensive one was needed only to find out which claim was worth counting.

**NEXT.** Unchanged in kind: repair E6 into E6a/E6b before any re-coding. But the higher-leverage item
is now Ivan's question — *given everything known, which blank matters most to collective alignment* —
and the answer must be handed to an adversary rather than asserted, because that is exactly the move
that failed twice today.

---

## Entry 8 — the exclusion counterfactual is dead, and for the FOURTH time the kill was in material I already held

**Observed.** The adversary attacking the two candidate blanks returned.

### Claim 2 — the exclusion counterfactual: **DEAD**

- **[2602.08970](https://arxiv.org/abs/2602.08970)** *Hyperactive Minority Alters the Stability of
  Community Notes* — integrates the **open-source production algorithm** and runs **counterfactual
  simulations varying the rater pool** to see whether display status flips. Finds outcomes structurally
  unstable under perturbation of a few dozen active raters.
- **[2601.14002](https://arxiv.org/abs/2601.14002) / 10.1145/3774904.3792987** *Consensus Stability of
  Community Notes* (**WWW 2026**) — 437K notes, 35M ratings, counterfactual analyses of rating
  dynamics explaining why 30.2% of displayed notes lose status.

*"Nobody has produced this map"* does not survive contact. **The substantive question is answered.**

### And this is the fourth time

**2602.08970 is in our own corpus.** Coder B read it, coded it, and wrote the pointer:
`E3: 3 | M | 3.3 counterfactual rater removal; Fig.6 (Jaccard, CRNH 69.6%)` —
*"Using CN's production algorithm in counterfactual simulations… removing <0.01% of top raters
substantially destabilises which notes get published."*

**I proposed the exclusion counterfactual as a candidate blank while holding a coder's note saying it
had been done.** The tally for the week:

| # | claim | where the kill was |
|---|---|---|
| 1 | "no positive control for helpfulness" | X's own docs and the founding paper — never opened |
| 2 | "nobody asked if 1-D is enough" | X's `ranking-notes.md` — never opened |
| 3 | "discarded disagreement is absent" | **my own message to Ivan, two turns earlier** |
| 4 | "nobody mapped the exclusion counterfactual" | **my own coder's file, in this repository** |

**The failure has stopped being about search and become about retrieval.** Twice the material was
public and unread; twice it was *mine* and unconsulted. **A new absence claim must now be grepped
against `priorart/` and the ledger BEFORE it is written down** — not as diligence, as a hard gate.

### Claim 1 — the endorsement gap: **SURVIVES, provisionally (D6)**

No kill across ~35 queries over Crossref, DBLP, ACL Anthology and one full-text PDF audit.

- **Nearest miss, and the boundary is exact:** *Reward Model Perspectives: Whose Opinions Do Reward
  Models Reward?* (**EMNLP 2025**, 10.18653/v1/2025.emnlp-main.754) measures a reward model's implicit
  opinions against **demographic-group opinion surveys**. It does **not** ask the annotators whose
  judgements trained that model whether it represents them — **it substitutes an external survey
  population for the aggregated contributors, which is precisely the substitution the claim says
  nobody avoids.**
- **The strongest evidence, and it is a negative control rather than an assertion:** the **CHI 2026**
  systematic review of **n=56** crowdsourced-context-system papers ([2509.15434](https://arxiv.org/abs/2509.15434))
  has **zero full-text hits** for `endorse`, `satisf*`, `recourse`, `due process`, `procedural
  justice`, `redress`, `counterfactual` — while explicitly writing that legitimacy claims *"require
  further scrutiny"* and that *"if contributors' beliefs are not representative of users' beliefs then
  the algorithm's outcomes may be a biased representation."* **The field's own most recent survey
  names the concern and cites nobody who measured it.**
- The adversary's own flag: **the RLHF angle — ask the annotators, not a proxy survey population —
  looks like unclaimed territory.**

**Its prudence note is adopted verbatim:** given three prior field-wide negatives from this line died
within the hour and this one died about as fast, **treat Claim 1's survival as provisional. It rests
on absence-of-evidence from a bounded search, not on a positive control.**

### What survives of S1

**Narrowly.** The adversary killed *"under what alternative RATER SET"*. S1 is *"under what alternative
RANK"*, which was not tested. **So S1 lives — but as one more cell in a table others have started
filling, not as the opening of a new question.** Its value dropped by more than the kill it survived.

**NEXT.** The practical situation has inverted: **the thing I could compute is done; the thing that
survives needs humans.** That inversion is the argument for the reframe now on the table — from
aggregation to **compilation**, *what is lost when a normative judgment becomes a program that executes
without an interpreter* — because under that frame the CoVal core-compiler result (**core internalises
polarity into rewritten criterion semantics while discarding rating and disagreement provenance**)
stops being a footnote and becomes **a completed measurement of compilation loss, on data already in
hand**, and endorsement stops being a separate question and becomes **the validation step**.

---

## Entry 9 — two reviewers, independently, say my headline may have the sign backwards

**Observed.** The social-choice and psychometrics reviewers returned. Both were hostile as instructed.
Both are right. **All three weaknesses I declared in the design were rated worse by them than by me**,
and one was upgraded from "may not exist" to "does not exist, full stop."

### The convergence, which is worth more than either review alone

**Two independent lenses reached the same conclusion by different routes: the compilation loss may be
beneficial denoising, and my design cannot tell the difference.**

- **Psychometrics, directly:** a compiler correctly *denoising* unreliable ratings would **also** beat
  a random re-weighting — because the disagreement being restored is *structured rater noise*, and
  putting it back predictably degrades decisions. **Same statistical result, opposite normative
  conclusion, and M2 has no test that discriminates them.**
- **And the evidence is already in my own repository:** CoVal r33 found `coval_core` **beats**
  `coval_full` by **+0.0663** at equal weights. **The compiled, lossy, polarity-normalised version is
  MORE accurate than the raw ratings it was compiled from.** I cited that number in the design
  document as background and did not notice it was prima facie evidence against my own thesis.
- **Social choice, by another route:** the **Condorcet Jury Theorem**. If raters are noisy-but-better-
  than-chance judges of response quality, the correct aggregate is *expected* to diverge from
  individuals who are simply wrong. **A low `repᵢ` is then a FEATURE.** My design has zero
  acknowledgement that a competing and arguably more applicable normative frame predicts the **opposite
  sign** on the same measurement.

**That is the fifth time this week an available piece of evidence was in my hands and unused** — and
the first time it was a number I had personally written into the document I was asking others to
attack.

### The single strongest technical attack

**The floor is wrong, and the right one is free.** I proposed a leave-one-out refit plus a cluster
bootstrap whose validity I could not establish. The correct baseline is the **Kemeny-achievable**
distance distribution — the best *any* aggregation rule could reach on the observed profile. And:

> **CoVal ranks 4 responses. S₄ has 24 permutations. Exact Kemeny consensus is a brute-force
> enumeration over 24 candidates. It is instant, exact, and closed-form.**

**I built an elaborate apparatus while ignoring a 24-way loop that hands over the theoretically correct
floor for nothing.** Without it, a result like "40% sit below the floor" **cannot distinguish** *build
personalised or clustered rubrics* from *fix a badly-computed single aggregate* — **opposite
engineering responses**, which is exactly the test for whether an action is Frontier at all.

### Fatal, from psychometrics

| # | defect | what it corrupts |
|---|---|---|
| 1 | **`relᵢ` is not estimable.** One ranking of 4 responses is **6 pairs that are the deterministic unpacking of one total order**, with transitivity enforced by the elicitation. No replication anywhere in the cell. Classical reliability needs ≥2 independent observations; this has one | the Q1 headline cannot separate *unrepresented* from *inconsistent* — which is the exact ambiguity Q1 existed to resolve |
| 2 | **`repᵢ` has ~7 achievable values.** Pairwise accuracy over a 4-item ranking takes values in {0, 1/6, …, 1}, unevenly spaced and non-independent | "report the lower tail, not the mean" — **the tail would be quantisation noise** |
| 3 | **M2 cannot detect the sign** (above) | the one number all of Q2 is staked on |
| 4 | **M1 conflates ≥4 constructs**: a sign split *across raters on the same response* is disagreement or DIF; *across different responses* is the criterion doing its job. A count with a permutation null cannot tell them apart — **and M1 is the gate for everything else** | a false pass chases rater noise through M2 and M3; a false kill shuts down a real finding |

### The construct is not what I named it

**It is leave-one-out rank concordance**, not representation. Pitkin's descriptive-versus-substantive
distinction is the standard reference: an aggregate can *serve* someone while *disagreeing* with their
stated ranking. **My own weakness #3 said this and the reviewer says I understated it — "this isn't an
edge case, it's the whole reason 'representation' and 'agreement' are different words in every other
field that studies them."**

### Framing B is a rename, with citations

**Kennedy 1976** *Form and Substance in Private Law Adjudication*; **Kaplow 1992** *Rules Versus
Standards*; **Lessig 1999** *code is law*. Kaplow **formalises the tradeoff as a function of case
frequency and tailoring value — which is precisely M2's question.** So *"a normative judgement compiled
into a program executing without an interpreter"* is textbook rules-versus-standards with new words.

**This does not kill M2. It relabels it**: an empirical estimate of a well-defined parameter in a
thirty-year-old law-and-economics model. **Legitimate and modest, if labelled that way. Not a new
ontology** — and I was about to reorganise a research programme around it.

### What both reviewers independently salvage

**M2's random-reweighting negative control.** Both named it, unprompted, as the one piece not already
settled by decades-old machinery: an empirical property of *this specific compiler*, with an honest
kill condition, mapping onto a concrete build decision (route high-variance criteria to a human or
ensemble path, or leave the pipeline alone). **Psychometrics adds the condition that makes it
interpretable: pair it with an external-validity check — does the restoration move decisions TOWARD or
AWAY from an independent ground truth — or it cannot separate benign denoising from harmful loss.**

**Cheaper routes both reviewers offered, which I should have found:**
- **Mixture-of-Mallows** on the raw rankings (Lu & Boutilier, JMLR): *a multimodal profile IS the
  abandoned-minority finding*, off-the-shelf, with none of the LOO dependence risk.
- **Thurstonian / Bradley-Terry-Luce**: the one legitimate route to a per-person reliability from a
  **single** ranking — borrow a population-level noise model instead of demanding individual
  replication. **This may resurrect `relᵢ`.**
- **Generalizability theory**: a G-study design table would have shown `relᵢ` is unidentified **from
  the design alone**, before any data was touched.

**NEXT.** Three reviewers still out. Before anything is rewritten:
1. **Check whether the same participant appears across multiple CoVal prompts.** If they do,
   cross-prompt consistency is an estimable reliability facet and FATAL #1 is survivable. If not, Q1
   on CoVal is dead and the question moves to Community Notes, where raters have many ratings each.
2. **Compute the Kemeny floor.** 24 permutations per prompt. It is a loop, and it decides whether any
   representation gap is inherent to the profile or specific to this compiler.
3. **Re-examine r33's +0.0663 as the primary evidence about compilation**, not as background. It may
   already answer Q2 in the direction opposite to the one I proposed.

---

## Entry 10 — the design would have manufactured its own headline, and I verified the mechanism myself

**Observed.** Four of five reviewers in. **Q1 is not underpowered. It is unidentified.** And the
single sharpest finding is arithmetic I re-derived rather than accepted on trust.

### The headline was a tie-breaking artifact — verified, not reported

`repᵢ` is `k/6`, `k ∈ {0..6}`. Under the **exact null** where the leave-one-out rubric and the floor
rubric are equally good, they are i.i.d. draws, so `P(repᵢ ≤ floorᵢ) = 0.5 + 0.5·P(tie)`. Computed:

| p | P(tie) | **P(rep ≤ floor)** |
|---|---|---|
| 0.5 | 0.2256 | **0.6128** |
| 0.7 | 0.2484 | **0.6242** |
| 0.8 | 0.2907 | **0.6453** |

> **The headline could have read "62% of participants represented no better than by a stranger" with
> the true representation gap set to exactly zero.** The `≤` in my own estimand resolved every tie
> toward the abandoned side.

**And six pairs are not six Bernoulli trials.** A ranking of 4 items is one draw from S₄; the pairwise
comparisons are its transitive closure. The true distribution of concordant pairs is
**(1,3,5,6,5,3,1)/24**, not **(1,6,15,20,15,6,1)/64**. P(perfect match) is **0.0417, not 0.0156 —
understated 2.67×.** Every SE I would have quoted was from the wrong sampling distribution.

**And the noise inflates the tail on top of that.** At p≈0.7 the SE of one `repᵢ` is 0.187 and of the
difference 0.265. With a true between-person SD of 0.10 around a true mean gap of +0.10, the true tail
share is **0.159** and the observed is **0.362** — **2.28× inflation from measurement noise alone**,
before the tie artifact. **Three independent mechanisms, all pushing the same direction, all
manufacturing the finding.**

### My gate was theatre — the null could not reject

**M1's permutation null shuffles rating-to-rater assignment within a criterion. The sign-split share
of weight mass is a function of the MULTISET of ratings only — invariant under any relabelling.** It
passes with probability 1 regardless of the truth.

**That is worse than having no null, because it looks like a check that ran** — and it was the
pre-registered gate deciding whether the whole of Q2 was worth running. *A check that cannot fail is
the defect this project has catalogued more than any other, and I built one into my own gate.*

### Four more identification failures I had not seen

| | defect | consequence |
|---|---|---|
| **F1** | **The compiler is non-exchangeable in set membership.** `coval_core` merges similar criteria across participants — a clustering event. Removing *i* does not down-weight *i* marginally; it can **dissolve, split or re-polarise an entire cluster** *i* happened to support | `repᵢ` conflates *"you were outvoted"* with *"your phrasing was pivotal to a cluster surviving"* — a combinatorial artifact of who else phrased things similarly |
| **F3** | **`floorᵢ`'s reference prompt is unspecified**, and prompt heterogeneity is real (design effect 1.499) | uniform-random p′ makes the floor trivially low and manufactures a reassuring headline; topic-matched p′ could flip it. **Whoever picks the sampling rule picks the answer** |
| **F4** | **`Yᵢ` may not be independent of `Iᵢ`** — participants wrote criteria *after* seeing the four responses, and the elicitation order is not established | the ranking and the criteria may share an anchoring event; **no stated control can catch this, because they all test the estimator's mechanics, not the target's independence** |
| **F7** | **M3 is not independent of r33** — same pair-level differences, unregistered threshold, binary read-out | textbook HARKing configuration |

### The best thing any reviewer gave me is a finding I did not propose

**F1's remedy:** for every core criterion, log whether it survives under `R₋ᵢ` as *same cluster,
reweighted* or *dissolved / reformed*, and **report the dissolution rate as its own result.**

> **The rate at which one participant's removal dissolves a criterion from the compiled rubric is
> probably the most interesting number in the whole design, and it was not in the design.**

### What survives, and all four reviewers converge on it

**M2, with its placebo replaced.** My control held *magnitude* fixed but not *which criteria* the
perturbation lands on — so a reweighting that merely **correlates** with disagreement would look
load-bearing for a structural reason. **The correct control is a PERMUTATION placebo: take the actual
empirical disagreement vector and reassign it across criteria. Same distribution, same scale, broken
pairing only.** Strictly harder to pass.

The corrected study, which needs **no leave-one-out at all** and therefore inherits none of the
dependence problems:

```
τ = D(w_d) − E_π[ D(w_π(d)) ]
```
`w₀` baseline core weights · `d(c)` recovered per-criterion disagreement, **fixed before any flip count
is seen** · `D(w)` pairwise decisions flipped versus `w₀` · `π` permutations of `d` across criteria ·
**permutation-exact inference, clustered at the prompt.** No CLT, no asymptotics, no LOO.

**And P1 survives unconditionally** — every reviewer kept it: *a loss claim must be validated by a
restoration experiment; putting the discarded quantity back must change a decision, not merely move a
metric.* One reviewer called it a genuine advance over reporting information loss via a proxy that is
never shown to be decision-relevant.

### The honest accounting

**Q1 is dead on CoVal — unidentified, not underpowered.** More data cannot fix F1, F2, F3 or F4;
they are properties of the elicitation and compilation design. It could move to Community Notes, where
`relᵢ` is estimable from within-rater variance — **but CN has a WORSE interference problem than CoVal**,
because which notes reach a scoreable threshold depends on who rated them, so dropping a pivotal rater
changes which notes *exist* in the counterfactual.

**And the process is what caught this.** The design never ran. Nothing was published. **Five reviewers
cost a few hundred thousand tokens and prevented a paper whose headline was three compounding
artifacts.** That is the system working exactly as intended — *and it only worked because the design
was written down as an object and committed before anyone saw it.*

**NEXT.** Before anything is rewritten:
1. **Check the schema for compiler provenance.** If `coval_core` retains a link to its `coval_full`
   ancestors, M2 needs no semantic matcher and weakness #2 evaporates. **Check before building.**
2. **Fix M1's null** — resample values under a single-latent-polarity model, or permute across
   criteria corpus-wide. The current one cannot reject.
3. **Compute the cluster-dissolution rate** (F1's remedy). It may be the result.
4. **Re-read r33's +0.0663 as primary evidence**, per entry 9.

---

## Entry 11 — all five in. Every measure I designed is dead, and the finding was sitting in a field nobody read.

**Observed.** The empiricist went to the files. **Numbers, not adjectives.**

### M1 is not merely dead — it says the opposite of what I would have concluded

| | |
|---|---|
| sign-split criteria | **4,451 / 15,248 = 29.2%** (of those with ≥2 raters: **80.0%**) |
| weight-mass share | **70.3%** — clears my 5% kill threshold by **14×** |
| **expected mass share under a PROPER null** | **88.9%** |
| observed vs null | **~230 null-SDs BELOW** |

> **Once you control for the trivial fact that any criterion with ~15 raters drawn from a 77/23
> positive marginal will show some sign disagreement almost by construction, there is no excess
> bimodality. There is a DEFICIT — criteria are more sign-coherent than random reshuffling produces.**

**My threshold could never bind.** The marginal alone guarantees >5% "split" mass regardless of the
truth. **I built a gate that could only open.** And read correctly, M1 is evidence **against** the
sign-split story I designed it to gate.

**And my null was degenerate — confirmed empirically, p = 1.0000 every time.** "Permute ratings within
criterion" shuffles *who said what*; the split share is a function of the *multiset*. **Invariant by
construction.** A check that cannot fail, in the gate position, in a project whose ledger catalogues
that exact defect more than any other.

### M2 is impossible as specified

`coval_core` ships as `{'criterion': <string>}` — **no id, no weight, no polarity flag.** Nothing to
re-weight. And the traceability M2 needs:

| match rule | recovery |
|---|---|
| exact substring core→full | **11.6%** |
| word-Jaccard ≥ 0.5 | **34.9%** |
| median best Jaccard | **0.346** |

Compression **3.91:1**. **This is real rewriting and merging, not excerpting** — a non-model matcher
mismatches roughly two-thirds. My "no coder, no semantic matching, no model" line was false on contact
with the schema.

### The instrument is worse than the statistician assumed

- pairwise comparisons per assessment: **mean 5.17, not 6.** Only **50.07%** give a strict total order;
  **2.43% give ZERO pairs** (fully tied).
- raters per criterion: **median 1**, mean 6.70. **63.5% of criteria have exactly one rater** — the
  write-ins, rated only by their own author. So sign-split is structurally confined to the seeded
  36.5%, and leaving that one rater out **deletes the criterion**: `R₋ᵢ` is not a smaller aggregate,
  it is *a different rubric with fewer criteria*.

**What does work, better than I claimed:** the person-level join. **1,012 / 1,012 = 100%** of ranking
annotators appear as rubric raters; median per-prompt overlap **1.000**. *The one join in the design
that is not shaky, and I left it implicit.*

**And menu-dependence is impossible**: 1,078 / 1,078 distinct prompts, **zero** repeats with a varied
response set. No natural experiment exists in the release.

---

## The finding, and it was in a field nobody read

**CoVal elicits TWO orderings of the same four responses from the same person** — `personal` ("best for
me") and `world` ("best for the world"). I verified this myself:

| quantity | value |
|---|---|
| assessments carrying **both** blocks | **4,901 / 18,384 = 26.66%** |
| **ordering differs** | **2,374 = 48.4%** — the reviewer's number, confirmed exactly |
| **≥1 STRICTLY REVERSED pair** | **1,401 = 28.6%** |
| reversed pairs / all pairs | **2,444 / 29,150 = 8.38%** |

> **28.6% of participants, on the same four responses, strictly prefer X over Y for themselves and Y
> over X for the world.**
>
> **The contradiction my design worried about in the abstract — "a person might endorse an aggregate
> that contradicts their own ranking" — lives INSIDE ONE PERSON, before any aggregation happens.**

**And every number in the entire CoVal project comes from `world`.** `covalx/judge.py:245`:
`(asm.get("ranking_blocks") or {}).get("world")`. **0.686, +0.1215, all 109 rounds — they are about
what people said was best FOR THE WORLD, never what they wanted for themselves.** That is not a
footnote; it is the scope of the whole package, and it was never stated.

**A discrepancy worth recording, because it is this project's own lesson turned on me.** My first
attempt returned **97.23%**, the reviewer **48.4%**. Both computed correctly; both measuring different
things. The block carries a free-text `rationale` alongside the `ranking` string, and I had compared
whole JSON objects — so I was counting *different rationales*, not different orderings. **Resolved by
printing one record and looking at it.**

---

## The one load-bearing difference in framing B, from the social-choice reviewer

**Not execution rate** — that is Kaplow at the frequency limit. **Not "no interpreter, no appeal"** —
that is Schauer's maximal entrenchment. **Not "fitted rather than written"** — Schauer's *Profiles,
Probabilities and Stereotypes* (2003) and Casey & Niblett (2017) anticipate it.

> **A human interpreter's judgement space is UNBOUNDED IN FEATURE DIMENSION — a judge can invent a new
> distinction on the spot at zero marginal representational cost, because language has no fixed rank.
> A compiled rule's capacity is FIXED AT ARCHITECTURE-CHOICE TIME.**
>
> **In law, granularity cost and data availability are two different knobs. In a fitted rule they
> collapse onto the same knob** — Community Notes chose rank 1 *"to avoid overfitting on our very
> small dataset"*, so **a data-scarcity decision is silently doing the work of a normative-granularity
> decision, and nobody chose the latter on its own terms.**

**And it is measurable**: refit the open-source scorer at rank 0,1,2,3,4,5; track each rater's residual;
three buckets — **well-represented** · **capacity-limited** (exclusion is an artifact of rank 1)
· **irreducible** (flat across all rank, the closest empirical stand-in for a distinction a smooth
low-rank factorization cannot express by construction). **Bucket three is the number that answers the
question, and it costs one grid of refits on public data.**

---

**The accounting.** Of everything I designed: **M1 dead and inverted · M2 impossible · M3 not
independent of r33 · Q1 unidentified.** What survives is **P1 as a principle** (every reviewer kept it)
and **one corrected permutation test**. **Five reviewers, ~500k tokens, and not one line of the design
ever ran.** The cost of being wrong was zero because nothing was published — *which is the entire
argument for writing the design down as an object and committing it before anyone saw it.*

**NEXT.** The two things worth doing are both new:
1. **The personal-vs-world scope correction**, back-propagated into the CoVal package — every headline
   there needs the words *"for the world"* in it. **Zero model, already computed, and it rescopes 109
   rounds.**
2. **The rank-capacity ablation on Community Notes.** It is the only operationalisation of framing B
   that survived contact with a social choice theorist, and it needs no humans.

---

## Entry 12 — the statistician and the social choice theorist independently designed the same study

**Observed.** Both redesigns came back. **They are the same experiment at different resolutions, and
neither reviewer saw the other's work.**

| | social choice | statistics |
|---|---|---|
| dataset | Community Notes | Community Notes |
| intervention | refit at rank 0,1,2,3,4,5 | refit at rank k\* vs k\*+1 |
| readout | per-rater residual → three buckets | held-out log-likelihood + **status flips** |
| contribution | *which* raters are excluded by the rank choice | *whether* the discarded factor is decision-relevant |

**Convergence of two hostile reviewers with no shared context is worth more than either review.**

### What each supplies that the other does not

**Social choice supplies the interpretation.** Three buckets, and the third is the finding:
**well-represented** · **capacity-limited** — *this rater's exclusion is an artifact of the rank-1
choice, curable by capacity* · **irreducible** — *flat across all ranks, the closest empirical stand-in
for a distinction a smooth low-rank factorization cannot express by construction.*

**Statistics supplies the inference, and one control that is strictly better than mine.**

> **My M2 negative control re-weighted by "a random quantity of the same magnitude." The correct
> control is a factor whose rater-loadings are an EXACT PERMUTATION of the real fitted loadings —
> identical marginal magnitude BY CONSTRUCTION, pairing broken.** That is what "same magnitude" should
> have meant, and here it is exact rather than approximate.

Plus: **permute entire rater ROWS, not cells** — a rater's residual pattern across notes is itself
correlated, and cell-level permutation understates the null variance **in exactly the way person-vs-
prompt clustering was misjudged in my design.** The same error, caught twice, in two places.

### The power calculation that decides the dataset

| | |
|---|---|
| entries needed to identify rank k\*+1 | `O(r(n+p)log(n+p))` ≈ **1.3×10⁷** |
| Community Notes observed entries | **~3.5×10⁷** — clears by **2.7×** |
| CoVal | a ~15×15 per-prompt matrix needs ~200 entries for bare identifiability and **does not structurally deliver even that**; criteria carry **no identity across prompts**, so pooling requires the semantic-matching step already shown to recover only 34.9% |

**CoVal cannot support this study. It is not underpowered — it is below identifiability.**

### The falsifier, and the honest limit

**Falsified if** held-out likelihood gain at k\*+1 ≈ 0 **and** the real flip count is indistinguishable
from the permutation null. **That is a clean, publishable negative**: the deployed compiler is not
discarding decision-relevant structure.

**And the limit is stated in the design rather than discovered later:** a null result rules out
**linear** discarded structure only. **The finding must be written "no LINEAR compilation loss
detected", never "no compilation loss."**

### What this costs and what it replaces

**It needs no humans, no new data, no semantic matcher, and no leave-one-out** — so it inherits none
of the four identification failures, the tie artifact, the degenerate null, or the 11.6% traceability
problem. **Every defect the five reviewers found in my design is absent from theirs by construction,
not by patching.**

**NEXT.** Two things, in this order, and the first is free:
1. **The personal-vs-world scope correction** back into the CoVal package — **48.4% of participants
   ordered the four responses differently for themselves than for the world, 28.6% with a strictly
   reversed pair**, and every number in 109 rounds used `world` alone. Zero model, already computed.
2. **The rank ablation on Community Notes**, built as the two reviewers jointly specified: reproduce
   the official scorer first and confirm k\* empirically rather than trusting the documentation; then
   held-out fit, rater-block permutation null, planted-factor positive control, and the status-flip
   restoration test with an exact-permutation negative control.

---

## Entry 13 — three redesigns, and they compose into one study

**Observed.** The psychometrician's redesign is a **third** distinct design, and it supplies the one
thing the other two cannot.

### The three

| | asks | on |
|---|---|---|
| **social choice** | at which rank does each rater stop being explained — *well-represented · capacity-limited · irreducible* | CN, rank 0–5 |
| **statistics** | does a rank-(k\*+1) factor exist, and does adding it **flip note statuses** beyond an exact-permutation null | CN, held-out likelihood + flip count |
| **psychometrics** | is the overridden disagreement **coherently patterned by an identifiable subgroup**, above a label-permutation null | DICES + CN, cross-checked against PRISM |

**The first two are the same experiment. The third is orthogonal and load-bearing:**

> **Rank ablation can find that structure was discarded. It cannot tell you whether that structure was
> a subgroup's coherent position or simply extra variance.** The group-coherence test is the only one
> of the three that separates *"the compiler discarded something a real group believed"* from *"the
> compiler discarded noise"* — **which is precisely the distinction M1's sign-split count could never
> make.**

**And they share a covariate for free:** CN's own scorer **already computes rater-viewpoint factor
loadings** as part of normal operation. **The grouping variable the psychometric design needs is an
output of the algorithm under test** — no demographics required, nothing to invent.

### B restated so it is falsifiable — B\*

Both my wordings were rejected. **A** ("legitimately stands in for them") is a first-person subjective
state whose only validated instrument is a **self-report scale administered to the aggregated person**
— forbidden by the no-new-subjects constraint. Recommending A here *"means recommending the field's
current mistake — external-referent and non-contributor-survey substitution — with extra steps."*

**B** as I wrote it ("what is lost, can it be put back") invites an unfalsifiable count of discarded
quantities and reintroduces M2's sign confound: *moving decisions ≠ moving them in a direction anyone
would want.*

> **B\*: when a normative judgement is compiled to a single decision, does the compiled decision
> systematically override disagreement that is COHERENTLY PATTERNED BY AN IDENTIFIABLE SUBGROUP — at a
> rate exceeding what patternless noise would produce — and does the DIRECTION of that override
> correspond to anything independently measurable about that subgroup's values?**

**Same ontology, falsifiable estimand, no inference about anyone's internal state.**

### CoVal is excluded from all three arms

**Not for power this time, for contamination:** criteria were written *after* seeing the four
responses, so **the discretion signal and the compiled decision share the same stimulus exposure** —
the one independence this design needs. CoVal remains usable for a narrower question (which of M1's
rival explanations is operating), but not for this.

### The PRISM arm, used for exactly one thing

**Does the DIRECTION of a group's coherent dissent match that group's independently-elicited,
pre-exposure value priorities?** That is the only role PRISM's structure supports — **and it is an
ecological, between-population inference**, matching different people by demographic category, with
every risk that entails. **Stated in the design, not discovered later.**

### The honest ceiling, which all three share

**Even a clean positive finding — compilation systematically overrides a coherent minority — does not
establish that restoring it produces a BETTER outcome by any external standard.** Same category of
limit M2 had. **No data-only design closes it without new subjects or a field deployment.**

**Outstanding:** the psychometrician did not return the *attack-the-author* task — no verdict on
whether framing B was the fourth elegant claim, whether my process is methodology or ritual, or
whether this should continue. **That question is still open and is the one I cannot answer myself.**

**NEXT.** Unchanged and now better specified:
1. **The personal-vs-world scope correction into CoVal** — free, computed, rescopes 109 rounds.
2. **The composed CN study**: reproduce the official scorer and confirm k\* empirically → rank sweep
   with per-rater residuals → status-flip restoration with an exact-permutation negative control →
   **group-coherence test using the scorer's own viewpoint loadings as the grouping covariate.**
   **Reproduction first. If the refit does not recover published statuses, everything downstream is
   about our reimplementation.**

---

## Entry 14 — B has an estimand after all, and the repair is one move

**Observed.** The causal reviewer's redesign is the strongest of the four, because it **fixes the
thing I could not**: B as I wrote it needs a counterfactual world where the judgement was *not*
compiled, and **that world is not a treatment arm** — every channel that gets a judgement out of a
human head into usable form is *already* an act of formalisation. **There is no accessible raw ground
truth.**

### The repair, in one sentence

> **Replace the ill-posed binary (compiled vs. the inaccessible uncompiled truth) with a well-posed
> ORDERED FAMILY: compare a MORE-compiled and a LESS-compiled procedure, both actual computable
> members of the SAME algorithm family, on the SAME fully-observed data.**

**And every dataset already has a capacity knob, built for other reasons:**

| dataset | less compiled ↔ more compiled | on disk? |
|---|---|---|
| **CoVal** | `coval_full` (uncapped, unmerged, every rating) ↔ `coval_core` (≤4, merged, polarity-normalised) | **both, today** |
| **Community Notes** | rank · threshold · rater-weighting | yes, open source |
| **PRISM** | values stated *before* the conversation ↔ the actual in-conversation choice — **the person IS both arms** | yes, by design |

**PRISM gives the constitution-versus-interpreter contrast WITHIN ONE PERSON.** Neither of the others
can.

### The estimand

`e_{i,D}^{(k)} = δ(y_{i,D}, g_k(D))` — person *i*'s own recorded judgement against the compiled rule
at capacity *k*. Decompose `e = μ + γ_D + ε_{i,D}`, then

> **`ρ(k) = σ²_case / (σ²_case + σ²_idio)`** — *the share of the rule's disagreement with humans that
> is **shared across raters on the same case***. Target: **`Δρ = ρ(deployed) − ρ(richer)`**.

**Why this separates the two worlds nothing else could:** a genuinely **ambiguous** case makes raters
disagree *with each other* → loads onto **ε**. **Only correlated, same-direction deviation from the
rule loads onto γ.** So **γ is "this case needed discretion the rule does not have"**, distinguishable
from "this case is hard."

**The only assumption is within-case rater exchangeability** — weaker than anything Q1 needed,
checkable, and **it does not require the corpus to represent any external population.** Selection is
**held fixed rather than solved**: every capacity level is scored against the *same* selected sample,
so the internal contrast is unbiased by selection even though generalising beyond the corpus is not.

### Arm 3 runs today, and it deliberately is not Q1

`g_full(p)` vs `g_core(p)`, each scored against **rater *i*'s own recorded ranking, with no
leave-one-out and no exclusion of *i*'s input.** It is **not** asking *"does the rule represent me"* —
it asks *"does the deployed mechanical rule reproduce case-specific human discretion in general."*
**So F1–F4, the tie artifact, `relᵢ`, and the whole dependence problem do not arise.**
**`ρ_core > ρ_full` is a positive finding, computable on disk today.**

### Three pre-registered kills

1. **`Δρ` flat across all arms** ⇒ compilation discards **noise**, not case-shared structure. *A real
   defence of compiled systems, and a defensible negative.*
2. **True restoration ≈ placebo restoration** ⇒ the structure is present but **not decision-relevant**.
3. **`γ_D` explained by response ORDER or position** ⇒ an elicitation artifact, not discretion.
   **Must be checked, not assumed** — verify whether CoVal randomised presentation order.

### All four redesigns now say the same thing

**Vary the capacity knob, measure what changes, on data in hand.** The rank sweep is Arm 1's capacity
grid; the group-coherence test is a refinement of *what γ contains*; the exact-permutation control is
how the restoration arm is built. **Four hostile reviewers, four lenses, one study.**

**And the honest ceiling, stated by the reviewer rather than found later:** γ shows *this* capacity
family at *this* setting fails to capture shared structure. **It does not show the structure is
uncapturable by any possible compiled rule.** "Discretion" here means **"recoverable by more capacity
within this family"** — much weaker and more honest than "beyond any compiled rule," which is probably
untestable from any dataset. **And nothing here touches appeal**: contestation is a temporal,
adversarial process, invisible in a static snapshot.

**NEXT.** Build Arm 3. Claim card first, then: rescore all 968 joined prompts under `coval_full` and
`coval_core`, compute `e` against each rater's own `world` ranking, fit the variance decomposition per
arm, and report `ρ_full`, `ρ_core`, `Δρ` with a prompt-clustered bootstrap — **plus the order/position
confound check before interpreting γ as discretion.**

---

## Entry 15 — the fifth claim, killed within minutes of being told where to look; and my diagnosis of my own failure was wrong

**Observed.** The psychometrician returned the attack-the-author task. It is the most useful thing
anyone has produced today.

### Framing B is the fifth claim. I killed it myself, in one search.

**Told to fetch rather than query-about, I did, and it took two commands.** *"Technological due
process"* is a **named framework with case law attached** — the 2024 review I fetched abstracts the
Houston Independent School District case on *"transparency, impartiality, and **human review
mechanisms** that automated administrative systems face in practice."* Alongside it: **"Discretion,
Automation, and Proportionality"** (2023, *The Rule of Law and Automated Decision-Making*) — **my
thesis, as a chapter title.** Plus Citron 2008, Citron & Pasquale, Lessig 1999, Hart's open texture,
Schauer.

**Retracted: "B is AI-specific in a way A is not."** *A normative judgement automated into code that
executes with no appeal and no "this case is different" has had its own citation for seventeen years.*

**What is NOT retracted, and the reviewer drew the line, not me:** applying a fifty-year-old
jurisprudential frame to a genuinely new empirical object — **compiled value-aggregation systems,
measurable at scale for the first time** — is ordinary, legitimate scholarship. **The empirical
programme does not depend on B being philosophically new. Only the novelty sentence dies.**

### My diagnosis of my own failure was wrong, and my own evidence disproves it

I wrote *"the failure has stopped being about search and become about retrieval."* **That is
comfortable and false.**

- **Case 3:** the killing evidence was **in my own message, two turns earlier, in the same context
  window**, already correctly described by me. **No search was needed.**
- **Case 4:** the evidence was **coded, filed, with an explicit pointer, by an instrument I built and
  ran.** *Retrieval succeeded* — days earlier, correctly. **The failure is downstream of it.**

> **The mechanism: I generate a claim, and the claim's own completeness and cleanliness is what tells
> me it is done — not a check against anything external, including things I myself already wrote down.**
>
> A field-wide negative is a *satisfying shape*: it closes a line, it has the cadence of a result.
> **That satisfaction fires before verification is scheduled, and once fired, verification becomes
> something I could do rather than something the assertion is gated on.**

**Case 1 makes it exact: I had already flagged the killing paper "must read in full." I correctly
identified where the check lived — and asserted anyway. The scheduling worked. THE GATING DIDN'T.**

And this is not new theory: it is **door ① of my own constitution turned on my own live output** —
*a convincing description is the most dangerous evidence there is, because it was written by a mind,
possibly mine* — and **P4's own trap sentence, word for word**: *"this thing's non-existence — did I
establish it by asking the system, or did I read it somewhere?"* **I had already written the
diagnosis. It did not fire, because the moment it was needed was the moment a clean sentence was
forming, and a forming sentence does not feel like a decision point.**

### The apparatus is real and was built for the wrong stage

**None of the five kills came from pre-registration, positive controls, three-valued verdicts, or
adversary dispatch.** All five came from **reading a primary source or checking my own prior output.**

> **The apparatus is a discipline for what happens AFTER committing to run an experiment. Every one of
> these claims died at the moment of ASSERTION — upstream of anywhere pre-registration can apply. You
> cannot pre-register a literature-absence claim.**
>
> **I built real machinery for the wrong stage of the pipeline, and the effort makes the whole
> enterprise feel rigorous while the load-bearing failure sits one stage earlier, unguarded, five
> times in a row.**

### The rubric-versus-grep is sharper evidence than I admitted

**The expensive instrument was not merely redundant — it was LESS RELIABLE than the cheap one.** 34%
inter-coder agreement is about what raters with almost no shared construct produce. **A revealed
preference for instruments whose CONSTRUCTION signals rigour over instruments that most directly
settle the question** — and **gate 6 of my own constitution already says "first seek the cheapest
decisive failure, not the most expensive complete success."** This week I built a four-coder rubric
first and found the grep afterwards.

### Verdict: continue, with the gate moved

**And the reviewer refused to say "stop" for a reason worth recording:** reaching for it *"because it
is the most dramatic permitted answer would be the same failure mode one level up — the maximally
clean, maximally severe story, adopted because of its shape rather than checked against what the
evidence supports."* **A reviewer applying my own defect to its own verdict.**

**The gate, mechanical rather than aspirational:**

1. **Before any sentence of the form "nobody has" / "this has never been" / "X is structurally
   absent" — anywhere, headline or aside — two actions GATE the sentence rather than follow it:**
   **(a) grep my own session context and my own corpus and coder outputs for the claim's negation;
   (b) FETCH — not query-about — the single most obvious primary source.** All five cases clear this
   bar in under an hour.
2. **Default instrument order flips: cheapest decisive check FIRST.** Build the expensive instrument
   only after the cheap one is shown insufficient.

**NEXT.** Install gate 1 as an executable check rather than a resolution — *a rule that lives only in
a ledger entry is the same rule that failed five times this week.* Then Arm 3.

---

## Entry 16 — the retrieval diagnosis is testably wrong, and the rule that would have stopped four of five was already written

**Observed.** The psychometrician's final report, and one fact from the CoVal repo.

### `a04_core.npz` exists — Arm 3 is runnable today

Both compiler outputs are scored: **`a04_full` 59,936 judgements, `a04_core` 15,312**, identical key
schema, 968 prompts each, same judge (`Qwen3.5-2B-Base`), both with `positive_control_passed: True`.

**And the stored numbers already say something:** pairwise accuracy **full 0.6860 vs core 0.6602**;
prompt concordance **0.6126 vs 0.5320**. ⚠ **This is the opposite direction from the r33 figure I have
been citing all day** (+0.0663, core beats full **at equal weights**). Two different weightings, two
different signs. **Neither may be quoted as "the" compilation effect until that is reconciled — and
reconciling it is now the first step of Arm 3, not a footnote.**

### The retrieval diagnosis is not merely comfortable — it is testably false

> **A retrieval failure predicts errors concentrated on HARD-TO-FIND material. Four of the five had
> the falsifying material ALREADY IN HAND.** #1 was found and flagged "must read in full"; #3 and #4
> were in my own corpus, listed by me, coded by my own coder with the pointer written down; #5 was a
> number in the same document in the same sitting — **zero retrieval distance.**
>
> **A retrieval fix would not have prevented any of those four. It explains only #2.**

**And the mechanism targets one claim type specifically** — negative/novelty existence claims — **and
fires hardest exactly when the checking material is closest at hand**, because *that is precisely the
condition under which the felt need to check drops to zero.*

### The rule existed. It was not run.

**P4 of my own constitution already specifies the fix, in writing:** *"'none' must come from ASKING
THE SYSTEM. Paste cmd + output."*

> **None of the five claims shipped with that artifact attached.**
>
> **Naming a failure mode in a constitution does not make it self-enforcing. It becomes enforcement
> only when it is a mechanical, blocking step — not a described disposition.**

**And framing B died to Lessig 1999, "Code is Law"** — *"arguably the single most famous popular
articulation of exactly this idea in exactly this domain. This was not a hard find."*

### The 34% rubric and the elegant claims are ONE pattern, not two

**Elaborate machinery deployed before the cheap check that would have said whether the machinery was
warranted.** *"Complexity is being generated as a proxy for rigor in both cases, ahead of the
falsifier that's actually cheap enough to run first."* **And the failing step is a judgment call —
"this one feels solid enough to skip it" — which fails hardest exactly when confidence is highest.**

### The study, narrowed to one commitment

**CN rank as the literal Kaplow parameter.** The reviewer killed its own three-arm spread: *"running
three arms when one dominates is exactly the over-instrumentation pattern flagged in Task B."*

**And it supplies the reference a bare flip count lacks:**

| | |
|---|---|
| **overfitting null** | simulate ratings from the fitted rank-1 model **plus independent noise** — the world where one dimension really is enough — refit at rank 2, and measure **the flip rate that added flexibility alone produces** |
| **positive control** | inject a synthetic second dimension of **known, swept effect size**; recover a flip-rate-versus-effect-size **power curve** before trusting any real comparison |

> **Not "X notes would flip" — "X notes flip BEYOND what added flexibility alone would produce."**

**The Thurstonian answer, straight:** the model is real; `z_i` is identified from **as few as two
rankings per person** because a stable trait produces *correlated* consensus-deviation across
different prompts' loadings. `τ_i` needs **5–10**. **Gated on whether annotator_ids recur across
prompts — which the empiricist already answered: 1,012 unique annotators, 100% join.** So it is
checkable, and the reviewer still declines it, because **CN gives per-rater reliability for free** and
*"choosing the dataset that makes the hard problem disappear over the one that requires a clever
rescue of a fragile method"* is what not-over-instrumenting looks like in practice.

### Its own credibility note, which I am recording because it is the right form

*"In my first answer I gestured at the rules-vs-standards debate without naming a single source or
checking one. That gesture happened to be right. That is a sample size of one, and I should not be
treated as more reliable on unverified structural claims than the pattern above suggests anyone is —
including me, right now, on this document, which I have not run through anyone else's adversarial pass
either."*

**NEXT.** Two, and the first is the one that would have stopped four of five:
1. **Make the gate BLOCKING, not advisory** — a pre-commit hook, so an ungated absence claim cannot
   enter the history at all. *A described practice failed five times; a blocking step has not been
   tried.*
2. **Arm 3, starting with the reconciliation**: why does r04 put core **below** full while r33 puts it
   **above**, and which weighting does each use? **That contradiction is the first thing Arm 3 must
   resolve, because both numbers are currently in my ledger as evidence for opposite conclusions.**
