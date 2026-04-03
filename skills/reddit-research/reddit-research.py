#!/usr/bin/env python3
"""
Reddit Question Research Tool
Discovers subreddits and extracts question-format content for a given topic.
Usage: python reddit_research.py "your topic" [--limit 100] [--subreddits 5]
"""

import argparse
import json
import re
import ssl
import sys
import time
import urllib.request
import urllib.parse
from collections import defaultdict, Counter

SSL_CTX = ssl.create_default_context()
try:
    import certifi
    SSL_CTX.load_verify_locations(certifi.where())
except ImportError:
    SSL_CTX.check_hostname = False
    SSL_CTX.verify_mode = ssl.CERT_NONE


HEADERS = {
    "User-Agent": "RedditResearch/1.0 (content research tool)"
}


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10, context=SSL_CTX) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"  [warn] fetch failed for {url}: {e}", file=sys.stderr)
        return {}


def discover_subreddits(topic: str, max_results: int = 8) -> list[dict]:
    """Find the most relevant subreddits for a topic."""
    encoded = urllib.parse.quote(topic)
    url = f"https://www.reddit.com/subreddits/search.json?q={encoded}&limit=20"
    data = fetch(url)

    subs = []
    for child in data.get("data", {}).get("children", []):
        s = child.get("data", {})
        subs.append({
            "name": s.get("display_name", ""),
            "title": s.get("title", ""),
            "subscribers": s.get("subscribers") or 0,
            "description": (s.get("public_description", "") or "")[:120],
        })

    # Sort by subscriber count, take top N
    subs = sorted(subs, key=lambda x: x["subscribers"], reverse=True)
    return subs[:max_results]


def fetch_posts(subreddit: str, topic: str, limit: int = 100) -> list[dict]:
    """Fetch top posts from a subreddit, filtered loosely by topic relevance."""
    encoded_topic = urllib.parse.quote(topic)
    url = f"https://www.reddit.com/r/{subreddit}/search.json?q={encoded_topic}&sort=top&t=year&limit={limit}&restrict_sr=1"
    data = fetch(url)
    time.sleep(0.5)  # be polite

    posts = []
    for child in data.get("data", {}).get("children", []):
        p = child.get("data", {})
        posts.append({
            "title": p.get("title", ""),
            "score": p.get("score", 0),
            "num_comments": p.get("num_comments", 0),
            "url": p.get("url", ""),
            "subreddit": subreddit,
        })
    return posts


def fetch_global_search(topic: str, limit: int = 100) -> list[dict]:
    """Search across all of Reddit for a topic."""
    encoded = urllib.parse.quote(topic)
    url = f"https://www.reddit.com/search.json?q={encoded}&sort=top&t=year&limit={limit}"
    data = fetch(url)

    posts = []
    for child in data.get("data", {}).get("children", []):
        p = child.get("data", {})
        posts.append({
            "title": p.get("title", ""),
            "score": p.get("score", 0),
            "num_comments": p.get("num_comments", 0),
            "url": p.get("url", ""),
            "subreddit": p.get("subreddit", ""),
        })
    return posts


def is_question(text: str) -> bool:
    """Detect question-format titles."""
    text = text.strip()
    question_words = r"^(what|how|why|when|where|who|which|is|are|can|could|should|do|does|did|has|have|will|would|any|best|anyone|has anyone|has anyone else|anyone else)"
    return bool(
        text.endswith("?") or
        re.match(question_words, text, re.IGNORECASE)
    )


def normalize_question(text: str) -> str:
    """Light normalization for deduplication."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def cluster_questions(questions: list[dict]) -> dict[str, list[dict]]:
    """Simple keyword-based clustering."""
    clusters = defaultdict(list)

    # Common theme keywords to cluster around
    theme_keywords = [
        ("getting started", ["beginner", "start", "new to", "learn", "basics", "intro", "first"]),
        ("best practices", ["best", "better", "should i", "recommend", "right way", "correct"]),
        ("comparison", ["vs", "versus", "difference", "compare", "or ", "which is"]),
        ("troubleshooting", ["not working", "problem", "issue", "error", "wrong", "broken", "fix", "help"]),
        ("how-to", ["how to", "how do", "how can", "how does", "how did"]),
        ("cost / roi", ["worth", "cost", "price", "pay", "free", "roi", "value", "expensive"]),
        ("tools / resources", ["tool", "software", "plugin", "resource", "app", "platform"]),
        ("results / outcomes", ["result", "work", "success", "fail", "effective", "actually"]),
    ]

    unclustered = []
    for q in questions:
        title_lower = q["title"].lower()
        matched = False
        for theme, keywords in theme_keywords:
            if any(kw in title_lower for kw in keywords):
                clusters[theme].append(q)
                matched = True
                break
        if not matched:
            unclustered.append(q)

    if unclustered:
        clusters["other questions"] = unclustered

    return dict(clusters)


def deduplicate(questions: list[dict]) -> list[dict]:
    """Remove near-duplicate questions."""
    seen = set()
    unique = []
    for q in questions:
        norm = normalize_question(q["title"])
        # Simple dedup: skip if first 6 words match something we've seen
        key = " ".join(norm.split()[:6])
        if key not in seen:
            seen.add(key)
            unique.append(q)
    return unique


def format_report(topic: str, subreddits: list[dict], clusters: dict[str, list[dict]], all_posts: list[dict]) -> str:
    lines = []
    lines.append(f"# Reddit Question Research: {topic}")
    lines.append(f"\n**Total posts analyzed:** {len(all_posts)}")
    lines.append(f"**Questions extracted:** {sum(len(v) for v in clusters.values())}")

    lines.append("\n---\n")
    lines.append("## Subreddits Searched\n")
    for s in subreddits:
        lines.append(f"- **r/{s['name']}** ({s['subscribers']:,} subscribers) — {s['description']}")

    lines.append("\n---\n")
    lines.append("## Questions by Theme\n")
    lines.append("*Use these to model prompts, identify content gaps, and plan FAQ/pillar content.*\n")

    for theme, questions in sorted(clusters.items(), key=lambda x: -len(x[1])):
        lines.append(f"### {theme.title()} ({len(questions)} questions)\n")
        # Sort by score + comment engagement
        sorted_q = sorted(questions, key=lambda x: x["score"] + x["num_comments"] * 2, reverse=True)
        for q in sorted_q[:15]:  # cap at 15 per cluster
            engagement = q["score"] + q["num_comments"]
            lines.append(f"- {q['title']}  *(r/{q['subreddit']}, {engagement} engagement)*")
        lines.append("")

    lines.append("---\n")
    lines.append("## Top Questions by Engagement\n")
    lines.append("*Highest signal questions across all themes.*\n")
    all_questions = [q for qs in clusters.values() for q in qs]
    top = sorted(all_questions, key=lambda x: x["score"] + x["num_comments"] * 2, reverse=True)[:20]
    for i, q in enumerate(top, 1):
        lines.append(f"{i}. **{q['title']}**  *(r/{q['subreddit']})*")

    lines.append("\n---\n")
    lines.append("## Content & Prompt Modeling Notes\n")
    lines.append("*Suggested angles based on question patterns:*\n")

    # Auto-generate some content notes based on cluster sizes
    biggest = sorted(clusters.items(), key=lambda x: -len(x[1]))[:3]
    for theme, qs in biggest:
        lines.append(f"- **{theme.title()}** is the highest-volume theme ({len(qs)} questions) — strong candidate for pillar content or FAQ section")

    lines.append("\n*Use the clustered questions above as:*")
    lines.append("- Prompt templates: 'Answer this as if responding to: [question]'")
    lines.append("- Content briefs: each cluster = one content pillar")
    lines.append("- FAQ sections: top engagement questions are highest priority")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Research questions asked about a topic on Reddit")
    parser.add_argument("topic", help="Topic to research")
    parser.add_argument("--limit", type=int, default=100, help="Posts per subreddit (default: 100)")
    parser.add_argument("--subreddits", type=int, default=5, help="Number of subreddits to search (default: 5)")
    parser.add_argument("--output", default="reddit_research.md", help="Output file (default: reddit_research.md)")
    args = parser.parse_args()

    topic = args.topic
    print(f"\n🔍 Researching: '{topic}'")

    # Step 1: Discover subreddits
    print("\n📡 Discovering subreddits...")
    subreddits = discover_subreddits(topic, max_results=args.subreddits)
    for s in subreddits:
        print(f"  r/{s['name']} ({s['subscribers']:,} subscribers)")

    # Step 2: Global search
    print(f"\n🌐 Running global Reddit search...")
    all_posts = fetch_global_search(topic, limit=args.limit)
    print(f"  Found {len(all_posts)} posts globally")

    # Step 3: Per-subreddit search
    for s in subreddits:
        print(f"  Searching r/{s['name']}...")
        posts = fetch_posts(s["name"], topic, limit=args.limit)
        all_posts.extend(posts)
        print(f"    +{len(posts)} posts")

    # Step 4: Extract questions
    print(f"\n❓ Extracting questions from {len(all_posts)} posts...")
    questions = [p for p in all_posts if is_question(p["title"])]
    questions = deduplicate(questions)
    print(f"  {len(questions)} unique questions found")

    # Step 5: Cluster
    print("\n🗂  Clustering by theme...")
    clusters = cluster_questions(questions)
    for theme, qs in sorted(clusters.items(), key=lambda x: -len(x[1])):
        print(f"  {theme}: {len(qs)} questions")

    # Step 6: Report
    report = format_report(topic, subreddits, clusters, all_posts)

    with open(args.output, "w") as f:
        f.write(report)

    print(f"\n✅ Report written to: {args.output}")
    print(f"   {len(questions)} questions across {len(clusters)} themes")


if __name__ == "__main__":
    main()