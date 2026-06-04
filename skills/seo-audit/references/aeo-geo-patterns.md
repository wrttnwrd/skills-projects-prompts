# AEO and GEO Content Patterns

Reusable content block patterns optimized for answer engines and AI citation.

---

## Answer Engine Optimization (AEO) Patterns

These patterns help content appear in featured snippets, AI Overviews, voice search results, and answer boxes.

### Definition Block

Use for "What is [X]?" queries.

```markdown
## What is [Term]?

[Term] is [concise 1-sentence definition]. [Expanded 1-2 sentence explanation with key characteristics]. [Brief context on why it matters or how it's used].
```

**Example:**
```markdown
## What is Answer Engine Optimization?

Answer Engine Optimization (AEO) is the practice of structuring content so AI-powered systems can easily extract and present it as direct answers to user queries. Unlike traditional SEO that focuses on ranking in search results, AEO optimizes for featured snippets, AI Overviews, and voice assistant responses. This approach has become essential as over 60% of Google searches now end without a click.
```

### Step-by-Step Block

Use for "How to [X]" queries. Optimal for list snippets.

```markdown
## How to [Action/Goal]

[1-sentence overview of the process]

1. **[Step Name]**: [Clear action description in 1-2 sentences]
2. **[Step Name]**: [Clear action description in 1-2 sentences]
3. **[Step Name]**: [Clear action description in 1-2 sentences]
4. **[Step Name]**: [Clear action description in 1-2 sentences]
5. **[Step Name]**: [Clear action description in 1-2 sentences]

[Optional: Brief note on expected outcome or time estimate]
```

**Example:**
```markdown
## How to Optimize Content for Featured Snippets

Earning featured snippets requires strategic formatting and direct answers to search queries.

1. **Identify snippet opportunities**: Use tools like Semrush or Ahrefs to find keywords where competitors have snippets you could capture.
2. **Match the snippet format**: Analyze whether the current snippet is a paragraph, list, or table, and format your content accordingly.
3. **Answer the question directly**: Provide a clear, concise answer (40-60 words for paragraph snippets) immediately after the question heading.
4. **Add supporting context**: Expand on your answer with examples, data, and expert insights in the following paragraphs.
5. **Use proper heading structure**: Place your target question as an H2 or H3, with the answer immediately following.

Most featured snippets appear within 2-4 weeks of publishing well-optimized content.
```

### Comparison Table Block

Use for "[X] vs [Y]" queries. Optimal for table snippets.

```markdown
## [Option A] vs [Option B]: [Brief Descriptor]

| Feature | [Option A] | [Option B] |
|---------|------------|------------|
| [Criteria 1] | [Value/Description] | [Value/Description] |
| [Criteria 2] | [Value/Description] | [Value/Description] |
| [Criteria 3] | [Value/Description] | [Value/Description] |
| [Criteria 4] | [Value/Description] | [Value/Description] |
| Best For | [Use case] | [Use case] |

**Bottom line**: [1-2 sentence recommendation based on different needs]
```

### Pros and Cons Block

Use for evaluation queries: "Is [X] worth it?", "Should I [X]?"

```markdown
## Advantages and Disadvantages of [Topic]

[1-sentence overview of the evaluation context]

### Pros

- **[Benefit category]**: [Specific explanation]
- **[Benefit category]**: [Specific explanation]
- **[Benefit category]**: [Specific explanation]

### Cons

- **[Drawback category]**: [Specific explanation]
- **[Drawback category]**: [Specific explanation]
- **[Drawback category]**: [Specific explanation]

**Verdict**: [1-2 sentence balanced conclusion with recommendation]
```

### FAQ Block

Use for topic pages with multiple common questions. Essential for FAQ schema.

```markdown
## Frequently Asked Questions

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context in 2-3 additional sentences].

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context in 2-3 additional sentences].

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context in 2-3 additional sentences].
```

**Tips for FAQ questions:**
- Use natural question phrasing ("How do I..." not "How does one...")
- Include question words: what, how, why, when, where, who, which
- Match "People Also Ask" queries from search results
- Keep answers between 50-100 words

### Listicle Block

Use for "Best [X]", "Top [X]", "[Number] ways to [X]" queries.

```markdown
## [Number] Best [Items] for [Goal/Purpose]

[1-2 sentence intro establishing context and selection criteria]

### 1. [Item Name]

[Why it's included in 2-3 sentences with specific benefits]

### 2. [Item Name]

[Why it's included in 2-3 sentences with specific benefits]

### 3. [Item Name]

[Why it's included in 2-3 sentences with specific benefits]
```

---

## Generative Engine Optimization (GEO) Patterns

These patterns optimize content for citation by AI assistants like ChatGPT, Claude, Perplexity, and Gemini.

### Statistic Citation Block

Statistics increase AI citation rates by 15-30%. Always include sources.

```markdown
[Claim statement]. According to [Source/Organization], [specific statistic with number and timeframe]. [Context for why this matters].
```

**Example:**
```markdown
Mobile optimization is no longer optional for SEO success. According to Google's 2024 Core Web Vitals report, 70% of web traffic now comes from mobile devices, and pages failing mobile usability standards see 24% higher bounce rates. This makes mobile-first indexing a critical ranking factor.
```

### Expert Quote Block

Named expert attribution adds credibility and increases citation likelihood.

```markdown
"[Direct quote from expert]," says [Expert Name], [Title/Role] at [Organization]. [1 sentence of context or interpretation].
```

**Example:**
```markdown
"The shift from keyword-driven search to intent-driven discovery represents the most significant change in SEO since mobile-first indexing," says Rand Fishkin, Co-founder of SparkToro. This perspective highlights why content strategies must evolve beyond traditional keyword optimization.
```

### Authoritative Claim Block

Structure claims for easy AI extraction with clear attribution.

```markdown
[Topic] [verb: is/has/requires/involves] [clear, specific claim]. [Source] [confirms/reports/found] that [supporting evidence]. This [explains/means/suggests] [implication or action].
```

**Example:**
```markdown
E-E-A-T is the cornerstone of Google's content quality evaluation. Google's Search Quality Rater Guidelines confirm that trust is the most critical factor, stating that "untrustworthy pages have low E-E-A-T no matter how experienced, expert, or authoritative they may seem." This means content creators must prioritize transparency and accuracy above all other optimization tactics.
```

### Self-Contained Answer Block

Create quotable, standalone statements that AI can extract directly.

```markdown
**[Topic/Question]**: [Complete, self-contained answer that makes sense without additional context. Include specific details, numbers, or examples in 2-3 sentences.]
```

**Example:**
```markdown
**Ideal blog post length for SEO**: The optimal length for SEO blog posts is 1,500-2,500 words for competitive topics. This range allows comprehensive topic coverage while maintaining reader engagement. HubSpot research shows long-form content earns 77% more backlinks than short articles, directly impacting search rankings.
```

### Evidence Sandwich Block

Structure claims with evidence for maximum credibility.

```markdown
[Opening claim statement].

Evidence supporting this includes:
- [Data point 1 with source]
- [Data point 2 with source]
- [Data point 3 with source]

[Concluding statement connecting evidence to actionable insight].
```

---

## Chunk-Level Extractability

AI search systems select content at the chunk/passage level, not the page level. A page "ranks" in generative search when individual chunks survive retrieval and selection. These patterns make chunks extractable.

### Self-Contained Chunk Pattern

Write every paragraph, bullet, and table row as if it could stand alone as an answer.

- One complete idea per paragraph
- No orphaned pronouns — restate the entity ("Google Search Console shows..." not "It shows..." or "This tool shows...")
- A concise heading before each content block, so models can group related information
- Short sentences, tight paragraphs

The Self-Contained Answer Block pattern above is the template form of this rule.

### Scope Statement Pattern

Lead chunks with conditions of applicability. Scoped advice survives selection; vague advice gets dropped.

```markdown
[Scope condition]. [Advice/claim that applies within that scope].
```

**Example:**

```markdown
For sites with more than 200 indexed pages on related topics, semantic similarity analysis is the most reliable way to detect cannibalization. Smaller sites can rely on a manual title and H1 review.
```

### Evidence Density Rule

Selection systems measure the proportion of meaningful, verifiable information to total tokens. Fact-forward chunks survive; anecdote-heavy chunks get dropped.

- Lead with facts, data, and direct answers; put stories and context after
- Use concrete numbers ("85 percent") over vague quantifiers ("most")
- Use full dates ("April 2024") over relative phrases ("recently")
- Put citations inside the chunk, not in a references footer

### Entity-Rich Writing Pattern

Clear entities strengthen how content maps into vector space and supports named entity recognition.

- Pick one term per concept and use it consistently throughout
- Use precise named entities over generic references ("Screaming Frog" not "the crawler")
- Write subject-predicate-object statements: "Paris is located in France"
- Add modifiers that disambiguate similar entities (size, function, location, purpose)

---

## Query Fan-Out and Intent-Complete Coverage

Generative search decomposes a single query into 15–20 subqueries — narrowed variants, format variations, and anticipated follow-ups — then routes each to preferred sources and formats. You can't optimize one page for one query; you optimize for the branches of the fan-out.

### Intent-Complete Hub Pattern

Cover the core question plus the adjacent intents the system will generate:

- **Narrowed variants**: audience, skill level, timeframe, budget segments of the core topic
- **Implicit slots**: prerequisites, duration, cost, safety considerations the user didn't state but needs
- **Anticipated follow-ups**: the natural next questions after the core answer

**Example:** a half-marathon training guide should cover the schedule (table), gear (list), injury prevention, nutrition, and pacing — each in its own extractable section — because the fan-out generates subqueries for all of them.

### Multimodal Parity

The system routes some subqueries to specific formats. If it prefers a table for a subquery and you only have prose, you're invisible to that branch.

- Present key data in tables and lists, not only narrative
- Provide transcripts for video content
- Expose data from interactive tools as crawlable text or structured data

---

## Freshness and Attribution Signals

Dated, attributed content outperforms undated, anonymous content in selection — especially in volatile domains.

- Explicit publication and "last reviewed" dates on the page
- Full dates inside the content where claims are time-sensitive
- Author name and credentials near the content, not only on a bio page
- Version markers for anything that changes (tools, prices, specs)

---

## Retrieval Simulation Method

How to test whether content actually surfaces for its target queries. The seo-audit skill's `scripts/retrieval_sim.py` implements the mechanics with local sentence-transformers embeddings.

**Method:**

1. Chunk each page the way retrieval systems do — split at headings, group paragraphs into ~200-word units
2. Embed chunks and target queries with the same model
3. Compute cosine similarity for every chunk-query pair
4. For each page-query pair, the best-chunk score is the signal: it represents the page's strongest candidate for retrieval

**Interpretation:**

- Scores are relative to the embedding model — always compare across the site's own pages rather than treating thresholds as absolute
- As starting points with all-MiniLM-L6-v2: best chunk below ~0.5 = likely invisible to retrieval for that query; 0.5–0.65 = weak; above 0.65 = competitive
- A page that scores well overall but has no single strong chunk is a chunking problem: the answer is smeared across paragraphs instead of concentrated in one extractable unit
- A page with one strong chunk buried below weak ones may still work — but check that the strong chunk is self-contained when read alone

**Remediation:** rewrite the weakest high-priority pages using the Chunk-Level Extractability patterns above, then re-run the simulation to confirm improvement.

---

## Extractability QA Checklist

- Every paragraph expresses one complete idea
- Chunks function independently — no orphaned pronouns or ambiguous references
- Specific data points included (percentages, full dates, metrics)
- Named entities used consistently throughout
- Scope statements define who/when the advice applies to
- Tables, lists, and structured formats used where data allows
- Citations appear inside chunks, near the claims they support
- Headings describe the content block that follows
- Author credentials and dates visible on the page
- Schema markup applied honestly and comprehensively
- Video content has transcripts; interactive tools expose crawlable data

---

## Domain-Specific GEO Tactics

Different content domains benefit from different authority signals.

### Technology Content
- Emphasize technical precision and correct terminology
- Include version numbers and dates for software/tools
- Reference official documentation
- Add code examples where relevant

### Health/Medical Content
- Cite peer-reviewed studies with publication details
- Include expert credentials (MD, RN, etc.)
- Note study limitations and context
- Add "last reviewed" dates

### Financial Content
- Reference regulatory bodies (SEC, FTC, etc.)
- Include specific numbers with timeframes
- Note that information is educational, not advice
- Cite recognized financial institutions

### Legal Content
- Cite specific laws, statutes, and regulations
- Reference jurisdiction clearly
- Include professional disclaimers
- Note when professional consultation is advised

### Business/Marketing Content
- Include case studies with measurable results
- Reference industry research and reports
- Add percentage changes and timeframes
- Quote recognized thought leaders

---

## Voice Search Optimization

Voice queries are conversational and question-based. Optimize for these patterns:

### Question Formats for Voice
- "What is..."
- "How do I..."
- "Where can I find..."
- "Why does..."
- "When should I..."
- "Who is..."

### Voice-Optimized Answer Structure
- Lead with direct answer (under 30 words ideal)
- Use natural, conversational language
- Avoid jargon unless targeting expert audience
- Include local context where relevant
- Structure for single spoken response
