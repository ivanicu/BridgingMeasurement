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
