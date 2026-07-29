#!/usr/bin/env python3
"""A hand-written threshold is a hand-written conclusion. This finds the ones nobody justified.

WHY THIS EXISTS
---------------
Ledger entry 19: a script printed "consistent with balance" on a chi-square of 52.1 with 3 df,
p = 2.85e-11, because the author had written `if chi > 100` with no reason. The number was invented,
it sat in the verdict position, and every downstream reader inherited a conclusion that the data
contradicted by nine orders of magnitude.

Nothing in the existing apparatus could catch that. Pre-registration does not apply -- the threshold
WAS in the pre-registered script. Positive controls do not apply -- the instrument worked fine.
Three-valued verdicts do not apply -- the verdict was printed as CONFIRMED, not UNVERIFIED. The
adversary reviews the DESIGN and the RESULT, and this is neither: it is a constant in the middle of
working code, which reads as implementation detail and is in fact the finding.

WHAT IT SEPARATES, because most literal thresholds are FINE
-----------------------------------------------------------
  MIN_SAMPLE  a bound on a COUNT -- `len(xs) < 30`, `m.sum() < 200`, `len(both) >= 30`. It
              decides whether to SPEAK, not what to conclude: on the wrong side the code
              withholds, and withholding is the safe direction, so an unjustified count bound
              cannot manufacture a verdict. BOTH polarities count: `len(x) >= 20` and
              `len(x) < 20` are the same guard written from opposite ends, and the first
              version of this file only caught the second.
  CONVENTION  compared against 0.05 or 0.01. A significance level is a shared convention with a
              literature behind it, not a number this author invented. Flagging it would bury the
              invented ones -- though note the standing discipline still requires significance and
              equivalence to be reported separately, which this gate cannot check.
  CHANCE      compared against 0.5 or 0.25 -- the chance rate of a pairwise comparison and of a
              four-way top-rank in this corpus. Structural, not chosen.
  DESCRIPTIVE the comparison sits inside an f-string or a persisted dict: it REPORTS a share
              rather than gating a conclusion.
  TOLERANCE   comparator within 1e-3 of zero, or an exact == 0. A drift check, a
              bit-identity assertion, a convergence bound. The number is not a scientific
              claim; it is a statement about floating point. Admissible without argument.
  RECOVERY    the surrounding lines mention a planted value, a positive control, or a
              recovery target. The threshold's reference is known BY CONSTRUCTION because
              the author put the signal there. Admissible.
  SUBSTANTIVE everything else: a bar on an accuracy, a correlation, a share, a z-score, a
              count. THIS is the entry-19 class, and it is admissible only if the number
              carries its provenance.

ADMISSIBILITY FOR A SUBSTANTIVE THRESHOLD -- one of:
  NAMED       compared against an UPPERCASE module-level constant. A named constant is
              greppable, appears in the claim card, and can be pre-registered. `chi > 100`
              cannot; `chi > CHI_KILL` can.
  JUSTIFIED   a comment within two lines giving provenance: "pre-registered", "because",
              "from <source>", a chance rate, a citation, a df, a distribution.

THE CONTROL IS TWO-SIDED, and the second half is what makes the first mean anything: a bare
substantive threshold must be flagged AND a named or justified one must pass. A checker that
flagged every literal would "catch" entry 19 and be useless.

  |X| AND THAT IS WHAT THE FIRST VERSION OF THIS FILE DID -- 196 of 216 substantive comparisons
  flagged, 91%, across 109 scripts. Its two-sided control PASSED, because the control's five cases
  were ones I INVENTED. A hand-written population turns an objective check into a self-report: I
  could only test the confusions I had already thought of, and the corpus immediately supplied four
  classes I had not -- count floors, structural chance rates, descriptive f-strings, and the
  minimum-n a correlation needs. So the gate now REFUSES when it flags more than a third of what it
  classifies, because a gate with a 91% flag rate does not identify the entry-19 threshold, it
  buries it among 195 innocents.

SCOPE, STATED RATHER THAN IMPLIED. This is a STRUCTURAL gate. It cannot tell whether a
justification is *true* -- only that one is present and that the number is not anonymous. It is the
cheap decisive check that should have run first, not a substitute for reading.

ATTACKED, because a lock never attacked is a lock never tested. Six evasions were written and run;
FOUR of them worked on the first build, and all four were the same move -- bind the literal to a
name, and the literal disappears from the comparison:

  A1 `thr = 0.90; if chi > thr`        EVADED -> now resolved through a symbol table
  A2 `if chi > 9/10`                   EVADED -> now folded through ast.literal_eval
  A3 `lo, hi = 0.35, 0.65; if x > hi`  EVADED -> now resolved through tuple unpacking
  A6 `CFG = {"bar": 0.90}; x > CFG[..]` EVADED -> now resolved, and ADMISSIBLE: an uppercase config
                                        with a named key is greppable and pre-registerable, which
                                        is the whole point of the NAMED class
  A4 `np.where(x > 0.90, 1, 0)`        caught from the start
  A5 `if not x <= 0.90`                caught from the start

WHAT STILL EVADES, stated rather than left for someone to discover: a threshold assembled at
runtime, read from a file or an environment variable, or computed from data. Those are outside a
static gate by construction. And it cannot tell whether a justification is TRUE -- only that one is
present and the number is not anonymous.
"""
from __future__ import annotations

import argparse
import ast
import pathlib
import re
import sys

TOLERANCE_MAX = 1e-3
# Pre-registered: refuse above this flag share rather than emit an unusable list. Noise in the
# verdict position is the very thing this file exists to catch.
MAX_FLAG_SHARE = 0.34
CHANCE_RATES = (0.5, 0.25)
CONVENTIONAL_ALPHA = (0.05, 0.01)
COUNTISH = {"n", "m", "k", "count", "size", "nobs", "n_pairs", "reps", "draws"}
RECOVERY = re.compile(r"plant|positive control|recover|by construction|plausib|drift|"
                      r"bit-identical|byte-identical|converge|rebuild control", re.I)
JUSTIFIED = re.compile(r"pre-?registered|because|chance|marginal|from the (?:paper|literature|"
                       r"ledger|release)|per the|\bdf\b|binomial|distribution|Bonferroni|"
                       r"\bcited\b|arXiv|doi|floor|not tuned", re.I)
# Small ints are loop guards, minimum-sample checks and index arithmetic, not scientific bars.
TRIVIAL_INT = 2


def module_constants(tree: ast.Module) -> set:
    out = set()
    for n in tree.body:                     # module level only: a local is not pre-registerable
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name) and t.id.isupper():
                    out.add(t.id)
    return out


def numeric_bindings(tree: ast.Module) -> dict:
    """Every name bound to a numeric literal, anywhere, including tuple unpacking and dict values.
    Four of six attacks on this gate worked by binding the literal to a name first, so a comparison
    against a NAME must be resolved back to its number or the gate is blind to its own class."""
    out: dict = {}
    for n in ast.walk(tree):
        if not isinstance(n, ast.Assign):
            continue
        for t in n.targets:
            if isinstance(t, ast.Name):
                v = _fold(n.value)
                if v is not None:
                    out[t.id] = v
                elif isinstance(n.value, ast.Dict):
                    for k, dv in zip(n.value.keys, n.value.values):
                        fv = _fold(dv)
                        if isinstance(k, ast.Constant) and fv is not None:
                            out[f"{t.id}[{k.value!r}]"] = fv
            elif isinstance(t, ast.Tuple) and isinstance(n.value, ast.Tuple):
                for tt, vv in zip(t.elts, n.value.elts):
                    if isinstance(tt, ast.Name):
                        fv = _fold(vv)
                        if fv is not None:
                            out[tt.id] = fv
    return out


def _fold(node):
    """A numeric literal, or an arithmetic expression of literals. `9/10` is a threshold."""
    try:
        v = ast.literal_eval(node)
    except (ValueError, TypeError, SyntaxError, MemoryError):
        try:
            v = eval(compile(ast.Expression(node), "<fold>", "eval"), {"__builtins__": {}}, {})
        except Exception:
            return None
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def _resolve(node, binds):
    """-> (value, name_or_None). The name is returned so NAMED admissibility can look at its case."""
    v = _fold(node)
    if v is not None:
        return v, None
    if isinstance(node, ast.Name) and node.id in binds:
        return binds[node.id], node.id
    if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) \
            and isinstance(node.slice, ast.Constant):
        key = f"{node.value.id}[{node.slice.value!r}]"
        if key in binds:
            return binds[key], node.value.id
    return None, None


def _is_count(node) -> bool:
    """len(x) / x.sum() / x.size / a count-named variable."""
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Name) and f.id in ("len", "sum"):
            return True
        if isinstance(f, ast.Attribute) and f.attr in ("sum", "size", "count", "nnz"):
            return True
    if isinstance(node, ast.Attribute) and node.attr in ("size", "shape"):
        return True
    if isinstance(node, ast.Name) and node.id.lower() in COUNTISH:
        return True
    # d["n"] / s["count"] -- a count read out of a record is still a count.
    if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Constant) \
            and str(node.slice.value).lower() in COUNTISH:
        return True
    return False


def classify(src: str):
    """-> list of (lineno, kind, admissible, code). Never raises on unparseable input."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    lines = src.splitlines()
    consts = module_constants(tree)
    binds = numeric_bindings(tree)
    # A Compare inside an f-string or a dict literal is REPORTING, not gating.
    reporting = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.JoinedStr, ast.Dict)):
            for d in ast.walk(n):
                if isinstance(d, ast.Compare):
                    reporting.add(id(d))
    out = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Compare):
            continue
        for c in n.comparators:
            v, via = _resolve(c, binds)
            if v is None:
                continue
            if via is not None and via.isupper():
                consts = consts | {via}      # an uppercase binding is NAMED wherever it was bound
            if isinstance(v, int) and abs(v) <= TRIVIAL_INT:
                continue
            ln = n.lineno
            ctx = "\n".join(lines[max(0, ln - 3):min(len(lines), ln + 2)])
            if abs(v) <= TOLERANCE_MAX:
                kind, ok = "TOLERANCE", True
            elif id(n) in reporting:
                kind, ok = "DESCRIPTIVE", True
            elif v in CHANCE_RATES:
                kind, ok = "CHANCE", True
            elif v in CONVENTIONAL_ALPHA:
                kind, ok = "CONVENTION", True
            elif _is_count(n.left):
                kind, ok = "MIN_SAMPLE", True
            elif RECOVERY.search(ctx):
                kind, ok = "RECOVERY", True
            else:
                named = (via is not None and via in consts) or any(
                    isinstance(x, ast.Name) and x.id in consts
                    for x in [n.left] + list(n.comparators))
                just = JUSTIFIED.search(ctx) is not None
                kind = "SUBSTANTIVE"
                ok = named or just
            out.append((ln, kind, ok, lines[ln - 1].strip()[:100]))
    return out


def control() -> bool:
    """Two-sided, and the negative half is the point: a gate that flags everything is useless."""
    cases = {
        "bare substantive": ("chi = 52.1\nif chi > 100:\n    print('consistent with balance')\n",
                             False),
        "named constant": ("CHI_KILL = 100\nchi = 52.1\nif chi > CHI_KILL:\n    print('PASS')\n",
                           True),
        "justified inline": ("chi = 52.1\n# pre-registered, 3 df\nif chi > 100:\n"
                             "    print('PASS')\n", True),
        "tolerance": ("d = 1e-16\nif d > 1e-15:\n    print('FAIL drift')\n", True),
        "recovery": ("# planted 0.30, must recover\nif abs(b - 0.30) > 0.05:\n"
                     "    print('FAIL')\n", True),
    }
    ok = True
    bits = []
    for name, (src, want_admissible) in cases.items():
        rows = classify(src)
        subs = [r for r in rows if r[1] == "SUBSTANTIVE"] or rows
        got = all(r[2] for r in subs) if subs else True
        bits.append(f"{name}->{'ok' if got == want_admissible else 'WRONG'}")
        ok &= (got == want_admissible)
    print("control: " + " · ".join(bits) + f"  -> {'PASS' if ok else 'FAIL'}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="*", default=["."])
    ap.add_argument("--glob", default="**/run.py")
    ap.add_argument("--staged", action="store_true",
                    help="scan only the .py files staged for commit, so the gate certifies a "
                         "CHANGE rather than a state. Without it, a clean tree passes forever and "
                         "every new anonymous threshold rides in behind an already-green check.")
    args = ap.parse_args()

    if not control():
        print("REFUSING: the gate cannot separate a bare threshold from a justified one, so it "
              "cannot certify either.", file=sys.stderr)
        return 1

    if args.staged:
        import subprocess
        out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
                             capture_output=True, text=True).stdout
        files = [pathlib.Path(x) for x in out.split()
                 if x.endswith(".py") and pathlib.Path(x).exists()]
        if not files:
            print("no python files staged -- nothing to gate.")
            return 0
    else:
        files = []
        for r in args.roots:
            files.extend(sorted(pathlib.Path(r).glob(args.glob)))
    if not files:
        print(f"REFUSING: no files matched {args.glob} under {args.roots}. "
              f"Nothing-to-check is exit 2, never a pass.", file=sys.stderr)
        return 2

    tally = {"TOLERANCE": 0, "DESCRIPTIVE": 0, "CHANCE": 0, "CONVENTION": 0,
             "MIN_SAMPLE": 0, "RECOVERY": 0, "SUBSTANTIVE": 0}
    bare = []
    unparseable = 0
    for f in files:
        rows = classify(f.read_text())
        if rows is None:
            unparseable += 1
            continue
        for ln, kind, ok, code in rows:
            tally[kind] += 1
            if kind == "SUBSTANTIVE" and not ok:
                bare.append((str(f), ln, code))
    total = sum(tally.values())
    print(f"\n{len(files)} scripts, {unparseable} unparseable, {total} literal-threshold "
          f"comparisons:")
    for k, why in (("TOLERANCE", "drift / bit-identity / convergence"),
                   ("DESCRIPTIVE", "in an f-string or persisted dict: reports, gates nothing"),
                   ("CHANCE", "0.5 pairwise / 0.25 four-way: structural, not chosen"),
                   ("CONVENTION", "0.05 / 0.01: a shared significance level, not invented here"),
                   ("MIN_SAMPLE", "a bound on a count: withholds rather than concludes"),
                   ("RECOVERY", "reference known by construction")):
        print(f"  {k:<12}{tally[k]:>4}  ({why})")
    print(f"  {'SUBSTANTIVE':<12}{tally['SUBSTANTIVE']:>4}  of which {len(bare)} are ANONYMOUS")
    share = len(bare) / max(total, 1)
    if share > MAX_FLAG_SHARE and total >= 50 and not args.staged:
        print(f"\nREFUSING: {share:.0%} of all classified comparisons flagged, above the "
              f"pre-registered {MAX_FLAG_SHARE:.0%}. A gate this noisy does not identify the "
              f"entry-19 threshold, it buries it. Add the missing class before trusting any row.",
              file=sys.stderr)
        return 1
    for f, ln, code in bare:
        print(f"    BARE  {f}:{ln}  {code}")
    if bare:
        print("\nA substantive threshold decides a verdict. Name it as an UPPERCASE constant so it "
              "can be pre-registered and grepped, or state its provenance in a comment beside it. "
              "`chi > 100` printed 'consistent with balance' on p = 2.85e-11.", file=sys.stderr)
        return 1
    print("Every substantive threshold is named or justified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
