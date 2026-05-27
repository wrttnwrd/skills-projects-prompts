# Routing rules

Each Reader item routes to `marketing`, `dnd`, or `drop`. Match on `site_name` / `source_url` host first; fall back to content similarity on title + summary for unknown sources.

## Marketing sources

| Source / host | Notes |
|---|---|
| growth-memo.com | Kevin Indig |
| sparktoro.com | Rand Fishkin, Amanda Natividad |
| moz.com | Aleyda Solis and others |
| seerinteractive.com | Wil Reynolds / Seer |
| SEOFOMO / orainti | newsletter (category: email) |
| MarketingFOMO | newsletter (category: email) |
| substack.com (Kevin Indig notes) | route by author when host is generic |

## D&D sources

| Source / host | Notes |
|---|---|
| thealexandrian.net | Justin Alexander |
| slyflourish.com | Sly Flourish / Mike Shea |

## Drop by default

- Raw search-engine result pages (e.g. google.com/search URLs)
- Empty highlights (null title and summary)
- Login / nav / utility pages
- General-interest or productivity newsletters that fit neither domain (e.g. Ness Labs) — drop unless the user requests a third bucket

## Fallback for unknown sources

If the host isn't mapped, score the title + summary against each domain's vocabulary:
- **Marketing:** SEO, search, AI Overviews, AI Mode, GEO/AEO, content strategy, ranking, SERP, LLM, agentic, marketing, citations, traffic, clickstream
- **D&D:** GM/DM, campaign, adventure, lore, worldbuilding, homebrew, monster, encounter, dungeon, RPG, tabletop, sourcebook

Assign to the higher-scoring domain only if the margin is clear. Otherwise mark **needs routing** and surface to the user with a suggested rule to add here. Never guess silently.

## Maintenance

When the user confirms a route for a previously unknown source, add it to the appropriate table above so future runs are deterministic.
