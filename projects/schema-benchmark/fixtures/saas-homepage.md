---
name: SaaS homepage
archetype: saas-homepage
url:
gold:
  primary_type_options: [SoftwareApplication, Organization]
  must_include_nested: [Organization]
  forbidden_types: [Article, BlogPosting, NewsArticle, HowTo, Recipe, Event, FAQPage, Service]
  must_have_properties: [name, url, description]
  must_have_topical_signals: true
  validator_must_pass: true
notes: |
  Homepage rule — expect full Organization detail. SoftwareApplication is preferred for a clear
  SaaS positioning, but Organization with the full homepage detail is also acceptable.
---

# Page content

**Title**: Acme Cloud — Ship Faster

**Hero**: The fastest CI/CD platform for engineering teams. Deploy in minutes, not hours.

**Pricing snippet**: Starter $29/mo • Growth $99/mo • Enterprise custom

**About**: Acme Cloud is the developer infrastructure company powering 10,000+ engineering teams worldwide. Founded in 2018. Based in San Francisco.

**Social**: Twitter @acmecloud • LinkedIn linkedin.com/company/acmecloud • GitHub github.com/acmecloud

**Topics covered**: continuous integration, continuous deployment, developer infrastructure, DevOps

**URL**: https://acmecloud.example.com
