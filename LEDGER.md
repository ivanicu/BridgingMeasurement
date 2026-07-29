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
