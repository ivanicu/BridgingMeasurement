#!/usr/bin/env python3
"""Every absence claim must carry the evidence that it was checked BEFORE it was written.

WHY THIS EXISTS
---------------
Five field-wide negatives died in one week. None of them was caught by this project's
existing apparatus -- not by pre-registration, not by positive controls, not by
three-valued verdicts, not by dispatching adversaries. All five were killed by reading a
primary source or by checking output I had already produced myself.

The reviewer who diagnosed it put the mechanism precisely: a claim's own completeness and
cleanliness is what signals it is done, and a field-wide negative is a satisfying shape --
it closes a line and has the cadence of a result. That satisfaction fires BEFORE
verification is scheduled, and once fired, verification becomes something one could do
rather than something the assertion is gated on.

  Case 1 is the proof: the killing paper was already flagged in the ledger as
  "must read in full". The check was correctly located and scheduled. THE GATING DIDN'T
  HAPPEN. The failure is not retrieval -- twice the evidence was already in hand, once in
  the same context window and once in a file written by an instrument I built.

So the apparatus was real and built for the WRONG STAGE. It disciplines what happens after
one commits to running an experiment; every one of these died at the moment of assertion,
upstream of anywhere pre-registration can apply. You cannot pre-register a
literature-absence claim.

WHAT THIS GATE DOES
-------------------
An absence claim is admissible only if, in the SAME paragraph, it carries one of:

  A POINTER   an arXiv id, a DOI, or a URL -- evidence that a primary source was FETCHED,
              not queried about. (Case 2 died on five queries ABOUT a system and zero
              queries OF it.)
  A HEDGE     the claim is explicitly marked UNVERIFIED, or stated as "I did not find",
              or carries a retraction marker. This is the honest form: a field-wide
              negative is not a finding one is entitled to state, it is a question one
              hands to an adversary.

Anything else is a bare assertion and is flagged.

THE CONTROL IS TWO-SIDED, and the second half is what makes the first mean anything:
a bare claim must be flagged AND a properly gated claim must pass. A checker that flags
everything would "catch" all five failures and be useless.

SCOPE, STATED RATHER THAN IMPLIED: this is a LEXICAL gate. It cannot tell whether the
pointer actually supports the claim, only that one is present. It is the cheap decisive
check that should have run first -- not a substitute for reading. Its own constitution's
gate 6: seek the cheapest decisive failure, not the most expensive complete success.
"""
from __future__ import annotations

import pathlib
import re
import sys

DOCS = ["LEDGER.md", "README.md", "PRIOR_ART.md", "DESIGN_FOR_REVIEW.md"]

# Phrasings that assert a gap in the world rather than in our own search.
ABSENCE = re.compile(
    r"nobody (?:has|ever|had)\b|no one has\b|has never been\b|have never been\b"
    r"|never been (?:run|done|tested|measured|asked)\b|structurally absent\b"
    r"|not one (?:of |paper|study|reviewer)|no paper\b|no study\b"
    r"|does not exist anywhere\b|exists nowhere\b|there is no (?:such )?(?:paper|study|work)\b",
    re.I)

# Evidence that a primary source was fetched.
POINTER = re.compile(r"\b(?:arxiv\.org|doi\.org|10\.\d{4,}/|https?://|\d{4}\.\d{4,5})", re.I)

# Honest hedges: the claim is marked as OUR search's limit, not the world's state.
HEDGE = re.compile(
    r"UNVERIFIED|RETRACTED|⛔|I did not find|we did not find|did not find a kill"
    r"|absence-of-evidence|provisional|not a positive control|no kill found"
    r"|dead|killed|does not survive|retracted", re.I)


def paragraphs(text: str):
    """Markdown paragraphs. A table row is its own paragraph -- a claim in a cell must
    carry its own pointer, because a reader of that row does not see the one three rows up."""
    out, buf, start = [], [], 1
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("|"):
            if buf:
                out.append((start, "\n".join(buf))); buf = []
            out.append((n, line))
            start = n + 1
            continue
        if not line.strip():
            if buf:
                out.append((start, "\n".join(buf))); buf = []
            start = n + 1
        else:
            if not buf:
                start = n
            buf.append(line)
    if buf:
        out.append((start, "\n".join(buf)))
    return out


def scan(text: str):
    bare = []
    for line_no, para in paragraphs(text):
        m = ABSENCE.search(para)
        if not m:
            continue
        if POINTER.search(para) or HEDGE.search(para):
            continue
        # QUOTING an absence claim is not MAKING one. Three of this gate's first
        # fourteen hits were the killing papers' own words, or this rule's own text
        # quoting the patterns it forbids. A gate that cannot tell use from mention
        # would push its reader toward paraphrasing sources to dodge it -- the
        # opposite of what it exists to encourage.
        span = para[max(0, m.start() - 200):m.end() + 200]
        quoted = (para.lstrip().startswith(">")
                  or re.search(r'["\u201c\u2018\u201d].{0,160}' + re.escape(m.group(0)),
                               span, re.I | re.S))
        if quoted:
            continue
        bare.append((line_no, m.group(0), " ".join(para.split())[:110]))
    return bare


def control() -> bool:
    """Two-sided. Bare claim must be flagged; each gated form must pass."""
    bad = "Nobody has ever measured the compilation loss on a deployed system.\n"
    ok_ptr = "Nobody has measured this on a deployed system (arXiv 2602.08970 comes closest).\n"
    ok_hedge = "I did not find anyone measuring this; the claim is UNVERIFIED.\n"
    ok_quote = 'The reviewer wrote that "nobody has ever measured" it, which killed us.\n'
    f_bad, f_ptr = scan(bad), scan(ok_ptr)
    f_hedge, f_quote = scan(ok_hedge), scan(ok_quote)
    ok = (len(f_bad) == 1 and not f_ptr and not f_hedge and not f_quote)
    print(f"control: bare->{len(f_bad)} flagged (want 1) · pointer->{len(f_ptr)} (want 0) · "
          f"hedge->{len(f_hedge)} (want 0) · quotation->{len(f_quote)} (want 0)  "
          f"-> {'PASS' if ok else 'FAIL'}")
    return ok


def staged() -> int:
    """Scan only the lines this commit ADDS. The working-tree scan certifies a state; this
    certifies a CHANGE, which is what a commit is. Without it the gate passes forever once
    the tree is clean, and every new bare claim rides in behind an already-green check."""
    import subprocess
    d = subprocess.run(["git", "diff", "--cached", "-U0", "--", "*.md"],
                       capture_output=True, text=True).stdout
    added = "\n\n".join(l[1:] for l in d.splitlines()
                         if l.startswith("+") and not l.startswith("+++"))
    if not added.strip():
        print("no markdown lines added in this commit -- nothing to gate.")
        return 0
    bare = scan(added)
    print(f"staged markdown: {len(added.splitlines())} added lines, {len(bare)} bare "
          f"absence claim(s).")
    for _, phrase, ctx in bare:
        print(f"  BARE  [{phrase}]  {ctx}")
    if bare:
        print("\nRefusing: add the fetched primary-source pointer, or mark it UNVERIFIED.",
              file=sys.stderr)
        return 1
    return 0


def main() -> int:
    if "--staged" in sys.argv:
        return 0 if not control() else staged()
    if not control():
        print("REFUSING: the gate cannot separate a bare claim from a gated one, so it "
              "cannot certify either.", file=sys.stderr)
        return 1
    root = pathlib.Path(__file__).resolve().parents[1]
    docs = [root / d for d in DOCS if (root / d).exists()]
    if not docs:
        print("REFUSING: no documents to check. Nothing-to-check is exit 2, never a pass.",
              file=sys.stderr)
        return 2
    total, bare = 0, []
    for d in docs:
        hits = scan(d.read_text())
        n_claims = sum(1 for _, p in paragraphs(d.read_text()) if ABSENCE.search(p))
        total += n_claims
        for line_no, phrase, ctx in hits:
            bare.append((d.name, line_no, phrase, ctx))
    print(f"\n{total} absence claims across {len(docs)} documents; "
          f"{total - len(bare)} carry a pointer or a hedge, {len(bare)} are bare.")
    for name, line_no, phrase, ctx in bare:
        print(f"  BARE  {name}:{line_no}  [{phrase}]  {ctx}")
    if bare:
        print("\nA bare absence claim is not a finding one is entitled to state. Add the "
              "primary-source pointer that was fetched, or mark it UNVERIFIED and hand it "
              "to an adversary.", file=sys.stderr)
        return 1
    print("Every absence claim carries its check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
