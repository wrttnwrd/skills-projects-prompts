---
name: Agency service detail page
archetype: service-page
url:
gold:
  primary_type_options: [Service, ProfessionalService]
  must_include_nested: [Organization]
  forbidden_types: [Product, Offer, Article, BlogPosting, NewsArticle, HowTo, Recipe, Event, FAQPage, SoftwareApplication]
  must_have_properties: [name, provider, description]
  must_have_topical_signals: true
  validator_must_pass: true
notes: |
  No price displayed for the service — agencies usually quote custom. Forbidden: Offer or Product
  with a price (the agency wants leads, not e-commerce semantics). The forbidden Article/BlogPosting
  pattern matters: this is a service page, not editorial content.
---

# Page content

**Title**: Brand Strategy & Positioning — Northstar Consulting

**Hero**: We help B2B SaaS companies define a brand position the market actually remembers.

**What you get**: 6-week engagement. Brand audit, competitive positioning workshop, messaging architecture, launch playbook.

**Who it's for**: Series B–D SaaS companies, $10M–$100M ARR.

**About the firm**: Northstar Consulting. Founded 2017. New York and remote. Past clients include three Fortune 500 brands and a dozen mid-market SaaS leaders.

**Contact**: hello@northstar.example.com

**URL**: https://northstar.example.com/services/brand-strategy

**Topics covered**: brand strategy, brand positioning, B2B SaaS marketing, messaging architecture
