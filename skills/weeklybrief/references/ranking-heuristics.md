# Ranking heuristics

Two different rankers. Do not cross them.

## Marketing — convergence-weighted

Score each *cluster* (not each item). Inputs, in rough priority:

1. **Convergence (primary).** How many independent sources cover this topic this week. Two sources is a signal; three or more is the week's headline. This is the single best filter and the reason weekly beats daily — convergence only becomes visible across days.
2. **User's own saves (weighted up).** Items the user actively saved (web highlighter, shortlist, `later`) count for more than passive RSS/feed items. They already voted. A cluster containing a deliberate save outranks an equivalent cluster of only feed items.
3. **Recency of the development vs. recency of the coverage.** Distinguish a genuinely new thing from the Nth take on last month's news. Compare `published_date` of the underlying development to the coverage dates.
4. **Relevance to the user's work.** Weight toward SEO, content strategy, AI-in-marketing, agentic tooling. A cluster that connects to the user's TTSOOE methodology or "inimitable content" positioning is more useful than generic marketing news — say so explicitly in the brief.

Output: clusters ordered high→low signal. Label each `high` / `medium` / `low` in the base file.

## D&D — author/craft-weighted

Do **not** expect or force convergence. Rank individual pieces by:

1. **Substance.** Depth of the piece (word count / reading time is a rough proxy). A 1,500-word craft essay beats a 300-word link post.
2. **Author the user follows.** Known authors (Justin Alexander, Sly Flourish) are inherently higher-confidence than random feed items.
3. **Praxia-adjacency (weighted up).** Anything touching worldbuilding, lore systems, homebrew settings, pantheons/cosmology, or content that could feed a queryable lore knowledge graph gets boosted — this actively feeds the user's Praxia project (Obsidian → RDF/Turtle → Neo4j) rather than just entertaining. Reviews and general GM advice are useful but rank below worldbuilding material.

Output: pieces ordered high→low, Praxia-relevant first. The framing is "here are the few good pieces, here's what each gives you" — not a converged narrative.
