#!/usr/bin/env python3
"""A green reproducibility gate certified an artifact its own code no longer produces.

WHY THIS EXISTS
---------------
Ledger entry 24. A round was patched after it ran, then gated, then committed without regenerating
its output. So the persisted json lacked a key the committed code emits, and the ledger quoted a
positive-control value (+0.2991) that appears in NO output of the committed file -- the real value is
0.3006319, and it had moved because a patch added an `rng.permutation` upstream of the planted noise.
A number I had watched print became false when I edited code above it, and nothing connected the two.

The two-hashseed reproducibility gate cannot see this, and the reason is structural rather than an
oversight: it runs the file twice and compares the two fresh runs TO EACH OTHER. Both agree perfectly.
Neither is ever compared to what is on disk. So the gate certifies DETERMINISM, not CURRENCY, and a
stale artifact passes it forever. I had been reading one green check as both properties.

THE CHEAP FIX, and it is O(1) rather than a rerun
-------------------------------------------------
A round stamps the sha256 of its own source into its output. This gate then reads every artifact and
asks whether the recorded hash equals the CURRENT hash of the file that claims to have produced it.
No reruns, no compute -- which matters, because a gate that costs minutes per round is a gate that
gets skipped, and the whole failure being fixed here is a gate not running.

THREE-VALUED, and this is the part that must not be collapsed
-------------------------------------------------------------
  MATCHES     the artifact records a hash and it equals the current source. Fresh.
  STALE       records a hash and it does NOT match. The artifact predates the code. FAIL.
  UNVERIFIED  records no hash at all -- every round written before this gate existed. This is NOT a
              pass. The artifact may be fresh or stale and this instrument cannot tell. Folding
              UNVERIFIED into MATCHES would manufacture 109 false certifications, and a false
              acquittal is permanent because nobody re-examines a cleared claim.

WHAT IT CANNOT DO, stated rather than left to be discovered
----------------------------------------------------------
It tracks the CODE, not the DATA. If an input file changes and the code does not, the artifact is
stale and this gate says MATCHES. It also cannot detect deliberate forgery -- a hand-edited hash
passes -- but forgery is not the accident class this exists for. And a round that stamps the hash of
some other file would pass; `stamp()` takes `__file__` to make that the awkward path rather than the
easy one.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys

STAMP_KEY = "source_sha256"


def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stamp(source_file: str) -> dict:
    """Rounds merge this into their output dict: `**stamp(__file__)`.

    Called with __file__ so the natural way to use it is also the correct one. A round that wanted
    to stamp a different file's hash would have to say so explicitly, which is the point."""
    p = pathlib.Path(source_file).resolve()
    return {STAMP_KEY: sha(p), "source_name": p.name}


def audit(round_dirs):
    rows = []
    for d in round_dirs:
        src = d / "run.py"
        if not src.exists():
            continue
        res = sorted((d / "results").glob("*.json")) if (d / "results").is_dir() else []
        if not res:
            rows.append((d.name, "NO-ARTIFACT", ""))
            continue
        cur = sha(src)
        for r in res:
            try:
                obj = json.loads(r.read_text())
            except (json.JSONDecodeError, UnicodeDecodeError):
                rows.append((d.name, "UNREADABLE", r.name))
                continue
            got = obj.get(STAMP_KEY) if isinstance(obj, dict) else None
            if got is None:
                rows.append((d.name, "UNVERIFIED", r.name))
            elif got == cur:
                rows.append((d.name, "MATCHES", r.name))
            else:
                rows.append((d.name, "STALE", f"{r.name} recorded {got[:12]} vs {cur[:12]}"))
    return rows


def control(tmp: pathlib.Path) -> bool:
    """Two-sided AND three-valued: a matching stamp passes, a mutated source goes STALE, and an
    unstamped artifact comes back UNVERIFIED rather than either."""
    d = tmp / "r00_control"
    (d / "results").mkdir(parents=True, exist_ok=True)
    src = d / "run.py"
    src.write_text("print('hello')\n")
    (d / "results" / "fresh.json").write_text(json.dumps(stamp(str(src))))
    (d / "results" / "unstamped.json").write_text(json.dumps({"beta": 1.0}))
    got = {name: kind for _r, kind, name in
           ((r[0], r[1], r[2].split()[0]) for r in audit([d]))}
    ok_fresh = got.get("fresh.json") == "MATCHES"
    ok_unst = got.get("unstamped.json") == "UNVERIFIED"
    src.write_text("print('hello')  # edited after the artifact was written\n")
    got2 = {name: kind for _r, kind, name in
            ((r[0], r[1], r[2].split()[0]) for r in audit([d]))}
    ok_stale = got2.get("fresh.json") == "STALE"
    ok = ok_fresh and ok_unst and ok_stale
    print(f"control: fresh->{got.get('fresh.json')} · unstamped->{got.get('unstamped.json')} · "
          f"after-edit->{got2.get('fresh.json')}  -> {'PASS' if ok else 'FAIL'}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("rounds_root")
    ap.add_argument("--tmp", default="/tmp")
    args = ap.parse_args()

    tmp = pathlib.Path(args.tmp) / "artifact_gate_control"
    if not control(tmp):
        print("REFUSING: the gate cannot separate a fresh artifact from a stale one, so it cannot "
              "certify either.", file=sys.stderr)
        return 1

    root = pathlib.Path(args.rounds_root)
    dirs = sorted((p for p in root.iterdir() if p.is_dir()), key=lambda p: p.name)
    if not dirs:
        print(f"REFUSING: no round directories under {root}. Nothing-to-check is exit 2, never a "
              f"pass.", file=sys.stderr)
        return 2
    rows = audit(dirs)
    counts: dict = {}
    for _d, kind, _n in rows:
        counts[kind] = counts.get(kind, 0) + 1
    # "directories", not "rounds": the walk includes anything under the root, and one of them is a
    # __pycache__ with no run.py. Calling 114 directories 114 rounds is a small false number and
    # this file exists because of small false numbers.
    print(f"\n{len(dirs)} directories, {len(rows)} artifacts:")
    for k in ("MATCHES", "STALE", "UNVERIFIED", "NO-ARTIFACT", "UNREADABLE"):
        if k in counts:
            print(f"  {k:<12}{counts[k]:>4}")
    for d, kind, n in rows:
        if kind == "STALE":
            print(f"    STALE  {d}/{n}")
    if counts.get("UNVERIFIED"):
        print(f"\n  {counts['UNVERIFIED']} artifacts carry no stamp. That is UNVERIFIED, not a pass: "
              f"this instrument cannot tell whether they are current. Rounds written before the "
              f"stamp existed are expected here, and calling them fresh would manufacture "
              f"{counts['UNVERIFIED']} false certifications.")
    if counts.get("STALE"):
        print("\nA stale artifact is a number nobody can reproduce from the code that claims to "
              "produce it. Rerun the round and commit the output with the source.", file=sys.stderr)
        return 1
    print("\nNo artifact contradicts the source that claims to have produced it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
