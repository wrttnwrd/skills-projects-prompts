---
name: seo-geo-audit
version: 1.5.0
description: When the user wants to audit, review, or diagnose SEO or AI search visibility issues on their site. Also use when the user mentions "SEO audit," "GEO audit," "technical SEO," "why am I not ranking," "why doesn't AI cite my site," "AI search visibility," "SEO issues," "on-page SEO," "meta tags review," or "SEO health check." For building pages at scale to target keywords, see programmatic-seo. For adding structured data, see schema-markup.
---

# SEO Audit

Your goal is to identify SEO issues and provide actionable recommendations to improve organic search performance, as well as visibility to AI models.

## Rules to ignore

If `references/itemstoignore.md` exists, check it for any items you should ignore in this audit. If there are items listed, ignore them in your analysis and recommendations.

## Initial Assessment

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before auditing, understand:

1. **Site Context**
   - What type of site? (SaaS, e-commerce, blog, etc.)
   - What's the primary business goal for SEO?
   - What keywords/topics are priorities?

2. **Current State**
   - Any known issues or concerns?
   - Current organic traffic level?
   - Recent changes or migrations?

3. **Scope**
   - Full site audit or specific pages?
   - Technical + on-page, or one focus area?
   - Access to Search Console / analytics?

If you don't clearly understand answers to these questions, ask. Don't assume — the audit will be more effective if you tailor it to the site's specific context and goals.

---

## Audit Framework

### Priority Order
1. **Crawlability & Indexation** (can Google find and index it?)
2. **Technical Foundations** (is the site fast and functional?)
3. **On-Page Optimization** (is content optimized?)
4. **Content Quality** (does it deserve to rank?)
5. **Authority & Links** (does it have credibility?)

If MCP tools are available, prefer them over manual choices. That includes Screaming Frog MCP and Google Search Console MCP.

---

## Technical SEO Audit

### Crawlability

**Robots.txt**
- Check for unintentional blocks
- Verify important pages allowed
- Check sitemap reference

**XML Sitemap**
- Exists and accessible
- Submitted to Search Console
- Contains only canonical, indexable URLs
- Updated regularly
- Proper formatting

**Site Architecture**
- Important pages within 3 clicks of homepage
- Logical hierarchy
- Internal linking structure
- No orphan pages

**Crawl Budget Issues** (for large sites)
- Parameterized URLs under control
- Faceted navigation handled properly
- Infinite scroll with pagination fallback
- Session IDs not in URLs

**Rendering**
- Check for blocked resources (JS/CSS)
- Ensure critical content is server-rendered or properly rendered by Googlebot
- Test random URLs with Google Search Console URL Inspection tool to see rendered HTML, if you have access
- Ensure critical content is not hidden behind user interactions that Googlebot can't perform (e.g., click, scroll)
- Check for "load more" automatic content loading that may not be crawlable

**Agent and AI Crawler Readiness**

*Browsing agents (Operator, computer-use agents):*

- cursor:pointer in CSS for clickable elements
- for attribute on <label> tags
- uses semantic HTML where possible (e.g., <nav>, <main>, <article>)
- ARIA roles where necessary for dynamic content

*AI retrieval crawlers (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Google-Extended):*

- robots.txt allows/blocks for AI user-agents are deliberate decisions, not accidents
- Critical content available without JS execution (AI crawlers are stricter than Googlebot — most don't render JS at all)
- Chunk extractability spot-check: headings before content blocks, one idea per paragraph, no orphaned pronouns, data in tables/lists, scope statements, explicit dates (see [AEO & GEO Patterns](references/aeo-geo-patterns.md))
- AI crawler hits in server logs, if available

### Indexation

**Index Status**
- site:domain.com check
- Search Console coverage report
- Compare indexed vs. expected

**Indexation Issues**
- Noindex tags on important pages
- Canonicals pointing wrong direction
- Redirect chains/loops
- Soft 404s
- Duplicate content without canonicals

**Canonicalization**
- All pages have canonical tags
- Self-referencing canonicals on unique pages
- HTTP → HTTPS canonicals
- www vs. non-www consistency
- Trailing slash consistency

### Site Speed & Core Web Vitals

**Core Web Vitals**
- LCP (Largest Contentful Paint): < 2.5s
- INP (Interaction to Next Paint): < 200ms
- CLS (Cumulative Layout Shift): < 0.1

**Speed Factors**
- Server response time (TTFB)
- Image optimization
- JavaScript execution
- CSS delivery
- Caching headers
- CDN usage
- Font loading

**Tools**
- PageSpeed Insights
- WebPageTest
- Chrome DevTools
- Search Console Core Web Vitals report

### Mobile-Friendliness

- Responsive design (not separate m. site)
- Tap target sizes
- Viewport configured
- No horizontal scroll
- Same content as desktop
- Mobile-first indexing readiness

### Security & HTTPS

- HTTPS across entire site
- Valid SSL certificate
- No mixed content
- HTTP → HTTPS redirects
- HSTS header (bonus)

### Accessibility

- Correct Aria roles configured
- Alt text on images
- Page content is accessible using a screen reader

### URL Structure

- Readable, descriptive URLs
- Keywords in URLs where natural
- Consistent structure
- No unnecessary parameters
- Lowercase and hyphen-separated

---

## On-Page SEO Audit

### Title Tags

**Check for:**
- Unique titles for each page
- Primary keyword near beginning
- Compelling and click-worthy
- Brand name placement (end, usually)

**Common issues:**
- Duplicate titles
- Too long (truncated)
- Too short (wasted opportunity)
- Keyword stuffing
- Missing entirely

### Meta Descriptions

**Check for:**
- Unique descriptions per page
- 150-160 characters
- Includes primary keyword
- Clear value proposition
- Call to action

**Common issues:**
- Duplicate descriptions
- Auto-generated garbage
- Too long/short
- No compelling reason to click

### Heading Structure

**Check for:**
- One H1 per page
- H1 contains primary keyword
- Logical hierarchy (H1 → H2 → H3)
- Headings describe content
- Not just for styling

**Common issues:**
- Multiple H1s
- Skip levels (H1 → H3)
- Headings used for styling only
- No H1 on page
- Headings buried in multiple levels of divs

### Content Optimization

**Primary Page Content**
- Keyword in first 100 words
- Related keywords naturally used
- Sufficient depth/length for topic
- Answers search intent
- Better than competitors

**Thin Content Issues**
- Pages with little unique content
- Tag/category pages with no value
- Doorway pages
- Duplicate or near-duplicate content

### Image Optimization

**Check for:**
- Descriptive file names
- Alt text on all images
- Alt text describes image
- Compressed file sizes
- Modern formats (WebP)
- Lazy loading implemented
- Responsive images

### Internal Linking

**Check for:**
- Important pages well-linked
- Descriptive anchor text
- Logical link relationships
- No broken internal links
- Reasonable link count per page
- Nofollow not used (unless justified)

**Common issues:**
- Orphan pages (no internal links)
- Over-optimized anchor text
- Important pages buried
- Excessive footer/sidebar links

### Keyword Targeting

**Per Page**
- Clear primary keyword target
- Title, H1, URL aligned
- Content satisfies search intent
- Not competing with other pages (cannibalization)

**Site-Wide**
- Keyword mapping document
- No major gaps in coverage
- No keyword cannibalization
- Logical topical clusters

### Keyword Cannibalization Analysis

Cannibalization happens when multiple pages on the same site compete for the same query, splitting authority and click signals. It's often invisible without deliberate analysis — the symptom is pages that rank but never quite *win*, or rankings that flip between URLs week to week.

**When to run this analysis**

- Site has more than ~50 indexed pages on related topics
- Multiple pages targeting overlapping keywords (common in SaaS, publishing, content-heavy sites)
- GSC shows multiple URLs ranking for the same query
- Rankings are unstable or stuck on page 2

See [Keyword Cannibalization](references/keyword-cannibalization.md) for detection methods (GSC query-to-page, title/H1 overlap, semantic similarity), severity scoring, remediation options, and deliverables.

### Retrieval Simulation (AI Search)

Tests whether a page's content actually surfaces for its target queries when chunked and embedded the way AI retrieval systems work. Run it when the site has clear keyword targets and AI visibility matters, or when pages rank in traditional search but never get cited by AI assistants.

- Run `scripts/retrieval_sim.py` with page URLs and target queries; it chunks each page, embeds chunks with a local model, and scores cosine similarity per chunk-query pair, writing results to CSV
- Interpret scores relatively — compare across the site's own pages rather than treating thresholds as absolute. As a starting point: best-chunk similarity below ~0.5 suggests the page is invisible to retrieval for that query; 0.5–0.65 is weak (review chunk structure); above 0.65 is competitive
- For pages that score poorly, diagnose against the chunk-level extractability patterns in [AEO & GEO Patterns](references/aeo-geo-patterns.md) and recommend specific rewrites

---

## Content Quality Assessment

### E-E-A-T Signals

**Experience**
- First-hand experience demonstrated
- Original insights/data
- Real examples and case studies

**Expertise**
- Author credentials visible
- Author is a specific person, not "staff" or other generic designation
- Accurate, detailed information
- Properly sourced claims

**Authoritativeness**
- Recognized in the space
- Cited by others
- Industry credentials

**Trustworthiness**
- Accurate information
- Transparent about business
- Contact information available
- Privacy policy, terms
- Secure site (HTTPS)

**If Google Analytics data was pulled as part of crawl**
- Bounce rate
- Time on page
- Engagement rate
- Key event rates (e.g., scroll depth, clicks)

**AI Search Visibility Signals**
- AI referral traffic (chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com referrers in GA)
- Branded search volume or direct traffic lift following AI citations
- Spot-check citation share of voice: run priority queries through AI assistants and note whether (and where) the site is cited

### Content Depth

- Comprehensive coverage of topic
- Answers follow-up questions
- Better than top-ranking competitors
- Updated and current

### User Engagement Signals

- Time on page
- Bounce rate in context
- Pages per session
- Return visits

---

## Common Issues by Site Type

### SaaS/Product Sites
- Product pages lack content depth
- Blog not integrated with product pages
- Missing comparison/alternative pages
- Feature pages thin on content
- No glossary/educational content

### E-commerce
- Thin category pages
- Duplicate product descriptions
- Missing product schema
- Faceted navigation creating duplicates
- Out-of-stock pages mishandled

### Content/Blog Sites
- Outdated content not refreshed
- Keyword cannibalization
- No topical clustering
- Poor internal linking
- Missing author pages

### Local Business
- Inconsistent NAP
- Missing local schema
- No Google Business Profile optimization
- Missing location pages
- No local content

---

## Output Format

### Audit Report Structure

**Executive Summary**
- Overall health assessment
- Top 3-5 priority issues
- Quick wins identified

**Technical SEO Findings**
For each issue:
- **Issue**: What's wrong
- **Impact**: SEO impact (High/Medium/Low)
- **Evidence**: How you found it
- **Fix**: Specific recommendation
- **Priority**: 1-5 or High/Medium/Low

**On-Page SEO Findings**
Same format as above

**Content Findings**
Same format as above

**Prioritized Action Plan**
1. Critical fixes (blocking indexation/ranking)
2. High-impact improvements
3. Quick wins (easy, immediate benefit)
4. Long-term recommendations

---

## References

- [AI Writing Detection](references/ai-writing-detection.md): Common AI writing patterns to avoid (em dashes, overused phrases, filler words)
- [AEO & GEO Patterns](references/aeo-geo-patterns.md): Content patterns optimized for answer engines and AI citation, including chunk-level extractability and query fan-out coverage
- [Keyword Cannibalization](references/keyword-cannibalization.md): Detection methods, severity scoring, and remediation for pages competing on the same queries

---

## Tools Referenced

**Free Tools**
- Google Search Console (essential)
- Google PageSpeed Insights
- Bing Webmaster Tools
- Rich Results Test
- Mobile-Friendly Test
- Schema Validator

**Paid Tools** (if available)
- Screaming Frog
- Ahrefs / Semrush
- Sitebulb
- ContentKing


---

## Task-Specific Questions

1. What pages/keywords matter most?
2. Do you have Search Console access?
3. Any recent changes or migrations?
4. Who are your top organic competitors?
5. What's your current organic traffic baseline?

---


