---
name: E-commerce product detail
archetype: product-detail
url:
gold:
  primary_type_options: [Product]
  must_include_nested: [Offer, Brand]
  forbidden_types: [Article, BlogPosting, NewsArticle, HowTo, Recipe, Event, FAQPage, Service, SoftwareApplication]
  must_have_properties: [name, image, description, offers, brand]
  must_have_topical_signals: false
  validator_must_pass: true
notes: |
  Clear-cut Product page — has a price, SKU, brand, single purchasable physical item. Topical
  signals are optional here because the product itself is the subject. AggregateRating is also
  expected since reviews are present, but it's not in must_include_nested to keep that list focused
  on the structural essentials.
---

# Page content

**Title**: Stanley Quencher H2.0 FlowState Tumbler — 40 oz, Charcoal

**Image**: https://shop.example.com/img/quencher-charcoal-40.jpg

**Price**: $44.99 USD

**Availability**: In stock

**Brand**: Stanley

**SKU**: STN-QH2-40-CHR

**Description**: 40-ounce insulated stainless steel tumbler with FlowState lid and rotating handle. Keeps drinks cold for 11 hours, iced for 2 days.

**Rating**: 4.6 / 5 across 12,847 reviews

**URL**: https://shop.example.com/stanley-quencher-40oz-charcoal
