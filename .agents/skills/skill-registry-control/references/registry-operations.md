# Registry Operations

## Register A New Git Source

1. Clone the upstream repository to `/private/tmp`.
2. Record the exact commit with `git rev-parse HEAD`.
3. Find skill folders with `find <repo> -name SKILL.md`.
4. Inspect license and README.
5. Vendor selected skill directories under `skills/vendor/<source>/`.
6. Add or update `sources/<source>.yaml` with:
   - `source`
   - `repo`
   - `ref`
   - `license`
   - `skills[].id`
   - `skills[].upstream_path`
   - `skills[].status`
   - `skills[].imported_at`
7. Run `bin/regctl analyze <skill-id>` for each imported skill.
8. Run `bin/regctl refresh-groups`.
9. Validate duplicate-name output with `bin/regctl alternatives <name>` when applicable.

Before steps 8-9, translate all Markdown/TXT documentation except licenses into
`locales/zh-CN/<skill-id>/`, run `bin/regctl translation-stamp <skill-id>`,
and require `bin/regctl translation-audit` to pass. An import may update the
English source and then exit non-zero until this mirror work is complete.
Translate the full natural-language content; do not retain an English body under
a Chinese guide or stamp an untranslated copy.

Default status guidance:

- Use `candidate` for newly registered usable skills.
- Use `analysis-only` for experimental, in-progress, personal-only, or deprecated upstream folders.
- Use `approved` only after review.
- Use `deprecated` only when the registry should retain but avoid the skill.

## Same-Name Skill Policy

Registration must merge same-name skills into `skill-groups.yaml`.

For each duplicate group:

- Compare sources, statuses, descriptions, scripts, and reference files.
- Keep exactly one `default_id`.
- Prefer an existing default when it still exists.
- Prefer `approved` over `candidate`, `candidate` over `analysis-only`, and `analysis-only` over `deprecated`.
- Among equal statuses, prefer the variant with a clearer trigger description and useful references.
- Preserve source override with `bin/regctl enable <project> <skill-name> --source <source>`.

Use:

```bash
bin/regctl alternatives <skill-name>
```

to show the difference and recommendation before enabling a duplicate-name skill.

## Enable A Skill For A Project

Prefer installing by skill name:

```bash
bin/regctl enable <project> <skill-name>
bin/regctl sync <project> --allow-candidate
```

`enable` expands explicit skill dependencies found in `SKILL.md`, such as
`` `/grilling` `` or `` `/domain-modeling` ``, and writes those dependency IDs
to the same project manifest. It prefers a dependency from the same source as
the parent skill when that source provides exactly one matching skill name; if
not, it falls back to the merged default in `skill-groups.yaml`.

Use source override only when requested:

```bash
bin/regctl enable <project> <skill-name> --source <source>
bin/regctl sync <project> --allow-candidate
```

Use exact IDs only when the user gives one or a manifest must be fully explicit:

```bash
bin/regctl enable <project> vendor/<source>/<skill>
bin/regctl sync <project> --allow-candidate
```

After sync, verify:

```bash
find <project>/.agents/skills -maxdepth 1 -type l -print | sort
bin/regctl audit <project> --allow-candidate
```

Both commands enforce a complete, current `zh-CN` mirror before inspecting or
changing project links. The mirror itself is never linked into a project.

If `audit` reports `missing dependency`, rerun `bin/regctl enable <project>
<skill-name>` for the parent skill so the manifest is repaired through normal
resolution rules.

## Enable A Rule For User-Home

Always-on rules are not skills. Enable them only on a project that defines
global adapters (`cursor_rules`, `codex_agents`, `claude_agents`), currently
`user-home`:

```bash
bin/regctl enable user-home coding-lenses --kind rule
bin/regctl sync user-home --allow-candidate
```

`sync` links `~/.cursor/rules/<name>.mdc` to `rules/.../RULE.mdc`, points
`~/.codex/AGENTS.md` at `publish/codex/AGENTS.md`, and writes a managed HTML
block into `~/.claude/CLAUDE.md`. Rules with `alwaysApply: false` go to Cursor
only. Never write a git repository's `AGENTS.md`.

## Final Response Checklist

Report:

- Which source and commit were registered, if applicable.
- Which skill ID or default source was chosen.
- Whether alternatives existed and why the default was recommended.
- Which project manifest changed.
- How many symlinks were created or removed.
- The commit hash for registry changes.
