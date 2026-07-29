# CODING RUBRIC — how much of the collective-alignment question does a paper actually answer?

**Written before any paper is coded.** Two ledger entries died this week because "has the field asked
X?" was answered as a **boolean** from **abstracts**. Boolean is the wrong type and abstracts are the
wrong evidence. This instrument replaces both: it codes **full texts** on **two ordered axes**, so
the output is a *matrix of coverage depth*, not a list of yes/no.

---

## The question, decomposed into a pipeline

Every collective-alignment system — Community Notes, CoVal, Polis, RLHF, jury learning — runs the
same eight stages. A paper "about collective alignment" touches some of them and is silent on the
rest, and **which** it touches is the thing nobody has counted.

| # | stage | the question it answers |
|---|---|---|
| **E1** | **ELICIT** | how is normative input got out of a person? menu, question order, abstention, whether they saw the options first |
| **E2** | **REPRESENT** | what form does *one* person's input take? ranking · criterion+weight · rating · free text · vote |
| **E3** | **AGGREGATE** | how do many become one? majority · matrix factorization · bridging · a social-choice rule |
| **E4** | **COMPILE** | how does the aggregate become machine-executable? rewriting, thresholding, fitting a model |
| **E5** | **EXECUTE** | how is it applied to a case it was not built on? judge, scorer, display decision |
| **E6** | **VALIDATE** | how do we know the output represents them? referent, ground truth, positive control |
| **E7** | **CONTEST** | what happens to someone who disagrees with the output? appeal, minority record, recourse |
| **E8** | **LEGITIMACY** | on what grounds does the output have authority over the people it came from? |

**A paper that measures spread reduction touches E5 only.** A paper that proves an aggregation rule
violates an axiom touches E3 and E8. **These are not the same contribution and must not be counted the
same way**, which is exactly what a boolean does.

---

## The depth axis — this is the part that makes it quantitative

For **each** stage a paper touches, code the **deepest** level it reaches. The levels are ordered and
a paper gets credit only for the highest it actually attains.

| level | name | test — must be answerable from the text with a page/section pointer |
|---|---|---|
| **0** | **ABSENT** | the stage is not discussed |
| **1** | **DESCRIBE** | says what the system does at this stage. No claim that it is right or wrong |
| **2** | **MEASURE** | puts a **number** on this stage's behaviour |
| **3** | **DIAGNOSE** | shows something is **wrong** here — a failure, a bias, a violated property — with evidence |
| **4** | **PRESCRIBE** | says how it **should** be done, concretely enough to implement |
| **5** | **VALIDATE** | shows the prescription **works**, against a referent stated in the paper |

**Level 5 requires a referent the paper names.** "Our method scores higher on our metric" is level 4,
not 5, unless the paper argues the metric tracks the thing it claims to fix. **This distinction is the
whole point of the instrument** — a field can be full of level-4 prescriptions and still have answered
nothing.

---

## The referent axis — coded once per paper, and it is the CoVal question

For any paper reaching level 3 or above, code **what it judged against**:

| code | referent | example |
|---|---|---|
| **N** | **non-normative** — exists in the world, no value judgment needed | retweets, timestamps, attack success, coverage counts |
| **X** | **external expert** | professional fact-checkers, expert-coded ideology scales |
| **C** | **the crowd itself**, treated as ground truth | majority label, held-out raters |
| **S** | **stated normative input from participants** | annotators' own declared moral values, written criteria |
| **A** | **axiom / formal property** | an impossibility theorem, a fairness definition, a social-choice axiom |
| **M** | **the model's own output** | undisturbed baseline, self-consistency |
| **–** | none — the paper does not reach level 3 |

**Why this axis exists:** the retracted claim was that the field only uses **N**. That was wrong (D3CODE
uses **S**, the axioms papers use **A**). **The corrected question is quantitative: what is the
DISTRIBUTION over referents, per stage?** A stage covered only by **M** and **C** referents is a stage
where the field is grading its own homework, and that is a measurable claim rather than a rhetorical
one.

---

## Coding protocol

1. **Full text only.** An abstract may not be coded. If the full text cannot be obtained, the paper is
   recorded `UNREACHABLE` and **excluded from every denominator** — never coded as 0.
2. **Pointer or it did not happen.** Every level ≥2 needs a section, figure, or table reference. A
   level assigned without one is downgraded to the highest level that has one.
3. **Code the deepest level actually attained, not the level claimed.** Papers assert contributions in
   their intro that the body does not deliver; the body decides.
4. **Independent coders.** No coder sees another's codes. **A subset is double-coded and agreement is
   reported** — self-coding by a single rater is precisely the failure mode this project studies, and
   an instrument that cannot state its own reliability may not state its results.
5. **Two positive controls, planted, and the instrument fails if it cannot separate them:**
   - a paper that should score **level 5 at E3** with referent **A** — *Axioms for AI Alignment from
     Human Feedback* proves standard rules violate axioms and constructs new ones
   - a paper that should score **level 2 at E5 only** — any difference-in-differences spread study
   **If a coder does not separate those two, that coder's codes are void**, not merely noisy.

---

## What gets computed from the codes

- **Coverage matrix** — stage × max level, over the corpus. *Where is the field deep, where is it shallow?*
- **Prescription rate** — share of papers reaching **level 4+** at each stage. *Does anyone say how to DO it?*
- **Validation rate** — share reaching **level 5**. *Does anyone show their prescription works?*
- **Referent distribution per stage** — *which stages are graded only by the crowd or the model itself?*
- **The intersection, quantified**: papers reaching **level 4 or 5** on **E1, E6, E7 or E8** — the four
  stages that carry *legitimately · stands in for · them*. **This number is the answer to "did they
  answer how to do collective alignment, or only make some measurements?"**

**Pre-registered before coding:** the expected shape is that E3 and E5 are deep (levels 4–5, many
papers) while **E1, E7 and E8 are shallow (level ≤2)**, and that E6's referents are dominated by
**N**, **C** and **M** rather than **S**. **Writing this down first is what makes a confirming result
mean anything** — and if the codes come back flat across stages, the pipeline decomposition itself is
wrong and gets retracted like the last two claims did.
