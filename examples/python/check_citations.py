"""
check_citations.py: check whether DOIs exist, and what they belong to, using the Crossref API.

Usage:
    python examples/python/check_citations.py 10.1016/j.jpowsour.2005.01.006 10.1000/not-a-real-doi
    python examples/python/check_citations.py --file references.txt     # one DOI (or a line containing one) per line

For each DOI the script prints FOUND with the title, container (journal) and year recorded by Crossref,
or NOT FOUND. A found DOI proves that a work with that identifier exists; it does not prove that the work
says what an AI claimed (worked example 2). Open it and read it.

Requires: pip install requests
No API key needed; please be polite to the free Crossref service (the script pauses briefly between requests).
"""

import re
import sys
import time

import requests

DOI_PATTERN = re.compile(r"10\.\d{4,9}/[^\s\"'<>]+")


def extract_dois(text: str) -> list[str]:
    """Find DOI-shaped strings in text, stripping trailing punctuation."""
    return [m.rstrip(".,;)") for m in DOI_PATTERN.findall(text)]


def lookup(doi: str) -> dict | None:
    """Return Crossref metadata for a DOI, or None if it does not resolve."""
    url = f"https://api.crossref.org/works/{doi}"
    headers = {"User-Agent": "essential-ai-skills-2026 check_citations.py (mailto:wangyanwei@gmail.com)"}
    try:
        r = requests.get(url, headers=headers, timeout=15)
    except requests.RequestException as exc:
        return {"error": str(exc)}
    if r.status_code == 404:
        return None
    if r.status_code != 200:
        return {"error": f"HTTP {r.status_code} from Crossref (network blocked or rate-limited?)"}
    msg = r.json().get("message", {})
    year = None
    for key in ("published-print", "published-online", "issued"):
        parts = msg.get(key, {}).get("date-parts", [[None]])
        if parts and parts[0] and parts[0][0]:
            year = parts[0][0]
            break
    return {
        "title": (msg.get("title") or ["(no title)"])[0],
        "container": (msg.get("container-title") or ["(no container)"])[0],
        "year": year,
        "authors": ", ".join(f"{a.get('family', '')}" for a in msg.get("author", [])[:3]),
    }


def main(argv: list[str]) -> None:
    if not argv:
        sys.exit(__doc__)
    if argv[0] == "--file":
        with open(argv[1], encoding="utf-8") as f:
            dois = extract_dois(f.read())
    else:
        dois = extract_dois(" ".join(argv))
    if not dois:
        sys.exit("No DOI-shaped strings found.")
    found = 0
    for doi in dois:
        meta = lookup(doi)
        if meta is None:
            print(f"{doi:<40} NOT FOUND")
        elif "error" in meta:
            print(f"{doi:<40} ERROR     {meta['error']}")
        else:
            found += 1
            print(f"{doi:<40} FOUND     {meta['title']} ({meta['container']}, {meta['year']}; {meta['authors']})")
        time.sleep(0.5)
    print(f"\n{found} of {len(dois)} DOIs resolve. Now open each one and check that it supports the claim attached to it.")


if __name__ == "__main__":
    main(sys.argv[1:])
