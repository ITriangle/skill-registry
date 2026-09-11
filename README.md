# Skill Registry

Central Git-managed registry for Codex skills.

This repository stores and reviews skills and always-on rules, but it is not a
Codex discovery location. Skills become active when `regctl sync` creates
symlinks under a project's `.agents/skills` directory. Global prompts for
Cursor, Codex, and Claude are published only from the `user-home` project.

## Layout

- `skills/vendor/<source>/<skill>/` - vendored approved or candidate skills.
- `rules/vendor/<source>/<rule>/RULE.mdc` - always-on rules (not skills).
- `publish/codex/AGENTS.md` - Codex global AGENTS.md source (symlink target).
- `globals.yaml` - registered global prompt files.
- `sources/<source>.yaml` - upstream provenance and import metadata.
- `projects/<project-slug>.yaml` - project activation manifests (local, not committed).
- `analysis/<source>/<skill>.md` - skill review reports.
- `locales/zh-CN/vendor/<source>/<skill>/` - read-only Chinese documentation mirrors.
- `skill-groups.yaml` - merged same-name skill index and default source.
- `bin/regctl` - import, analyze, audit, enable, disable, and sync command.

## Basic workflow

1. Import a skill from a pinned upstream ref:

   ```bash
   bin/regctl import \
     --source openai \
     --repo https://github.com/openai/skills.git \
     --ref main \
     --skill-path skills/.curated/example-skill \
     --id vendor/openai/example-skill
   ```

2. Analyze the skill:

   ```bash
   bin/regctl analyze vendor/openai/example-skill
   ```

3. Mark it approved in `sources/<source>.yaml` after review.

4. Add it to a project:

   ```bash
   bin/regctl enable noeticai example-skill
   ```

   `enable` also installs explicit skill dependencies referenced from
   backticked slash commands in `SKILL.md`, such as `` `/domain-modeling` ``.
   Dependencies are resolved from the same source when available, then from the
   merged default in `skill-groups.yaml`.

5. Synchronize symlinks into the target project:

   ```bash
   bin/regctl sync noeticai
   ```

## Chinese documentation mirrors

Every registered skill has a Chinese documentation mirror under
`locales/zh-CN/vendor/<source>/<skill>/`. Mirrors include `SKILL.md` and other
Markdown/TXT documentation, but exclude licenses, scripts, and code. They are
review-only artifacts: discovery and project sync continue to use the English
files under `skills/vendor/`.

After importing or editing a vendored skill, update its mirror and stamp the
reviewed source/translation hashes:

```bash
bin/regctl translation-status vendor/openai/example-skill
bin/regctl translation-stamp vendor/openai/example-skill
bin/regctl translation-audit
```

`import`, `refresh-groups`, project `audit`, and `sync` fail while any required
Chinese mirror is missing or stale. The audit also rejects placeholder sections,
English-only mirrors, and translations that remain substantially identical to
the English prose; a matching hash alone is not considered a completed translation.

## Project manifest

Project manifests live in `projects/<project-slug>.yaml`:

```yaml
project: user-home
path: /Users/you
adapters:
  skills: ~/.agents/skills
  cursor_rules: ~/.cursor/rules
  codex_agents: ~/.codex/AGENTS.md
  claude_agents: ~/.claude/CLAUDE.md
skills:
  - id: vendor/openai/example-skill
rules:
  - id: vendor/tsoul/coding-lenses
```

`enable` accepts `--kind skill|rule`. Rules can only be enabled on a project that
defines global adapters. `sync` links Cursor `.mdc` files, points
`~/.codex/AGENTS.md` at `publish/codex/AGENTS.md`, and writes a managed block
into `~/.claude/CLAUDE.md`. It does not write repository `AGENTS.md` files.

```yaml
project: noeticai
path: /absolute/path/to/project
skills:
  - id: vendor/openai/example-skill
```

`path` must point at the project root. `sync` creates links at:

```text
<project>/.agents/skills/<skill-directory-name>
```

## Same-name skills

When two sources provide a skill with the same `name`, the registry merges them
in `skill-groups.yaml`. Each group has one `default_id`; installing by skill
name uses that default so only one variant becomes active in the project.

Registration and refresh must analyze the variants before they are used by a
project. `skill-groups.yaml` records:

- `variants`: every registered implementation of the same skill name.
- `difference`: source/status/profile differences, including references and scripts.
- `recommendation`: the default choice and when to override it.
- `default_id`: the variant installed when a project asks for the skill by name.

Show the available variants and their differences:

```bash
bin/regctl alternatives grilling
```

Install the default variant:

```bash
bin/regctl enable project-1 grilling
```

Install a variant from a specific source:

```bash
bin/regctl enable project-1 grilling --source yugasun
```

Exact IDs still work when you need a fully explicit manifest:

```bash
bin/regctl enable project-1 vendor/yugasun/grilling
```

After importing or manually vendoring skills, refresh the merge index:

```bash
bin/regctl refresh-groups
```

When adding a same-name skill to a project, prefer the skill name first so the
merged default is used:

```bash
bin/regctl enable project-1 grilling
```

Use `--source` only when the project intentionally wants a non-default source.

## Safety model

- The registry is outside `.agents/skills`, so storing a skill here does not
  make it visible to Codex.
- Only project symlinks under `.agents/skills` activate skills.
- `sync` only manages symlinks that point back into this registry.
- Rules publish only through `user-home` global adapters; `sync` does not write
  repository `AGENTS.md`, `CLAUDE.md`, or `.cursor/rules`.
- `audit` reports project manifests that omit explicit skill dependencies.
- Translation mirrors never become project symlink targets.
- By default, `sync` refuses skills that are not marked `approved` in source
  metadata. Use `--allow-candidate` only for explicit experiments.
