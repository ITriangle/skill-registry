# Skill Documentation Locales

Localized skill documentation is stored under:

```text
locales/<locale>/vendor/<source>/<skill>/
```

These files are review-only mirrors. Skill discovery, dependency resolution,
and project activation always use `skills/vendor/`.

Each mirror contains translated Markdown/TXT documentation plus a generated
`.translation.yaml` with source and translation SHA-256 hashes. Do not copy or
translate licenses, scripts, or code. After editing a mirror, run:

```bash
bin/skillctl translation-stamp <skill-id> --locale <locale>
bin/skillctl translation-audit --locale <locale>
```

A mirror must translate the complete natural-language content. Chinese summaries
followed by English source text, pure-English copies, and placeholder sections
such as `# 上游说明原文` fail the audit.
