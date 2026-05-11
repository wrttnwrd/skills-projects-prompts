---
name: Local dentist office homepage
archetype: local-business
url:
gold:
  primary_type_options: [Dentist, LocalBusiness, MedicalBusiness]
  must_include_nested: [PostalAddress]
  forbidden_types: [Product, Offer, Article, BlogPosting, NewsArticle, HowTo, Recipe, Event, FAQPage]
  must_have_properties: [name, address, telephone, url]
  must_have_topical_signals: true
  validator_must_pass: true
notes: |
  Strong preference for the most specific subtype — Dentist. LocalBusiness is acceptable but
  loses the specificity advantage. MedicalBusiness acceptable as a parent. Anything more generic
  (Organization, Place) should fail criterion 1.
---

# Page content

**Title**: Bright Smile Dental — Family Dentistry in Portland, OR

**Hero**: Gentle, modern family dentistry in Northwest Portland. Accepting new patients.

**Address**: 1234 NW 23rd Ave, Portland, OR 97210

**Phone**: (503) 555-0142

**Hours**: Mon–Thu 8am–5pm, Fri 8am–noon

**Services**: Cleanings, fillings, crowns, Invisalign, pediatric dentistry

**About**: Dr. Maria Rodriguez has practiced in NW Portland since 2010. Bright Smile is a two-dentist family practice serving the Pearl District and surrounding neighborhoods.

**URL**: https://brightsmilepdx.example.com

**Topics covered**: family dentistry, cosmetic dentistry, Invisalign, Portland Oregon dentist
