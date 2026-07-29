#!/usr/bin/env python3
"""Attacks on `thresholds_are_justified.py`. A lock never attacked is a lock never tested.

Six evasions, each with the outcome it SHOULD produce. Four of the six worked against the first
build, and all four were one move: bind the literal to a name and it vanishes from the comparison.
The gate now resolves names, tuple unpacking, dict values and constant arithmetic back to numbers.

A6 is the one that is SUPPOSED to pass. `CFG = {"bar": 0.90}` compared as `CFG["bar"]` is an
uppercase binding with a named key -- greppable, pre-registerable, and appearing in a claim card.
That is exactly what the NAMED class exists to reward, so a gate that flagged it would be punishing
the fix it asks for. Recording the expectation here rather than letting a future reader see "EVADES"
and try to close a hole that is the design.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from thresholds_are_justified import classify  # noqa: E402

# (source, should_be_flagged)
ATTACKS = {
    "A1 lowercase local constant":  ("thr = 0.90\nchi = 0.5\nif chi > thr:\n    print('PASS')\n",
                                     True),
    "A2 arithmetic expression":     ("chi = 0.5\nif chi > 9/10:\n    print('PASS')\n", True),
    "A3 tuple-unpacked":            ("lo, hi = 0.35, 0.65\nx = 0.5\nif x > hi:\n"
                                     "    print('PASS')\n", True),
    "A4 numpy where":               ("import numpy as np\nv = np.where(x > 0.90, 1, 0)\n"
                                     "print('PASS', v)\n", True),
    "A5 negated form":              ("x = 0.5\nif not x <= 0.90:\n    print('PASS')\n", True),
    "A6 uppercase dict config":     ("CFG = {'bar': 0.90}\nif x > CFG['bar']:\n"
                                     "    print('PASS')\n", False),
}


def main() -> int:
    bad = 0
    for name, (src, want_flag) in ATTACKS.items():
        rows = classify(src) or []
        subs = [r for r in rows if r[1] == "SUBSTANTIVE"]
        flagged = any(not r[2] for r in subs)
        ok = flagged == want_flag
        bad += not ok
        print(f"  {name:<28} flagged={str(flagged):<5} want={str(want_flag):<5} "
              f"{'ok' if ok else 'REGRESSION'}   classes={[r[1] for r in rows]}")
    print(f"\n{len(ATTACKS) - bad} of {len(ATTACKS)} attacks behave as specified.")
    if bad:
        print("A regression here means the gate stopped catching a class it once caught, or "
              "started punishing the named form it asks for.", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
