# Sources

Each source metadata file records where vendored skills came from and how they
were reviewed.

Example:

```yaml
source: openai
repo: https://github.com/openai/skills.git
ref: main
skills:
  - id: vendor/openai/example-skill
    upstream_path: skills/.curated/example-skill
    status: approved
    imported_at: 2026-07-03T00:00:00Z
```

Supported statuses:

- `analysis-only`
- `candidate`
- `approved`
- `deprecated`

