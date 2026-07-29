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

**I had two of these kills in my own hands.** Two turns before asserting that discarded disagreement
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

**The apparatus exists. The deployed-system empirics exist. Nobody has connected them.** Measurement
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

**NEXT.** Two things, and the first is not optional:
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

**NEXT.** Two things, in order:
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
