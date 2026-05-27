# Phase two: adding the email inbox

Not active in v1.0. The skill pulls Readwise Reader only. This documents how to add
the email inbox as a second source once the Reader-based briefs are proven.

## Why phase two, not phase one

Reader is already structured, has a working MCP, and holds the user's deliberate
saves — highest signal, lowest engineering. Get clustering, routing, and ranking
right against clean input first. The inbox is the noisy, dedupe-heavy bucket; design
a better deduper *after* seeing the briefs work on the easy data.

## What changes when the inbox is added

1. **Access.** The user grants Gmail access explicitly at that point — not before.
   Never pull the inbox without it being enabled.
2. **Ingestion.** Add an inbox pull alongside the Reader pull in workflow step 1.
   Many newsletters already arrive in Reader via forwarding (the May data had
   SEOFOMO, MarketingFOMO, Ness Labs as `category: email` inside Reader) — so check
   for **duplication between the inbox and Reader** before merging, or the same
   newsletter counts twice and inflates the convergence score.
3. **Routing.** The same `routing-rules.md` map applies. Newsletters are mostly
   marketing-domain; add senders to the map as they appear.
4. **Dedupe weight.** Inbox newsletters frequently re-report the same story (the
   exact problem the brief exists to solve). Treat multiple newsletters covering one
   development as convergence — but only after confirming they're independent sources,
   not the same item arriving via two paths.

## Open design question for that phase

Decide whether a newsletter that itself aggregates links (SEOFOMO, MarketingFOMO)
should contribute its *individual linked stories* to clustering, or just count as one
source. Aggregators can dominate convergence scoring if every link they carry is
treated as a separate source. Likely answer: count the newsletter as one source, but
mine its links to corroborate clusters formed from primary sources.
