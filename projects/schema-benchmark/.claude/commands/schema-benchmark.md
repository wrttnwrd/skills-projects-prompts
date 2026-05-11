---
description: Benchmark the schema-json-ld skill against fixtures and write a report
---

# /schema-benchmark

Run the schema-json-ld skill against every fixture in `fixtures/`, score each output against the gold rubric in `rubric.md`, and write a timestamped report to `results/`.

## Step 1 — Load fixtures

List every `.md` file in `fixtures/`. For each, parse:

- The frontmatter — gives you `gold` (expected primary types, must-include nested, forbidden types, must-have properties, topical-signal requirement, validator requirement) and optionally `url`.
- The body — everything after the `# Page content` heading. This is the page content the subagent will see.

## Step 2 — Generate schema for each fixture, in parallel

For each fixture, launch a subagent with the Agent tool (`subagent_type: general-purpose`). Send all subagent calls in a single message so they run in parallel.

Prompt template for each subagent:

> Generate JSON-LD schema for the page below. Follow the skill at `/Users/i.lurie/prompts-projects-skills/skills/schema/skill.md` exactly. The skill defines a mandatory 8-step workflow — execute every step, including Step 3 (verify each type against schema.org) and Step 7 (submit to validator.schema.org and report the result).
>
> Page content:
>
> {body of the fixture, verbatim}
>
> URL: {url from frontmatter, or "not provided"}
>
> Return exactly two things:
>
> 1. The final JSON-LD output wrapped in `<script type="application/ld+json">` tags.
> 2. A single line that starts with `VALIDATOR:` followed by either `clean`, `errors: <list>`, or `unreachable`.

**Critical**: do NOT pass the `gold` block or any expected-output information to the subagent. It must only see the page content.

## Step 3 — Score each output

For each subagent return, evaluate against the fixture's gold per `rubric.md`. Parse the JSON-LD from inside the `<script>` tags first.

- **Criterion 1 — Primary type correctness (40 pts)**: Find the primary type. If the output is a single object, it's the top-level `@type`. If the output uses `@graph`, the primary type is the first non-boilerplate entity (skip standalone `WebSite` / `Organization` that exist only to anchor `@id` references). Does it appear in `gold.primary_type_options`? Award 40 or 0.

- **Criterion 2 — Required nested types (15 pts)**: Walk every node in the output and collect every `@type` value (including nested). Does every type in `gold.must_include_nested` appear in that set? Award 15 or 0.

- **Criterion 3 — No forbidden types (15 pts)**: Same walk. If any type in `gold.forbidden_types` appears anywhere, award 0. Otherwise 15.

- **Criterion 4 — Required properties (10 pts)**: Does every property in `gold.must_have_properties` appear on the primary entity, or on a nested entity that logically owns it (e.g. `address` on a nested `PostalAddress`, `telephone` on a nested `ContactPoint`)? Award 10 or 0.

- **Criterion 5 — Topical signals (5 pts)**: If `gold.must_have_topical_signals` is true, does the primary entity have `about` or `mentions` with at least one named subject? Award 5 or 0. If false, award 5 automatically.

- **Criterion 6 — Validator clean (10 pts)**: Read the subagent's `VALIDATOR:` line. `clean` = 10, `errors` = 0, `unreachable` = N/A (re-normalize this fixture's score).

- **Criterion 7 — No invented properties (5 pts)**: Pick three less-common properties used in the output (skip `name`, `url`, `description`, `@type`, `@id`, `@context`, `headline`, `image`). Fetch `https://schema.org/<TypeName>` for the type each property is used on, and confirm the property is listed. All three must exist for full credit; one invented = 0. If fewer than three less-common properties exist, check all of them.

Compute the fixture score: `(sum of awarded points / total possible) × 100`. Re-normalize if any criterion was N/A.

## Step 4 — Roll up

- Overall score = mean of fixture scores.
- Per-criterion pass rate = % of fixtures that received full points for that criterion.

## Step 5 — Write the report

Write to `results/YYYY-MM-DD-HHMM.md` using local time. Use this structure:

```markdown
# schema-benchmark report — {timestamp}

**Overall score: XX / 100**

## Per-fixture scores

| Fixture | Score | Primary type chosen | Validator | Notes |
|---|---|---|---|---|
| saas-homepage | 95 | SoftwareApplication | clean | — |
| blog-post | 70 | Article | clean | expected BlogPosting; criterion 1 failed |
| ...

## Per-criterion pass rates

| Criterion | Pass rate |
|---|---|
| 1. Primary type correctness | 4/6 (67%) |
| 2. Required nested types | 5/6 (83%) |
| 3. No forbidden types | 6/6 (100%) |
| 4. Required properties | 5/6 (83%) |
| 5. Topical signals | 5/6 (83%) |
| 6. Validator clean | 6/6 (100%) |
| 7. No invented properties | 4/6 (67%) |

## Notable failures

- **{fixture}**: chose `{X}` when `{Y}` was expected. {Why this matters.}
- ...

## Recommendations

- {2–4 bullets on what to fix in the skill, based on the lowest-scoring criteria.}
```

## Step 6 — Cleanup

If you created any intermediate JSON files while parsing or scoring, delete them.

## Step 7 — Report to user

Print the overall score and the relative path to the full report. Example:

> Overall: 82/100. Full report at results/2026-05-11-1430.md
> Weakest criterion: type correctness (67% pass rate) — see blog-post and pricing-page failures.

## Notes

- Parallelization is mandatory for the generation step (Step 2). Sequential runs are slow enough that the benchmark won't get used.
- Be honest in scoring. The benchmark exists to find weaknesses in the skill, not to make the skill look good. When in doubt, score against the gold as written; if the gold is wrong, fix the gold file and re-run.
- If `VALIDATOR: unreachable` shows up across most fixtures, the skill's Step 7 isn't actually executing — flag that in the report's Recommendations as the highest-priority fix.
