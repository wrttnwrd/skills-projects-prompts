# schema-benchmark

A benchmark for the `schema-json-ld` skill at `../../skills/schema/skill.md`. Runs the skill against a set of fixture pages, scores each output against a gold rubric, and rolls up to an overall score.

## What it measures

See `rubric.md` for the full scoring breakdown. Headline criteria:

- **Primary type correctness** — did the agent pick a type the gold accepts?
- **Required nested types present** — did it nest the right secondary entities?
- **No forbidden types** — did it avoid Product on non-priced pages, HowTo on non-tutorials, etc.?
- **Required properties present** — name, url, key type-specific properties.
- **Topical signals** — `about` / `mentions` for knowledge-graph / LLM visibility.
- **Validator pass** — `validator.schema.org` reports no errors.
- **No invented properties** — properties used actually exist on schema.org for their type.

## How to run

From inside this directory:

```
/schema-benchmark
```

The command generates schema for every fixture in parallel, scores each output, and writes a timestamped report to `results/`.

## Layout

```
fixtures/    one .md file per page archetype — frontmatter holds the gold, body holds the page content
rubric.md    per-criterion scoring rules
results/     timestamped reports (gitignored)
.claude/     slash command definition
```

## Adding fixtures

Copy any file in `fixtures/`, rename it, edit the frontmatter (`gold` block) and the page content. The benchmark will pick it up automatically.

Keep the body of a fixture in a "Page content" section. Only that section is passed to the generating subagent — the gold stays hidden from it.

## Updating the gold

When schema.org evolves or the skill's preferred type for an archetype changes, update affected fixtures. Keep the gold strict but reasonable — if multiple types are genuinely acceptable, list them all in `primary_type_options`.

## Why this lives in a project, not the skill

The skill is "how to generate schema." The benchmark is "verify the skill does that well." Different workflow, different lifecycle. Keeping them separate stops the skill from bloating every load and keeps the benchmark's fixtures and rubric in a place where they can be versioned independently.
