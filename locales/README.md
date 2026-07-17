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
