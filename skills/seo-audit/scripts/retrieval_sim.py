#!/usr/bin/env python3
"""Retrieval simulation: score page chunks against target queries with local embeddings.

Mechanics only. Interpretation thresholds and remediation guidance live in
SKILL.md and references/aeo-geo-patterns.md.

Usage:
    python retrieval_sim.py --urls urls.txt --queries queries.txt --output results.csv
    python retrieval_sim.py --urls "https://example.com/a,https://example.com/b" \
        --queries "best widget for beginners" --output results.csv

Inputs:
    --urls       Path to a file with one URL per line, or a comma-separated list.
    --queries    Path to a file with one query per line, or a comma-separated list.
    --output     Output CSV path (default: retrieval_sim_results.csv).
    --model      sentence-transformers model name (default: all-MiniLM-L6-v2).
    --max-words  Approximate words per chunk (default: 200).

Output CSV columns:
    url, query, chunk_id, heading, chunk_words, similarity, best_for_query, chunk_preview

Requires:
    pip install sentence-transformers beautifulsoup4 requests
"""

import argparse
import csv
import os
import re
import sys

import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util

USER_AGENT = "Mozilla/5.0 (compatible; retrieval-sim/1.0; SEO audit tool)"
STRIP_TAGS = ["script", "style", "noscript", "nav", "footer", "header", "aside", "form"]
BLOCK_TAGS = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "td", "th", "blockquote", "pre"]
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


def read_list_arg(value):
    """Resolve an argument that is either a file path or a comma-separated list."""
    if os.path.isfile(value):
        with open(value, encoding="utf-8") as f:
            items = [line.strip() for line in f]
    else:
        items = [item.strip() for item in value.split(",")]
    return [item for item in items if item]


def fetch_html(url):
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    return response.text


def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()


def extract_chunks(html, max_words):
    """Split a page into heading-delimited chunks of roughly max_words words."""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(STRIP_TAGS):
        tag.decompose()

    chunks = []
    current_heading = ""
    current_parts = []

    def flush():
        text = " ".join(current_parts).strip()
        if text and len(text.split()) >= 10:
            chunks.append({"heading": current_heading, "text": text})

    for element in soup.find_all(BLOCK_TAGS):
        text = clean_text(element.get_text())
        if not text:
            continue
        if element.name in HEADING_TAGS:
            flush()
            current_parts = []
            current_heading = text
        else:
            current_parts.append(text)
            if len(" ".join(current_parts).split()) >= max_words:
                flush()
                current_parts = []

    flush()
    return chunks


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--urls", required=True, help="File of URLs (one per line) or comma-separated list")
    parser.add_argument("--queries", required=True, help="File of queries (one per line) or comma-separated list")
    parser.add_argument("--output", default="retrieval_sim_results.csv", help="Output CSV path")
    parser.add_argument("--model", default="all-MiniLM-L6-v2", help="sentence-transformers model name")
    parser.add_argument("--max-words", type=int, default=200, help="Approximate words per chunk")
    args = parser.parse_args()

    urls = read_list_arg(args.urls)
    queries = read_list_arg(args.queries)
    if not urls or not queries:
        sys.exit("Error: need at least one URL and one query.")

    print(f"Loading model {args.model}...", file=sys.stderr)
    model = SentenceTransformer(args.model)
    query_embeddings = model.encode(queries, convert_to_tensor=True, normalize_embeddings=True)

    rows = []
    for url in urls:
        try:
            html = fetch_html(url)
        except requests.RequestException as exc:
            print(f"SKIP {url}: {exc}", file=sys.stderr)
            continue

        chunks = extract_chunks(html, args.max_words)
        if not chunks:
            print(f"SKIP {url}: no extractable chunks", file=sys.stderr)
            continue

        chunk_texts = [
            f"{c['heading']}. {c['text']}" if c["heading"] else c["text"] for c in chunks
        ]
        chunk_embeddings = model.encode(chunk_texts, convert_to_tensor=True, normalize_embeddings=True)
        scores = util.cos_sim(query_embeddings, chunk_embeddings)  # [queries x chunks]

        for qi, query in enumerate(queries):
            query_scores = scores[qi]
            best_chunk = int(query_scores.argmax())
            for ci, chunk in enumerate(chunks):
                rows.append({
                    "url": url,
                    "query": query,
                    "chunk_id": ci,
                    "heading": chunk["heading"],
                    "chunk_words": len(chunk["text"].split()),
                    "similarity": round(float(query_scores[ci]), 4),
                    "best_for_query": ci == best_chunk,
                    "chunk_preview": chunk["text"][:160],
                })
        print(f"OK   {url}: {len(chunks)} chunks scored against {len(queries)} queries", file=sys.stderr)

    if not rows:
        sys.exit("Error: no results produced. Check URLs and network access.")

    rows.sort(key=lambda r: (r["url"], r["query"], -r["similarity"]))
    fieldnames = ["url", "query", "chunk_id", "heading", "chunk_words", "similarity", "best_for_query", "chunk_preview"]
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
