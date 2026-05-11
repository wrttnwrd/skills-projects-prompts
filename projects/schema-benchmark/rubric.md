# Scoring rubric

Each fixture is scored out of 100. The overall benchmark score is the mean across all fixtures.

## Criteria

| # | Criterion | Points | Pass condition |
|---|---|---|---|
| 1 | Primary type correctness | 30 | Output's primary type appears in fixture's `gold.primary_type_options` |
| 2 | Required nested types present | 15 | Every type in `gold.must_include_nested` appears somewhere in the output (top-level or nested) |
| 3 | No forbidden types | 15 | No type in `gold.forbidden_types` appears anywhere in the output |
| 4 | Required properties present | 10 | Every property in `gold.must_have_properties` appears on the primary entity, or on a nested entity that logically owns it (e.g. `address` on a nested `PostalAddress`) |
| 5 | Topical signals | 5 | If `gold.must_have_topical_signals` is true, the primary entity carries topical signals using the right schema.org property for its type family (see table below) with at least one named subject. If false, full credit automatically. |
| 6 | Validator clean | 10 | `validator.schema.org` reports zero errors. Warnings do not count against this criterion. |
| 7 | No invented properties | 5 | Spot-check three less-common properties used in the output against schema.org. Skip `name`, `url`, `description`, `@type`, `@id`, `@context`. All three must exist on the type they're used on. |
| 8 | Proper nesting | 10 | All three sub-checks pass (see below). |

### Criterion 5 — Topical signals (detail)

`about` is not valid on every type, so the property that satisfies criterion 5 depends on the primary entity's type family:

| Primary entity family | Property that satisfies criterion 5 |
|---|---|
| `CreativeWork` subtypes (`Article`, `BlogPosting`, `NewsArticle`, `WebPage`, `FAQPage`, `HowTo`, `Recipe`, `VideoObject`, etc.) | `about` and/or `mentions` |
| `Organization` family (`Organization`, `LocalBusiness` and subtypes, `Corporation`, `EducationalOrganization`, etc.) | `knowsAbout` |
| `Service` / `ProfessionalService` | `serviceType` plus `category` and/or `audience` |
| `Product` / `SoftwareApplication` | `category` and/or `keywords` (rarely required — usually `must_have_topical_signals: false` here) |
| `Person` | `knowsAbout` |
| `Event` | `about` |

The signal must be on the **primary** entity. Topics on a sibling `WebPage` only do not satisfy this criterion — that's the failure mode the criterion was designed to catch.

### Criterion 8 — Proper nesting (detail)

Award 10 if **all** of these hold; 0 otherwise:

1. **Primary at the root.** The primary entity is at the JSON root, or is the first non-anchor entity inside `@graph` (anchors = standalone `WebSite` or site-identity `Organization`).
2. **No orphans.** Every non-primary top-level entity (sibling of root, or inside `@graph`) is either (a) a recognized site-wide anchor — standalone `WebSite` or site-identity `Organization` — or (b) referenced from the primary entity via an `@id` reference somewhere in its property tree.
3. **Typed relationships, not bare strings.** Where a natural-secondary-entity relationship is present on the primary entity (`author`, `publisher`, `brand`, `offers`, `address`, `contactPoint`, `aggregateRating`, `review`, `performer`, `hiringOrganization`, `provider`, `location`), its value is either an inline nested object with `@type`, or an `@id` reference — never a bare string.

If the relationship is absent entirely, criterion 4 catches that. Criterion 8 only fires when relationships are present but expressed flatly.

## Scoring rules

- **All-or-nothing per criterion.** No partial credit unless noted. Partial credit invites the agent to argue itself into a higher score; binary checks are auditable.
- **Forbidden types are a hard zero on criterion 3, regardless of how many forbidden types appear.** One is one too many.
- **If the validator cannot be reached**, mark criterion 6 as N/A and re-normalize the fixture score (exclude its 10 points from both numerator and denominator).
- **If there aren't three less-common properties to spot-check** on criterion 7, check all available less-common properties; award full credit if none are invented.

## Roll-up

- **Per fixture**: sum of points awarded / total possible points × 100. Re-normalize if any criterion is N/A.
- **Overall**: mean of fixture scores.
- **Per criterion**: % of fixtures that received full points on that criterion. Useful for spotting systematic weaknesses.

## Targets

- **80+**: skill is in good shape.
- **60–79**: type selection or property fidelity needs work — check criterion 1 and 7 roll-ups first.
- **<60**: skill workflow probably isn't being followed end-to-end; check whether the validator pass (Step 7 of the skill) is happening.

## On honesty

The benchmark is useful only if scoring is strict. When a fixture is on the edge, default to scoring it against the gold as written, not against the most charitable reading of the agent's output. If the gold itself is wrong, fix the gold and re-run — don't soften the scoring.
