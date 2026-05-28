---
name: weeklybrief
version: 1.0.0
description: When the user wants their weekly reading digest from Readwise Reader — staying on top of new developments in marketing/SEO/AI and in Dungeons & Dragons. Triggers include "run my weekly brief," "industry brief," "what did I miss this week," "catch me up on my feeds," or "weekly digest." Produces two separate briefs (marketing and D&D) from one Reader pull and writes each to its own dated Markdown file.
---

# Weekly Brief

Generate two weekly synthesis briefs from the user's Readwise Reader — one for **marketing** (SEO, content strategy, AI-in-marketing, agentic tooling) and one for **Dungeons & Dragons** — in a single pass, and write each brief to its own dated file so the user accumulates a queryable history.

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

### 4. Flag marketing stories to pass to clients (Otter)

After ranking the marketing clusters — and **marketing only**, D&D is never checked — decide whether any story is worth passing along to a specific client. The point is to catch the moment when this week's development directly bears on something a client is actively working on, so you can proactively forward it.

Roster is **hybrid**: start from a maintained client list if one exists, and also surface clients found in Otter that aren't on the list. See `references/client-flagging.md` for the full procedure. In short:

- Load the roster from `/Users/i.lurie/claude-tasks/client-list.md` — each client has a **topics/notes** line of what they're actively working on. Use those notes as the primary match signal, and augment with current Otter meetings (topics drift). If a client has no notes yet, fall back to inferring topics from their Otter meetings. If the file is missing, work from Otter alone.
- Pull Otter meeting metadata for the **last 90 days** (`search` with empty `query` and `created_after` = today − 90 days). Match stories against each meeting's `summary` / `outline` / `action items`; only `fetch` a full transcript to confirm a borderline match.
- For each marketing cluster, flag a client only when there is a **genuine, specific** connection — story → client → why, citing the meeting title and date. No speculative or generic matches ("they do marketing too" is not a match).
- Surface any client found in Otter but not on the list as a **"new client?"** suggestion to add to `client-list.md`.
- If nothing connects this week, record that explicitly rather than padding.
- If Otter is unavailable (e.g. connector errors/timeouts after a retry), do **not** silently skip this step — write "Otter unavailable this week — client matches not checked" in the "Pass along to clients" section so the gap is visible.

### 5. Emit two briefs

Write each brief as Markdown. Structure in `references/brief-format.md`. In short:
- **Marketing:** lead with the week's converged signal as a synthesized paragraph (not a link list), name *why it matters to the user's work*, then secondary clusters, then a **"Pass along to clients"** section (from step 4), then links.
- **D&D:** "N solid pieces this week, here's what each gives you," Praxia-relevant pieces first.
- If a section is empty this week, say so briefly rather than padding.

### 6. Write the two dated brief files

Write each brief to its own dated file in the user's data directory (NOT in the
skill folder — methodology and accumulated history are kept separate). One file per
brief per week, named by the brief's end date (`YYYY-MM-DD.md`), in a per-domain subfolder:
- `/Users/i.lurie/claude-tasks/weeklybrief/marketing/{YYYY-MM-DD}.md`
- `/Users/i.lurie/claude-tasks/weeklybrief/dnd/{YYYY-MM-DD}.md`

Create `/Users/i.lurie/claude-tasks/weeklybrief/marketing/` and `.../dnd/` if they do not exist (`mkdir -p`) before writing. If a file for that date already exists (a re-run), overwrite it — one canonical file per week.

Use the **dated-file format** in `references/brief-format.md` (one pipe-delimited record per item with fixed fields, under cluster headings). Filename is the date, so no in-file date header is needed. The fixed pipe fields keep each file human-readable *and* machine-parseable, so "show me everything on AI search since March" stays a reliable grep across the folder.

### 7. Report

Show the user both briefs in the conversation. Note any "needs routing" items and propose routing-map additions. Surface any **"new client?"** candidates found in Otter and ask whether to add them to `client-list.md`. Confirm both dated files were written, with their paths.

## References

- [Routing rules](references/routing-rules.md): source→domain map and routing logic
- [Ranking heuristics](references/ranking-heuristics.md): per-domain signal scoring
- [Client flagging](references/client-flagging.md): matching marketing stories to client transcripts in Otter
- [Brief format](references/brief-format.md): brief structure and the dated per-brief file format
- [Phase two: inbox](references/phase-two-inbox.md): how to add the email inbox as a second source later
