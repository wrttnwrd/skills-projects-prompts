# Brief format

## Marketing brief (conversational output)

Lead with the converged signal as a *synthesized paragraph*, not a link dump. Then secondary clusters. Then links grouped by cluster.

```
**Marketing brief — week of {start}–{end}, {year}**

**This week's signal: {one-line headline of the top cluster}.** {2–4 sentences
synthesizing what the converged sources collectively say. Name the sources inline.
State explicitly why it matters to the user's work — TTSOOE, inimitable content,
client positioning, etc.} ({N} sources, links below)

**Also notable: {secondary cluster}.** {1–2 sentences.} ({N} sources)

Links:
- {title} — {source} — {url}
- ...
```

If only one cluster has real signal this week, say so — don't manufacture a second.

## D&D brief (conversational output)

```
**D&D brief — week of {start}–{end}, {year}**

{N} solid pieces this week. {If any are Praxia-relevant, lead with those and say why.}

- **{title}** ({author}) — {1 sentence on what it gives you}. {Praxia note if relevant.} {url}
- ...
```

## Structured base append format

Append to `/Users/i.lurie/weeklybrief/marketing-brief.md` and
`/Users/i.lurie/weeklybrief/dnd-brief.md`. Never overwrite. One dated `##`
section per week; one pipe-delimited record per item with fixed fields so the base
stays grep-able and re-readable.

Record fields: `DATE | SOURCE (mark "saved" if a deliberate save) | TITLE | URL | ONE-LINE SUMMARY`

Marketing base — group records under a cluster heading with its signal label:

```markdown
## {YYYY-MM-DD} — week of {start}–{end}

### Cluster: {name} [signal: high]
- 2026-05-21 | Kevin Indig (saved) | "What is/How to" lost 35–60% of clicks | https://... | Informational content no longer best; original research wins
- 2026-05-25 | Rand Fishkin / SparkToro | Inimitable Product is the New "Make Great Content" | https://... | "Just make great content" obsolete as Google stops indexing

### Cluster: {name} [signal: medium]
- ...
```

D&D base — flat list under the dated header, Praxia-relevant tagged:

```markdown
## {YYYY-MM-DD} — week of {start}–{end}

- 2026-05-25 | Justin Alexander | Chaos Lorebook: The Scarlet Oath | https://... | Lorebook entry [praxia]
- 2026-05-25 | Sly Flourish | Defending Out of the Fun | https://... | GM advice on defensive play
```

The dated `##` headers make time-slicing trivial; the fixed pipe fields make field
extraction trivial. Keep both properties — that's the whole point of a Markdown base
over a prose log.
