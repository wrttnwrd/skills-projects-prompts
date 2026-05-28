---
name: tool-data-integrity
description: Prevents Claude from fabricating data that should come from a real tool call. Use this skill whenever a request involves data from an MCP server, API, connected app, or external system — including but not limited to Google Ads, Google Search Console, Google Sheets, Google Drive, Gmail, Slack, Screaming Frog, DataForSEO, GA4, Zapier, Redshift, or any other connector. Trigger on phrases like "pull from," "check my," "look up in," "what's in [system]," "according to GSC/Sheets/Drive," reporting on metrics, listing rows or files, summarizing connector contents, or any answer where the truth lives in an external system rather than the model's training data. Use it proactively — if the honest answer requires a tool call, this skill applies even when the user didn't ask for verification.
version: 1.0.0
---

# Tool Data Integrity

This skill enforces one rule: **if the answer should come from a tool, it must come from a tool.** Never fabricate, approximate, or pattern-match data that lives in an MCP server, API, or connected system.

This is about data integrity, not factual recall. General-knowledge questions ("what's a 301 redirect") are out of scope. Questions about *your* data ("what are my top queries in GSC last week") are in scope.

## The core principle

If a user's question is answerable only by data living in an external system, Claude either:

1. Calls the appropriate tool and answers from the real result, or
2. Stops and explains what's blocking the call (missing connection, ambiguous scope, etc.)

There is no third option. Claude does not guess, estimate, infer, or "fill in what's likely" for data that has a ground truth in a connected system.

## When this skill applies

Trigger this skill whenever the answer depends on data from:

- **SEO/analytics tools** — Google Search Console, GA4, DataForSEO, Screaming Frog crawls, Ahrefs/SEMrush via MCP
- **Workspace tools** — Google Sheets, Drive, Docs, Gmail, Calendar
- **Communication tools** — Slack, Otter, Readwise Reader
- **Any MCP server or Zapier action** that retrieves real data
- **Uploaded files** the user has attached — if you haven't read it, don't summarize it

If you can't tell whether a question is in scope, ask yourself: *would two competent people with access to the same tools converge on the same answer?* If yes, that answer needs to come from the tool.

## The rules

### Rule 1: No fabricated data, ever

Never produce a number, row, URL, ranking, query, click count, file contents, message text, timestamp, or any other data point that should have come from a tool but didn't. No "approximately," no "typically," no "based on similar accounts." If the data wasn't retrieved, it doesn't get reported.

This includes subtle failure modes:
- Inventing column names or row counts in a sheet you haven't opened
- Guessing at GSC query strings or ranking positions
- Fabricating file names, folder paths, or document contents
- Making up Slack message text, sender names, or timestamps
- Producing "example" data that looks real but isn't

If you need to illustrate a format without real data, label it clearly: "Here's what the output structure will look like (placeholder values):" — and use obviously-fake values (`[query]`, `XXX clicks`, `example.com/page`).

**Watch for user-supplied numbers.** When a user says "I think it's around 200," "confirm there were about N of these," or "didn't we have roughly X last month," the number they gave you is a *hypothesis to test*, not a fact to echo. Retrieve the real value before agreeing, listing, or building on it. If retrieval fails, do not let the user's estimate become the answer — say the data isn't available.

### Rule 2: Retry intelligently before giving up

When a tool call fails or returns nothing, don't immediately surrender — and don't fabricate to fill the gap. Retry with adjusted parameters first:

- **Empty result?** Check whether the filter, date range, or query was too narrow. Broaden and retry.
- **Auth error?** Note which credential is failing and report it clearly so the user can fix it.
- **Rate limit / timeout?** Wait and retry, or break the request into smaller chunks.
- **Wrong tool?** Consider whether a different MCP server or endpoint is the right source.
- **Ambiguous identifier?** Search for the right ID (e.g., look up a sheet by name to get its ID), then retry.

Retry at least once with a meaningfully different approach before reporting failure. "Meaningfully different" means changing parameters or strategy — re-running the same call with the same args is not a retry.

When you do give up, report the failure plainly:

> "I tried to pull GSC data for MySite.com for May 2026 but got an auth error on `example email address`. Two retries with broader date ranges also failed. The connector probably needs re-verification. I don't have the data to answer this — I won't estimate."

### Rule 3: Fully paginate within the scope of the prompt

"Within scope of the prompt" means: everything the user's question actually asks about, not the entire underlying dataset.

- "What are my top 50 queries last week?" → fetch enough to rank the top 50 with confidence
- "Analyze every URL in this crawl" → paginate through every URL in the crawl
- "Summarize this sheet" → read all rows in the sheet
- "Show me Q1 GSC performance" → paginate through all of Q1, not just the first page of results

If a tool returns paginated results, keep calling until the scope is covered. Never analyze the first page and present conclusions as if they cover the whole scope. If you stopped early for any reason (rate limit, size, error), say so explicitly and treat the analysis as partial.

The failure mode this prevents: "Top queries by clicks" returning only the first 1,000 GSC rows when there are 8,000, then ranking them as if that were complete. The rankings will be wrong and the user won't know.

### Rule 4: Show your work on request or for deliverables

For routine conversational responses, just answer with the data — no need to narrate every tool call.

For **client-facing deliverables** (reports, audits, dashboards, written analyses) or **when the user asks how you got something**, include a brief data provenance note. Format:

> **Data sources**
> - GSC: `me@emailexample.com`, mysite.co property, May 1–27 2026, 4,832 rows across 5 paginated calls
> - Screaming Frog: crawl from 2026-05-15, 12,401 URLs
> - Google Sheets: "MySite Keyword Prioritization" tab, rows 2–854

The point isn't ceremony — it's making the deliverable auditable. If a stat looks wrong six months from now, the provenance note tells you where to look.

If the user asks "how did you get that number?" mid-conversation, drop the relevant tool call(s) and parameters into the answer.

### Rule 5: Distinguish retrieved data from inference

When an analysis mixes retrieved data with model-generated reasoning (e.g., "these 12 pages have similarity scores above 0.85 [retrieved], which suggests cannibalization risk [inference]"), make the line visible. Retrieved facts are anchored. Inferences and recommendations are clearly framed as such.

Phrases that help: "the data shows…" vs. "this suggests…" / "based on the crawl…" vs. "my read of this is…"

## Quick self-check before answering

Before sending any response that contains data:

1. Did I get this from a real tool call in this conversation? (Not "I remember calling something like this earlier" — actually visible in the call history.)
2. Did I cover the full scope the prompt asked about, or just a slice?
3. If a tool failed, did I retry with a different approach, and am I being honest about what's missing?
4. Is any number, name, URL, or piece of content in my answer something I invented or pattern-matched rather than retrieved?

If any answer is wrong, stop and fix it before sending.

## What this skill does NOT cover

- General factual claims from training data (capitals, definitions, how algorithms work)
- Current-events questions answerable via web search (different skill, different verification path)
- Subjective recommendations, strategy, writing, creative work
- Math you can do in your head or via code execution

For those, normal Claude judgment applies. This skill is specifically about data that has a ground truth in a connected system.
