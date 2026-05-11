---
name: Real FAQ page with Q&A pairs
archetype: faq-page
url:
gold:
  primary_type_options: [FAQPage]
  must_include_nested: [Question, Answer]
  forbidden_types: [Article, BlogPosting, Product, Offer, HowTo, Recipe, Event, Service, SoftwareApplication]
  must_have_properties: [mainEntity]
  must_have_topical_signals: false
  validator_must_pass: true
notes: |
  Genuine FAQ — has explicit question-answer pairs visible on the page. Each Question should have
  an acceptedAnswer of type Answer.
---

# Page content

**Title**: Acme Cloud Pricing FAQ

**URL**: https://acmecloud.example.com/pricing/faq

**Q: Can I switch plans at any time?**
A: Yes. Plan changes take effect immediately and we prorate the difference on your next invoice.

**Q: What payment methods do you accept?**
A: All major credit cards (Visa, Mastercard, Amex, Discover), and ACH for annual Enterprise plans.

**Q: Is there a free trial?**
A: Every paid plan includes a 14-day free trial. No credit card required to start.

**Q: Do you offer discounts for nonprofits or education?**
A: Yes — 50% off all plans for registered nonprofits and accredited educational institutions. Contact sales for details.

**Q: How do I cancel my subscription?**
A: From your account settings, click "Billing" → "Cancel subscription." You retain access through the end of your current billing period.
