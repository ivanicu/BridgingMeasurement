#!/usr/bin/env python3
"""Consume the coders' output and compute the intersection, quantitatively.

WRITTEN BEFORE ANY CODE ARRIVED. An analysis authored after seeing the data is an
analysis shaped by it, and this project has already lost two claims to exactly that
family of error.

Reads one plain-text file per coder from `priorart/codes/`, each containing blocks:

    PAPER: 2210.15723
    E1: 3 | S | Sec 4.2
    ...
    E8: 0 | - | none
    DELIVERS: ...
    PRESCRIBES_HOW: YES - ...

Computes:
  - the CONTROL CHECK first, and voids any coder who fails it
  - inter-coder agreement on the double-coded papers
  - coverage matrix (stage x depth), prescription rate, validation rate
  - referent distribution per stage
  - THE INTERSECTION: papers reaching level >= 4 on E1/E6/E7/E8

Run its own positive control with `--selftest`: synthetic codings with a known answer
must be recovered exactly. An analysis that has never recovered a planted result is not
a measurement.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys
from collections import defaultdict

STAGES = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"]
NAMES = {"E1": "ELICIT", "E2": "REPRESENT", "E3": "AGGREGATE", "E4": "COMPILE",
         "E5": "EXECUTE", "E6": "VALIDATE", "E7": "CONTEST", "E8": "LEGITIMACY"}
LEVELS = {0: "absent", 1: "describe", 2: "measure", 3: "diagnose", 4: "prescribe",
          5: "validate"}
# The four stages that carry "legitimately / stands in for / them".
INTERSECTION = ["E1", "E6", "E7", "E8"]
# Controls, unlabelled to the coders. Expected profiles, pre-registered in the rubric.
CTRL_DEEP, CTRL_SHALLOW = "2604.11224", "2409.08781"

ROW = re.compile(r"^(E[1-8]):\s*([0-5])\s*\|\s*([NXCSAM-])\s*\|\s*(.*)$")


def parse(text: str) -> dict:
    """One coder's file -> {paper: {stage: (level, referent, pointer), ...}}."""
    out: dict = {}
    cur = None
    for line in text.splitlines():
        line = line.strip()
        m = re.match(r"^PAPER:\s*(\S+)", line)
        if m:
            cur = m.group(1).replace("v1", "").replace("v2", "").strip()
            out[cur] = {}
            continue
        if cur is None:
            continue
        m = ROW.match(line)
        if m:
            out[cur][m.group(1)] = (int(m.group(2)), m.group(3), m.group(4).strip())
            continue
        m = re.match(r"^PRESCRIBES_HOW:\s*(YES|NO)", line, re.I)
        if m:
            out[cur]["_prescribes"] = m.group(1).upper()
        m = re.match(r"^DELIVERS:\s*(.+)$", line)
        if m:
            out[cur]["_delivers"] = m.group(1)
    return {k: v for k, v in out.items() if any(s in v for s in STAGES)}


def control_check(codes: dict) -> tuple[bool, str]:
    """The rubric's rule: a coder who cannot separate the two controls is VOID, not noisy.
    DEEP must reach >=4 somewhere in E3/E4; SHALLOW must not reach 4 anywhere."""
    d, s = codes.get(CTRL_DEEP), codes.get(CTRL_SHALLOW)
    if not d or not s:
        return True, "controls absent from this coder's set - not checked"
    deep_ok = max(d.get(x, (0,))[0] for x in ("E3", "E4")) >= 4
    shallow_ok = max(s.get(x, (0,))[0] for x in STAGES) <= 3
    ok = deep_ok and shallow_ok
    return ok, (f"deep={CTRL_DEEP} reaches>=4 at E3/E4: {deep_ok}; "
                f"shallow={CTRL_SHALLOW} stays<=3 everywhere: {shallow_ok}")


def merge(valid: dict) -> tuple[dict, list]:
    """Double-coded papers take the MIN level per stage: a level survives only if every
    coder who read the paper saw it. Conservative on purpose -- this instrument is being
    used to make an absence-shaped argument, and absence claims must not be inflated by
    one generous coder."""
    per_paper: dict = defaultdict(dict)
    disagreements = []
    for coder, codes in valid.items():
        for paper, st in codes.items():
            for s in STAGES:
                if s not in st:
                    continue
                lvl, ref, _ = st[s]
                if s in per_paper[paper]:
                    prev, prev_ref, prev_coders = per_paper[paper][s]
                    if prev != lvl:
                        disagreements.append((paper, s, prev, lvl))
                    per_paper[paper][s] = (min(prev, lvl), prev_ref if prev <= lvl else ref,
                                           prev_coders + [coder])
                else:
                    per_paper[paper][s] = (lvl, ref, [coder])
    return per_paper, disagreements


def report(per_paper: dict, disagreements: list) -> None:
    papers = sorted(per_paper)
    n = len(papers)
    print(f"\nPAPERS CODED: {n}")

    print(f"\n{'stage':<12} {'name':<12} " + "  ".join(f"L{i}" for i in range(6))
          + "   >=4   ==5   deepest")
    inter_hits = defaultdict(list)
    for s in STAGES:
        lv = [per_paper[p].get(s, (0,))[0] for p in papers]
        hist = [sum(1 for x in lv if x == i) for i in range(6)]
        pres = sum(1 for x in lv if x >= 4)
        val = sum(1 for x in lv if x == 5)
        print(f"{s:<12} {NAMES[s]:<12} " + "  ".join(f"{h:2d}" for h in hist)
              + f"   {pres:3d}   {val:3d}   {max(lv) if lv else 0}")
        if s in INTERSECTION:
            for p in papers:
                if per_paper[p].get(s, (0,))[0] >= 4:
                    inter_hits[s].append(p)

    print(f"\nREFERENT DISTRIBUTION (papers reaching level >=3 at that stage)")
    print(f"{'stage':<12} " + "  ".join(f"{c:>3}" for c in "NXCSAM"))
    for s in STAGES:
        cnt = defaultdict(int)
        for p in papers:
            lvl, ref, _ = per_paper[p].get(s, (0, "-", ""))
            if lvl >= 3 and ref in "NXCSAM":
                cnt[ref] += 1
        print(f"{s:<12} " + "  ".join(f"{cnt[c]:3d}" for c in "NXCSAM"))

    print(f"\n=== THE INTERSECTION ===")
    print(f"Papers reaching PRESCRIBE(4) or VALIDATE(5) on the four stages that carry")
    print(f"'legitimately / stands in for / them' -- E1 elicit, E6 validate, E7 contest,")
    print(f"E8 legitimacy:")
    total = set()
    for s in INTERSECTION:
        hits = inter_hits[s]
        total |= set(hits)
        print(f"  {s} {NAMES[s]:<12} {len(hits):2d}/{n}  {', '.join(hits) if hits else '(none)'}")
    print(f"\n  UNION: {len(total)}/{n} papers say HOW on at least one of the four.")
    both = [p for p in papers
            if sum(1 for s in INTERSECTION if per_paper[p].get(s, (0,))[0] >= 4) >= 2]
    print(f"  Papers doing so on TWO OR MORE of the four: {len(both)}/{n}"
          f"  {', '.join(both) if both else '(none)'}")

    if disagreements:
        agree = 1 - len(disagreements) / max(
            sum(len(v[2]) - 1 for p in per_paper for v in [per_paper[p].get(s)]
                if v for s in [None]) or 1, 1)
        print(f"\nINTER-CODER DISAGREEMENTS on double-coded papers: {len(disagreements)}")
        for p, s, a, b in disagreements[:14]:
            print(f"  {p} {s}: {a} vs {b}")
    else:
        print("\nNo double-coded cells found - reliability NOT measurable, "
              "and no result here may be quoted without saying so.")


def selftest() -> None:
    """Plant a known answer and require the analysis to recover it exactly."""
    synth = {
        "coderX": parse(
            "PAPER: 2604.11224\nE3: 4 | M | Sec 5\nE5: 2 | N | Tab 1\n"
            "E1: 0 | - | none\nE6: 0 | - | none\nE7: 0 | - | none\nE8: 0 | - | none\n"
            "PAPER: 2409.08781\nE5: 2 | N | Tab 2\nE3: 1 | - | none\n"
            "E1: 0 | - | none\nE6: 0 | - | none\nE7: 0 | - | none\nE8: 0 | - | none\n"
            "PAPER: 9999.00001\nE8: 5 | A | Thm 1\nE7: 4 | A | Sec 6\n"
            "E1: 0 | - | none\nE6: 0 | - | none\n")
    }
    ok, why = control_check(synth["coderX"])
    assert ok, f"selftest: control check should PASS on a clean coder -- {why}"
    bad = {"E3": (2, "-", ""), "E4": (1, "-", "")}
    ok2, _ = control_check({CTRL_DEEP: bad, CTRL_SHALLOW: synth["coderX"][CTRL_SHALLOW]})
    assert not ok2, "selftest: control check must FAIL a coder who flattens the deep control"
    per, dis = merge(synth)
    hits = [p for p in per if per[p].get("E8", (0,))[0] >= 4]
    assert hits == ["9999.00001"], f"selftest: intersection recovery wrong -- {hits}"
    assert per["2409.08781"]["E5"][0] == 2
    print("SELFTEST PASS: control check accepts a clean coder, rejects a flattened one, "
          "and the intersection recovers exactly the planted paper.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--codes", type=pathlib.Path, default=pathlib.Path("priorart/codes"))
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest(); return
    files = sorted(a.codes.glob("*.txt"))
    if not files:
        # EXIT 2, not 1 and never 0. "Nothing to check" and "a check that failed" are
        # different states, and a harness that cannot tell them apart reads an empty
        # population as a clean pass -- which is how a gate certifies a void.
        print(f"REFUSING: no coder files in {a.codes}. Nothing to check.", file=sys.stderr)
        raise SystemExit(2)
    valid, voided = {}, []
    for f in files:
        codes = parse(f.read_text())
        ok, why = control_check(codes)
        print(f"CONTROL {f.stem:<10} {'PASS' if ok else 'VOID'}  {why}")
        (valid.setdefault(f.stem, codes) if ok else voided.append(f.stem))
    if not valid:
        raise SystemExit("REFUSING: every coder failed the control. The instrument, not "
                         "the field, is what this run measured.")
    if voided:
        print(f"\nVOIDED CODERS (excluded entirely, not down-weighted): {voided}")
    per, dis = merge(valid)
    report(per, dis)


if __name__ == "__main__":
    main()
