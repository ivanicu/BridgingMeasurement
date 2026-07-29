#!/usr/bin/env python3
"""Non-arXiv literature search, built from routes that were TESTED rather than assumed.

WHY THIS FILE EXISTS
--------------------
Two field-wide negatives died in one day, and both died to venue coverage: the sweep
behind them queried only arXiv, while the killing papers sat in CHI, FAccT, NeurIPS,
EMNLP and WWW. The route list is worth more than either verdict, because venue coverage
is the binding constraint on every absence claim this project can make.

WHAT WORKS, MEASURED
--------------------
  Crossref   no key, reliable, returns DOI + venue + year for ACM / AAAI / ACL /
             NeurIPS proceedings. THE WORKHORSE.
  DBLP       works for author and topic-NAME queries. Indexes titles LITERALLY -- it
             does no semantic matching, so a stacked multi-word phrase returns 0 hits
             and that is a miss, not an error.
  arXiv      reliable, but `ti:"..."` is brittle: it fails silently on a paraphrased
             title. Use it to fetch an ABSTRACT once Crossref has given you the exact
             title, not to discover.

WHAT DOES NOT
-------------
  DuckDuckGo        anti-bot block page on html. and lite. subdomains, every query.
  Semantic Scholar  HTTP 429 without a key.
  OpenAlex          now requires payment; returns "Insufficient budget".

THE PATTERN, and it is the reusable part:
  Crossref to DISCOVER  ->  arXiv `ti:` for the ABSTRACT when a preprint exists  ->
  the DOI itself otherwise.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
import urllib.parse

UA = "bridging-measurement/0.1 (mailto:tingzen318@gmail.com)"


def get(url: str, timeout: int = 45) -> str:
    """curl rather than urllib: the box's python has no certifi story worth debugging,
    and curl is what was actually tested."""
    r = subprocess.run(["curl", "-sS", "--max-time", str(timeout), "-A", UA, url],
                       capture_output=True, text=True)
    return r.stdout


def crossref(query: str, rows: int = 20) -> list[dict]:
    """Discovery. Returns venue, which is the field arXiv cannot give you."""
    u = ("https://api.crossref.org/works?query.bibliographic="
         + urllib.parse.quote(query)
         + f"&rows={rows}&select=title,DOI,issued,container-title,type")
    try:
        items = json.loads(get(u))["message"]["items"]
    except Exception as e:
        print(f"  [crossref failed: {e}]", file=sys.stderr)
        return []
    out = []
    for it in items:
        ti = (it.get("title") or [""])[0]
        venue = (it.get("container-title") or [""])
        yr = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
        out.append({"title": ti, "doi": it.get("DOI"), "year": yr,
                    "venue": venue[0] if venue else "", "type": it.get("type", "")})
    return out


def dblp(query: str, rows: int = 30) -> list[dict]:
    """Literal title index. Short topic phrases only -- a long AND-ish phrase returns 0
    and that zero means 'no literal match', never 'nothing exists'."""
    u = (f"https://dblp.org/search/publ/api?q={urllib.parse.quote(query)}"
         f"&format=json&h={rows}")
    try:
        hits = json.loads(get(u))["result"]["hits"].get("hit", [])
    except Exception as e:
        print(f"  [dblp failed: {e}]", file=sys.stderr)
        return []
    out = []
    for h in hits:
        i = h.get("info", {})
        v = i.get("venue", "")
        out.append({"title": i.get("title", ""), "year": i.get("year"),
                    "venue": v if isinstance(v, str) else ", ".join(v),
                    "doi": i.get("doi"), "url": i.get("ee", "")})
    return out


def arxiv_abstract(exact_title: str) -> str | None:
    """Fetch an abstract for a title Crossref already gave us EXACTLY. Do not guess a
    title here -- a paraphrase returns nothing and reads as 'no preprint exists'."""
    import re
    u = ("https://export.arxiv.org/api/query?search_query=ti:"
         + urllib.parse.quote(f'"{exact_title}"') + "&max_results=1")
    x = get(u)
    m = re.search(r"<summary>(.*?)</summary>", x, re.S)
    return " ".join(m.group(1).split()) if m else None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("query")
    ap.add_argument("--rows", type=int, default=15)
    ap.add_argument("--source", choices=["crossref", "dblp", "both"], default="both")
    ap.add_argument("--abstracts", action="store_true",
                    help="fetch arXiv abstracts for exact titles found (slow: 3s/call)")
    a = ap.parse_args()

    if a.source in ("crossref", "both"):
        print(f"=== CROSSREF · {a.query}")
        for r in crossref(a.query, a.rows):
            print(f"  {str(r['year']):>4}  {r['venue'][:34]:<34} {r['title'][:76]}")
            print(f"        doi:{r['doi']}")
            if a.abstracts:
                ab = arxiv_abstract(r["title"])
                time.sleep(3)
                if ab:
                    print(f"        {ab[:300]}")
    if a.source in ("dblp", "both"):
        print(f"\n=== DBLP · {a.query}   (literal title match; 0 hits = no literal match)")
        for r in dblp(a.query, a.rows):
            print(f"  {str(r['year']):>4}  {r['venue'][:34]:<34} {r['title'][:76]}")


if __name__ == "__main__":
    main()
