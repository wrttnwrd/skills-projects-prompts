# Scoring rubric

Each fixture is scored out of 100. The overall benchmark score is the mean across all fixtures.

## Criteria

| # | Criterion | Points | Pass condition |
|---|---|---|---|
| 1 | Primary type correctness | 40 | Output's primary type appears in fixture's `gold.primary_type_options` |
| 2 | Required nested types present | 15 | Every type in `gold.must_include_nested` appears somewhere in the output (top-level or nested) |
| 3 | No forbidden types | 15 | No type in `gold.forbidden_types` appears anywhere in the output |
| 4 | Required properties present | 10 | Every property in `gold.must_have_properties` appears on the primary entity, or on a nested entity that logically owns it (e.g. `address` on a nested `PostalAddress`) |
| 5 | Topical signals | 5 | If `gold.must_have_topical_signals` is true, `about` or `mentions` appears on the primary entity with at least one named subject. If false, full credit automatically. |
| 6 | Validator clean | 10 | `validator.schema.org` reports zero errors. Warnings do not count against this criterion. |
| 7 | No invented properties | 5 | Spot-check three less-common properties used in the output against schema.org. Skip `name`, `url`, `description`, `@type`, `@id`, `@context`. All three must exist on the type they're used on. |

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
