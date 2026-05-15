---
name: Personal consultant / digital-marketing-nerd homepage
archetype: personal-consultant-homepage
url: https://www.ianlurie.com/
gold:
  primary_type_options: [Person, ProfessionalService]
  must_include_nested: []
  forbidden_types: [Product, Offer, Article, BlogPosting, NewsArticle, HowTo, Recipe, Event, FAQPage, SoftwareApplication]
  must_have_properties: [name, url, description]
  must_have_topical_signals: true
  validator_must_pass: true
notes: |
  This fixture loads the real-world HTML of ianlurie.com (saved as a sibling file in this folder)
  instead of embedding the page content inline. The subagent must read the file, strip nav/footer
  chrome and any pre-existing JSON-LD, and treat the remaining visible content as the page.

  Archetype discriminator: the homepage of a one-person consultant where the *person* is the brand.
  Person is the most specific and best choice — the page is unambiguously about Ian Lurie himself
  (his name is the H1, the domain, and the entire framing). ProfessionalService is acceptable if
  the skill leans into the consulting/training/speaking offering, but it has to actually carry the
  service-family signals (serviceType, category, audience) on the primary if it goes that way.

  Why Organization is NOT acceptable as primary: there is no current organization. Ian references
  Portent ("RIP Portent") as defunct in his own writing. Emitting a primary Organization here
  would invent an entity the page doesn't claim.

  Why SoftwareApplication is forbidden: the page lists blog posts and consulting services, not
  software products. The skill sometimes reaches for SoftwareApplication on tech-leaning content;
  this fixture exists partly to catch that lazy reach.

  Why blog-post-y types (Article, BlogPosting, NewsArticle) are forbidden: this is the homepage,
  not an individual blog post. The homepage *lists* posts; it isn't one.

  Topical signals: must be on the primary. For Person → knowsAbout. For ProfessionalService →
  serviceType plus category and/or audience. Topics on a sibling WebPage do not satisfy
  criterion 5.

  must_include_nested is intentionally empty. The skill has reasonable latitude here — it could
  nest a Blog, a WebSite anchor, sameAs URLs as bare strings, or nothing beyond knowsAbout
  Thing nodes. None of those are required; what matters is that the primary is right and the
  topical signals are well placed.
---

# Page content

The page content for this fixture is the HTML file saved at:

`/Users/i.lurie/prompts-projects-skills/projects/schema-benchmark/fixtures/ianlurie-homepage.html`

Read that file with the Read tool. Treat its rendered, visible content as the page you are generating schema for — specifically:

- Use the `<title>` tag, `<meta name="description">`, and visible body content (H1, H2, body copy, post listings, about/bio text, social links) as the page-truth source.
- Ignore the existing `<script type="application/ld+json">` blocks already on the page. Do not copy or be biased by them — generate schema independently from the visible content.
- Ignore boilerplate nav, footer, cookie banners, and search-form chrome that doesn't describe the page subject.

The page is the public homepage of Ian Lurie, an independent digital marketing consultant. Treat the homepage as describing the person (and/or their consulting offering), not as describing a separate organization or product.

URL: https://www.ianlurie.com/
