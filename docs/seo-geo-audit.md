# SEO/GEO Audit Skill: Usage Guide

The `seo-geo-audit` skill runs a structured audit of a site's traditional SEO health and its visibility to AI search systems (ChatGPT, Claude, Perplexity, Google AI Overviews). It covers crawlability, indexation, on-page optimization, content quality, keyword cannibalization, AI crawler readiness, and chunk-level retrieval testing.

This guide explains what to have ready before you invoke the skill, and how to use the bundled retrieval simulation script.

## Installation

Copy the `skills/seo-geo-audit/` folder (or unzip `skills/seo-geo-audit.zip`) into your Claude skills directory — typically `~/.claude/skills/` for Claude Code.

## What to Provide When Invoking the Skill

The audit is only as good as its inputs. Have these ready:

### Required

1. **A crawl of the site.** Either:
   - A Screaming Frog export — `internal_all.csv` or `internal_html.csv`. If you have Google Analytics connected in Screaming Frog, include that data in the export; the skill uses engagement metrics in its content quality assessment.
   - The Screaming Frog MCP server, if you have it configured. The skill prefers MCP tools when available.

2. **Your priority keywords and target pages.** A simple list mapping keywords to the pages that should rank for them. This drives keyword targeting checks, cannibalization analysis, and retrieval simulation. Without it, the skill can still find technical issues, but it can't tell you whether the right pages compete for the right queries.

3. **Site context.** Be ready to answer:
   - What type of site is it? (SaaS, e-commerce, blog, local business)
   - What's the primary business goal for SEO?
   - Full site audit or specific pages?
   - Any recent changes or migrations?

### Strongly Recommended

- **Google Search Console access**, ideally via a GSC MCP server. GSC data powers the fastest cannibalization detection (query-to-page analysis), indexation checks, and Core Web Vitals reporting.
- **Google Analytics data**, either in the crawl export or via a GA4 MCP server. Used for engagement signals and AI referral traffic analysis.

### Optional

- **`.claude/product-marketing-context.md`** in your project: if present, the skill reads it instead of asking baseline questions about your business.
- **`references/itemstoignore.md`** inside the skill folder: list known issues you want excluded from findings (false positives, accepted risks, things you can't change).

## Example Invocations

```text
Run an SEO audit on example.com. Here's my Screaming Frog export:
crawl/internal_html.csv. My priority keywords and target pages are in
keywords.md. I have GSC access via MCP.
```

```text
Why doesn't AI cite my site? Audit example.com for AI search visibility.
Target queries: "best project management software", "gantt chart tool".
```

```text
Check these five pages for keyword cannibalization against my GSC data.
```

## The Retrieval Simulation Script

`scripts/retrieval_sim.py` tests whether a page's content actually surfaces for its target queries when chunked and embedded the way AI retrieval systems work. The skill invokes it during audits, but you can also run it directly.

### Dependencies

```bash
pip install sentence-transformers beautifulsoup4 requests
```

The first run downloads a local embedding model (~80MB). Everything runs locally — no API keys, no cost, no data leaves your machine.

### Usage

```bash
python scripts/retrieval_sim.py \
  --urls urls.txt \
  --queries queries.txt \
  --output results.csv
```

| Flag | Description |
|---|---|
| `--urls` | File with one URL per line, or a comma-separated list |
| `--queries` | File with one query per line, or a comma-separated list |
| `--output` | Output CSV path (default: `retrieval_sim_results.csv`) |
| `--model` | sentence-transformers model (default: `all-MiniLM-L6-v2`) |
| `--max-words` | Approximate words per chunk (default: 200) |

### Output

One CSV row per chunk-query pair: `url`, `query`, `chunk_id`, `heading`, `chunk_words`, `similarity`, `best_for_query`, `chunk_preview`. The `best_for_query` flag marks each page's strongest chunk for each query — that score is the signal.

### Interpreting Scores

Scores are relative to the embedding model. Compare across your own pages rather than treating thresholds as absolute. As starting points with the default model:

- **Below ~0.5**: the page is likely invisible to retrieval for that query
- **0.5–0.65**: weak — review the chunk structure
- **Above 0.65**: competitive

A page that scores poorly usually has a chunking problem: the answer is smeared across paragraphs instead of concentrated in one extractable, self-contained unit. The skill's `references/aeo-geo-patterns.md` covers the remediation patterns (self-contained chunks, scope statements, evidence density, entity-rich writing).

## What You Get Back

The audit report includes:

- An executive summary with overall health and the top 3–5 priority issues
- Findings by category (technical, on-page, content), each with the issue, impact, evidence, specific fix, and priority
- A prioritized action plan: critical fixes, high-impact improvements, quick wins, and long-term recommendations
