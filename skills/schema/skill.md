---
name: schema-json-ld
description: Generate, self-review, and validate JSON-LD schema markup for web pages. Enforces schema.org compliance through a mandatory workflow with type selection, verification against schema.org, self-review, revision, and a validator pass before delivery.
---

# When to use this skill

Whenever the user asks you to generate, write, add, or fix JSON-LD schema markup for a web page or site. Also use when the user mentions "schema markup," "structured data," "JSON-LD," "rich results," or "schema.org."

# The workflow is mandatory

Do not skip steps. The most common failure mode in schema generation is picking the wrong type from memory, then writing plausible-looking JSON around it. The workflow below is the only reliable way to avoid that.

Steps:

1. Analyze the page
2. Choose the primary type
3. Verify the type against schema.org
4. Generate
5. Self-review against the checklist
6. Revise
7. Validate
8. Deliver

## Step 1 — Analyze the page

Before opening JSON, write a one-line answer to each:

- **Primary purpose of this page** — is it selling a product, describing a service, publishing an article, listing a physical location, presenting an event, hosting a video, etc.?
- **Is there a price on this page** for a specific purchasable item? (Yes/No)
- **Are there numbered, sequential steps** to accomplish a task? (Yes/No)
- **Are there explicit questions and answers** visible on the page? (Yes/No)
- **Is this a physical place customers can visit**, or only an online entity? (Physical/Online/Both)
- **Topics covered** — the 2–5 main subjects the page discusses.

If you were given a URL, fetch the page first. Do not infer page content from the URL slug.

If the user instructions say to ignore previously-generated schema, do not look at existing schema markup on the page. Work from page content only.

## Step 2 — Choose the primary type

Use the page-archetype map and disambiguation tables below. Do not pick from memory. Write down:

- **Chosen type** and the one-line reason it fits the page's primary purpose better than the alternatives.
- **Nested types** you plan to include (brand, author, publisher, breadcrumbs, etc.).

If you cannot answer "why this type and not the alternative" in one line, you have not chosen yet — keep working.

## Step 3 — Verify the type against schema.org

For every type you plan to use — primary and nested — fetch `https://schema.org/<TypeName>` and confirm:

- The type exists at that URL (a 200 response with the type's spec page).
- Every property you plan to use is listed on that page or inherited from a parent type.
- You are not using a property defined only on a different type.

Do not skip this step on the assumption that you remember the spec. Your memory of schema.org is stale and incomplete; this is the single highest-yield check.

## Step 4 — Generate the schema

Write the JSON-LD. Follow the core principles and data formatting standards below.

## Step 5 — Self-review against the checklist

Before delivering, work through every item. Write out the answer to each — do not skim.

**Type correctness**

- [ ] Did I confirm the chosen type exists on schema.org by fetching its page?
- [ ] Does the type match the page's *primary* purpose, not a secondary feature?
- [ ] Did I pick the most specific applicable type (e.g., `LocalBusiness` over `Organization`, `BlogPosting` over `Article` when appropriate)?
- [ ] Did I avoid defaulting to a familiar type out of habit?

**Property correctness**

- [ ] Is every property I used valid for its type (verified against schema.org, not memory)?
- [ ] Did I invent any properties? (If yes, remove them.)
- [ ] Are all required properties for the type present?
- [ ] Did I omit properties whose values I do not actually know? (No guessing.)

**Forbidden patterns**

- [ ] No `Offer` or `Product` schema if there is no price for a specific purchasable item on the page.
- [ ] No `HowTo` unless the page contains numbered, sequential steps to accomplish a task.
- [ ] No `FAQPage` or `Question` unless there are explicit Q&A pairs visible on the page.
- [ ] No `Article` (or subtype) on a page whose primary purpose is selling a product or service.
- [ ] No `Recipe` unless the page is an actual recipe with ingredients and instructions.
- [ ] No `Event` unless there is a specific dated occurrence (not an evergreen page about events generally).

**Structure**

- [ ] Schema is nested rather than split into many flat top-level blocks.
- [ ] Topical signals are present — `about` and/or `mentions` referencing the page's main subjects.
- [ ] Repeated entities are tied together with `@id` references rather than duplicated.
- [ ] If this is the homepage, full `Organization` (or `LocalBusiness` / `Corporation`) detail is present.

**Data formatting**

- [ ] All URLs are absolute.
- [ ] All dates use ISO 8601.
- [ ] Prices include `priceCurrency`.
- [ ] Phone numbers use international format.
- [ ] JSON is syntactically valid (no trailing commas, balanced braces, properly quoted strings).

For every box you cannot tick, note what's wrong. That's the input to Step 6.

## Step 6 — Revise

For each issue found in Step 5, fix it. If a fix requires re-verifying a type or property against schema.org, do that — don't just edit and hope.

After revising, run Step 5 again on the changed portions. Stop iterating only when every box can be ticked honestly.

## Step 7 — Validate

Submit the generated JSON-LD to `https://validator.schema.org/`. Use WebFetch with the JSON in the payload, or Playwright if the page needs a JS-driven flow. Read the errors and warnings:

- **Errors**: must be fixed. Return to Step 6.
- **Warnings about missing recommended properties**: fix if the data is available on the page; otherwise note them to the user as opportunities for richer markup.
- **Warnings you do not recognize**: do not ignore. Look up the property on schema.org.

If you cannot reach the validator for any reason, say so explicitly when delivering and recommend the user run it.

## Step 8 — Deliver

Present the final schema in the agreed output format (see Output Format below). Include a short note covering:

- The primary type chosen and why.
- Any required properties that were unavailable on the page and therefore omitted.
- The validator result — clean, or a list of remaining warnings the user should be aware of.

# Type selection reference

## Page archetype → recommended primary type

| Page archetype | Primary type | Common nested types |
|---|---|---|
| SaaS / software homepage | `SoftwareApplication` or `Organization` (homepage rule) | `Offer`, `AggregateRating`, `Organization` |
| Agency / services homepage | `Organization` or `ProfessionalService` | `Service`, `Person` (founders), `ContactPoint` |
| Physical business homepage | `LocalBusiness` (most specific subtype) | `PostalAddress`, `GeoCoordinates`, `OpeningHoursSpecification` |
| Pricing page | `Product` or `SoftwareApplication` with `Offer`(s) | `Offer`, `PriceSpecification` |
| Service detail page | `Service` | `Organization` (provider), `Offer` (if priced) |
| Blog post | `BlogPosting` | `Person` (author), `Organization` (publisher), `ImageObject` |
| News article | `NewsArticle` | same as `BlogPosting` |
| Long-form editorial / guide | `Article` | same as `BlogPosting` |
| Product detail page | `Product` | `Offer`, `Brand`, `AggregateRating`, `Review` |
| Comparison / "X vs Y" page | `Article` or `WebPage` with `mentions` on each compared item | `Product` / `SoftwareApplication` in `mentions` |
| Location page (one of many) | `LocalBusiness` subtype | `PostalAddress`, `GeoCoordinates` |
| Case study | `Article` with `about` referencing the client/project | `Organization` (client), `Person` (testimonial author) |
| FAQ page | `FAQPage` (only if real Q&A pairs visible) | `Question`, `Answer` |
| How-to / tutorial with numbered steps | `HowTo` | `HowToStep`, `HowToSupply`, `HowToTool` |
| Event page | `Event` (most specific subtype) | `Place`, `Offer`, `Person`/`Organization` (performer/organizer) |
| Recipe | `Recipe` | `NutritionInformation`, `HowToStep` |
| Video page | `VideoObject` | `Person` (creator), `Organization` (publisher) |
| Job posting | `JobPosting` | `Organization` (hiringOrganization), `Place` |
| Author bio / team member page | `Person` | `Organization` (works for), `Occupation` |
| Generic content page that fits none of the above | `WebPage` with `about` / `mentions` | depends on subject |

## Disambiguation tables

**Article vs BlogPosting vs NewsArticle**

| Use | When |
|---|---|
| `NewsArticle` | Time-sensitive news reporting from a news publication |
| `BlogPosting` | Personal or company blog post, opinion, tutorial, marketing content |
| `Article` | Long-form editorial that isn't clearly a blog post or news (use as fallback) |

**Product vs SoftwareApplication vs Service**

| Use | When |
|---|---|
| `Product` | Physical goods, or a packaged digital good with a SKU |
| `SoftwareApplication` | Software / SaaS — has version, operating system, application category |
| `Service` | Human-delivered or ongoing service (consulting, agency work, subscriptions where the value is service not software) |

A SaaS offering can reasonably be `SoftwareApplication`; use `Product` only if the context strongly prefers e-commerce semantics.

**Organization vs LocalBusiness vs Corporation**

| Use | When |
|---|---|
| `Organization` | Generic organization with no physical customer-facing location |
| `LocalBusiness` (or subtype) | Has a physical place customers visit |
| `Corporation` | Specifically a publicly-traded or large corporate entity (rarely needed) |

Always prefer the most specific `LocalBusiness` subtype available (`Restaurant`, `Dentist`, `LegalService`, `Plumber`, etc.).

**WebPage vs CollectionPage vs ItemPage vs ProfilePage**

| Use | When |
|---|---|
| `WebPage` | Generic single page |
| `CollectionPage` | Page that lists or collects multiple items (category, index) |
| `ItemPage` | Page about one specific item (often combined with `Product`, etc.) |
| `ProfilePage` | Bio or profile page for a person or organization |

**Review vs AggregateRating**

| Use | When |
|---|---|
| `Review` | A single review by a named author |
| `AggregateRating` | Summary stats across many reviews (rating value + review count) |

Both can appear together on a product page.

## Forbidden patterns

Do not produce any of these. They are the most common type-misuse errors:

- `Product` or `Offer` on a page that does not display a price for a specific purchasable item.
- `HowTo` on a page that does not have numbered, sequential, actionable steps.
- `FAQPage` or `Question` on a page without explicit, visible question-and-answer pairs.
- `Article` (or subtype) on a page whose primary purpose is selling a product or service.
- `Recipe` on a page that is *about* food but isn't an actual recipe with ingredients and steps.
- `Event` on a page that discusses events in general but doesn't host a specific dated event.
- `Review` with no named author.
- `AggregateRating` with no `reviewCount` and `ratingValue`.
- Inventing properties — putting a property on a type where it doesn't exist. Always verify on schema.org.
- Filling required properties with placeholder or guessed data. If the value is unknown, either omit the property or choose a more general type that doesn't require it.
- Many flat top-level entities when nesting would be more accurate (e.g., separate `Organization` and `Person` blocks where the `Person` is an employee — nest the `Person` inside).

# Core principles

1. **Hierarchical, nested structure.** Describe the main entity, then nest related entities (brand, author, publisher, offers, reviews, breadcrumbs) inside it. Avoid emitting many flat sibling blocks when a hierarchy is more accurate.

2. **schema.org vocabulary first.** Use the types and properties defined at schema.org. If no schema.org vocabulary exists for something specific, use simple clear names — but verify there isn't a schema.org equivalent first.

3. **Most specific applicable type.** `Dentist` beats `LocalBusiness` beats `Organization`. `BlogPosting` beats `Article`. Generic types are a last resort.

4. **Topical signals for knowledge graph and LLM visibility.** Always include `about` and/or `mentions` referencing the main subjects of the page. This is what makes the schema useful beyond Google rich results — it's how the page becomes legible to knowledge graphs and LLMs.

5. **Page-truth only.** Only include data that actually appears on the page. Don't fabricate, infer, or pull from outside sources unless the user explicitly approves.

6. **Homepage rule.** Unless told otherwise, assume the site's homepage gets the full `Organization` (or `LocalBusiness` / `Corporation`) schema — name, url, logo, sameAs (social profiles), contactPoint, address, founder, foundingDate, etc., as available.

7. **Reference, don't duplicate.** When the same entity appears in multiple places, define it once with an `@id` and reference it elsewhere.

# Common types overview

Familiar types for quick recall. Always verify on schema.org before using.

- **Organization**: Companies, brands, institutions
- **LocalBusiness**: Physical business locations (prefer a specific subtype)
- **Person**: Individual people
- **Product**: Physical or packaged digital goods
- **SoftwareApplication**: Software / SaaS
- **Service**: Services offered
- **Article / BlogPosting / NewsArticle**: Editorial content
- **WebPage / WebSite**: Generic pages and sites
- **BreadcrumbList**: Navigation breadcrumbs
- **FAQPage**: Pages with real Q&A pairs
- **HowTo**: Step-by-step instructions
- **Review / AggregateRating**: Reviews and ratings
- **Event**: Specific dated events
- **Recipe**: Cooking recipes
- **VideoObject / ImageObject**: Media
- **JobPosting**: Job listings

# Data formatting standards

**Dates** — ISO 8601:

- Date only: `YYYY-MM-DD`
- Date and time: `YYYY-MM-DDTHH:MM:SS`
- With timezone: `YYYY-MM-DDTHH:MM:SS-07:00` or `YYYY-MM-DDTHH:MM:SSZ`

**URLs** — always absolute. Never relative paths.

**Images** — full URL, ideally as an `ImageObject` with `width` and `height`:

```json
"image": {
  "@type": "ImageObject",
  "url": "https://example.com/image.jpg",
  "width": 1200,
  "height": 800
}
```

**Phone numbers** — international format: `+1-415-555-1234`.

**Prices** — always include `priceCurrency`:

```json
"offers": {
  "@type": "Offer",
  "price": "29.99",
  "priceCurrency": "USD",
  "availability": "https://schema.org/InStock"
}
```

**@context** — at root level:

```json
{
  "@context": "https://schema.org",
  "@type": "TypeName"
}
```

For multiple top-level entities, use `@graph`:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", "@id": "https://example.com/#organization" },
    { "@type": "WebSite" }
  ]
}
```

# Patterns

## Organization with logo and social profiles

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Example Company",
  "url": "https://example.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://example.com/logo.png",
    "width": 600,
    "height": 60
  },
  "sameAs": [
    "https://twitter.com/example",
    "https://www.linkedin.com/company/example"
  ]
}
```

## BlogPosting nested with author, publisher, and topical signals

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Article Title",
  "image": "https://example.com/image.jpg",
  "datePublished": "2026-05-11",
  "dateModified": "2026-05-11",
  "author": {
    "@type": "Person",
    "name": "John Doe",
    "url": "https://example.com/authors/john-doe"
  },
  "publisher": {
    "@id": "https://example.com/#organization"
  },
  "about": [
    { "@type": "Thing", "name": "AI copywriting" },
    { "@type": "Thing", "name": "Marketing automation" }
  ]
}
```

## BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com" },
    { "@type": "ListItem", "position": 2, "name": "Category", "item": "https://example.com/category" },
    { "@type": "ListItem", "position": 3, "name": "Current Page", "item": "https://example.com/category/page" }
  ]
}
```

## Multiple related entities with @id references

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Corp"
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com",
      "publisher": { "@id": "https://example.com/#organization" }
    },
    {
      "@type": "BlogPosting",
      "publisher": { "@id": "https://example.com/#organization" },
      "isPartOf": { "@id": "https://example.com/#website" }
    }
  ]
}
```

# Output format

Always wrap the final schema in `<script type="application/ld+json">` tags so it can be pasted directly into a page:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TypeName"
}
</script>
```

For multiple related schemas, prefer one `@graph` block inside a single script tag over multiple script tags.

# Validation tools

The skill requires that you (the agent) run validation in Step 7. Tools:

- **Schema Markup Validator** — `https://validator.schema.org/` — the canonical schema.org validator. Use this in Step 7.
- **Google Rich Results Test** — `https://search.google.com/test/rich-results` — recommend to the user for Google-specific rich-result eligibility.
- **JSON-LD Playground** — `https://json-ld.org/playground/` — useful for debugging unusual graph structures.
