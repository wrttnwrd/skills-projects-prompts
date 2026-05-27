---
name: weeklybrief
version: 1.0.0
description: When the user wants their weekly reading digest from Readwise Reader — staying on top of new developments in marketing/SEO/AI and in Dungeons & Dragons. Triggers include "run my weekly brief," "industry brief," "what did I miss this week," "catch me up on my feeds," or "weekly digest." Produces two separate briefs (marketing and D&D) from one Reader pull and appends structured records to two running Markdown base files.
---

# Weekly Brief

Generate two weekly synthesis briefs from the user's Readwise Reader — one for **marketing** (SEO, content strategy, AI-in-marketing, agentic tooling) and one for **Dungeons & Dragons** — in a single pass, and append structured records to two running base files so the user accumulates a queryable history.

The goal is not to list what the user saved. It is to **triage and synthesize**: collapse the same story told by many sources into one entry, surface what genuinely matters, and connect it to the user's work. The user already captures plenty; what's missing is something that reads across all of it and says "here are the few things that matter, here's why."

## Why two briefs

Marketing and D&D have genuinely different signal logic, so they get different rankers:

- **Marketing** lives on **convergence**. Multiple independent sources landing on the same topic in one week is *the* signal — in a fast-moving professional field, importance reveals itself through that convergence. Lead with the converged story.
- **D&D** is the opposite. These feeds are mostly individual authors publishing standalone craft pieces (GM advice, lorebooks, reviews). They rarely converge in a week, and shouldn't be expected to. The signal is "is this a meaty piece from a writer the user follows," not "are multiple sources saying this." The brief's value here is *don't lose good craft pieces in the feed firehose*, not *stay abreast of an industry*.

One ranker cannot serve both honestly. Keep them separate end to end: separate clustering, separate ranking, separate base files.

## Inputs and scope

- **Source: Readwise Reader only** (phase 1). Email inbox is a documented phase-2 addition — see `references/phase-two-inbox.md`. Do not pull the inbox unless the user has explicitly enabled it.
- **Time window: the last 7 days** by default, using `updated_after` set to 7 days before today. The user can ask for a different window ("last two weeks," "since the start of the month").
- Pull across all relevant locations (`new`, `later`, `shortlist`, `archive`, `feed`,`library`). Saves the user made deliberately (web highlighter, shortlist) get weighted up — they already voted.

## Workflow

### 1. Pull the week from Reader

Call `reader_list_documents` with `updated_after` = (today − 7 days, ISO 8601), `limit` 100, and lean `response_fields`: `title, author, source, category, location, tags, site_name, word_count, reading_time, published_date, summary, url, source_url, saved_at`. Paginate with `page_cursor` if `nextPageCursor` is returned.

### 2. Route each item to a domain

Assign every item to `marketing`, `dnd`, or `drop`. Routing is primarily **source-based** — see `references/routing-rules.md` for the maintained source→domain map. For sources not in the map, fall back to content similarity against the domain descriptions (marketing keywords vs. D&D keywords in title + summary).

**Flag, don't guess.** If an item can't be routed with confidence (unknown source, ambiguous content), put it in a "needs routing" list shown to the user rather than silently dropping or misfiling it. Suggest a rule to add to the routing map.

`drop` covers non-content noise: raw Google searches, empty highlights, login pages, etc. Productivity/general-interest newsletters (e.g. Ness Labs) that fit neither domain also drop by default unless the user asks for a third bucket.

### 3. Cluster and rank — per domain

**Marketing:**
- Cluster items by topic. Group items covering the same development into one cluster.
- Score each cluster's signal using the heuristic in `references/ranking-heuristics.md`: convergence (primary — how many independent sources), the user's own saves (weighted up), recency-of-development vs. recency-of-coverage, and relevance to the user's work (SEO, content strategy, AI-in-marketing, agentic tooling).
- Order clusters by signal, highest first.

**D&D:**
- Do **not** force convergence clustering. Treat items mostly as individual pieces.
- Rank by piece substance (word count / depth as a rough proxy), author the user follows, and **Praxia-adjacency**: weight up anything touching worldbuilding, lore systems, homebrew, or knowledge-graph-able lore, since that actively feeds the user's Praxia project rather than just entertaining. See `references/ranking-heuristics.md`.

### 4. Emit two briefs

Write each brief as Markdown. Structure in `references/brief-format.md`. In short:
- **Marketing:** lead with the week's converged signal as a synthesized paragraph (not a link list), name *why it matters to the user's work*, then secondary clusters, then links.
- **D&D:** "N solid pieces this week, here's what each gives you," Praxia-relevant pieces first.
- If a section is empty this week, say so briefly rather than padding.

### 5. Append to the two base files

Append a dated section to each base file in the user's data directory (NOT in the
skill folder — methodology and accumulated history are kept separate):
- `/Users/i.lurie/claude-tasks/weeklybrief/marketing-brief.md`
- `/Users/i.lurie/claude-tasks/weeklybrief/dnd-brief.md`

Create `/Users/i.lurie/claude-tasks/weeklybrief/` if it does not exist (`mkdir -p`) before the
first write. Each base file gets a title header on creation; thereafter append only,
never overwrite.

Use the **structured append format** in `references/brief-format.md` (dated `##` header per week, one pipe-delimited record per item with fixed fields). This keeps the base human-readable *and* machine-parseable, so "show me everything on AI search since March" is a reliable grep or clean re-read. Create the file with a title header if it doesn't exist yet; never overwrite — always append.

### 6. Report

Show the user both briefs in the conversation. Note any "needs routing" items and propose routing-map additions. Confirm both base files were appended to.

## References

- [Routing rules](references/routing-rules.md): source→domain map and routing logic
- [Ranking heuristics](references/ranking-heuristics.md): per-domain signal scoring
- [Brief format](references/brief-format.md): brief structure and the structured base append format
- [Phase two: inbox](references/phase-two-inbox.md): how to add the email inbox as a second source later
