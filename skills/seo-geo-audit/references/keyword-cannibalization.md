# Keyword Cannibalization Analysis

Detection methods, severity scoring, and remediation for pages competing on the same queries. See SKILL.md for when to trigger this analysis.

---

## Detection Methods, in Order of Rigor

1. **GSC query-to-page check (fastest signal)**
   - Pull GSC performance data grouped by query, then by page
   - Flag any query where 2+ URLs have impressions above a meaningful threshold (e.g., >50/month)
   - Flag queries where the top-ranking URL changes across recent date ranges
   - Use `gscServer:get_search_by_page_query` if MCP is available

2. **Title/H1 overlap check (cheap, catches obvious cases)**
   - Crawl the site and extract title tags and H1s
   - Look for near-duplicate phrasing across URLs
   - Manual review or simple string-similarity scoring (Jaccard, fuzzy match)

3. **Semantic similarity analysis (most rigorous, recommended for libraries >200 pages)**
   - Generate embeddings for each page's primary content (title + H1 + first 500 words, or full body if scoped)
   - Compute pairwise cosine similarity across the corpus
   - Flag pairs above a similarity threshold (typically 0.85+ for clear cannibalization risk; 0.70–0.85 for review)
   - Visualize as a heatmap or ranked pair list to make patterns legible
   - Cross-reference high-similarity pairs against GSC to confirm they're competing for the same queries (similarity alone isn't cannibalization — two pages can be semantically close but serve different intents)

---

## Severity Scoring

For each flagged pair, score severity using:

- **Similarity score** (semantic or query-overlap percentage)
- **Traffic stakes** (combined impressions/clicks of the competing URLs)
- **Intent alignment** (do they actually serve the same user need, or is the overlap superficial?)
- **Backlink distribution** (is authority split, or concentrated on one URL?)

A high-severity case looks like: two URLs >85% similar, both getting meaningful GSC impressions on shared queries, both targeting the same intent, with backlinks split between them.

---

## Remediation Options, by Severity

| Severity | Likely fix |
|---|---|
| High — same intent, high overlap | Consolidate: merge content, 301 the weaker URL to the stronger, update internal links |
| Medium — similar topic, distinguishable intent | Differentiate: rewrite to clarify each page's unique angle, retarget keywords, adjust internal anchor text |
| Low — surface overlap only | Monitor: tighten titles/H1s, leave structure alone |

Consolidation is usually the right call when traffic is small or evenly split. Differentiation is right when both pages have meaningful traffic from distinct queries and the overlap is fixable through editing.

---

## What to Deliver

- Ranked list of cannibalization pairs with similarity score, combined traffic, and recommended action
- For high-severity pairs: specific consolidation or differentiation plan, including target URL, redirect map if applicable, and internal link updates needed
- Heatmap or matrix visualization for libraries large enough to warrant it (>200 pages)
