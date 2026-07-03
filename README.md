# Skill Registry

Central Git-managed registry for Codex skills.

This repository stores and reviews skills, but it is not a Codex discovery
location. Skills only become active in a project when `skillctl sync` creates
symlinks under that project's `.agents/skills` directory.

## Layout

- `skills/vendor/<source>/<skill>/` - vendored approved or candidate skills.
- `sources/<source>.yaml` - upstream provenance and import metadata.
- `projects/<project-slug>.yaml` - project activation manifests.
- `analysis/<source>/<skill>.md` - skill review reports.
- `skill-groups.yaml` - merged same-name skill index and default source.
- `bin/skillctl` - import, analyze, audit, enable, disable, and sync command.

## Basic workflow

1. Import a skill from a pinned upstream ref:

   ```bash
   bin/skillctl import \
     --source openai \
     --repo https://github.com/openai/skills.git \
     --ref main \
     --skill-path skills/.curated/example-skill \
     --id vendor/openai/example-skill
   ```

2. Analyze the skill:

   ```bash
   bin/skillctl analyze vendor/openai/example-skill
   ```

3. Mark it approved in `sources/<source>.yaml` after review.

4. Add it to a project:

   ```bash
   bin/skillctl enable noeticai example-skill
   ```

   `enable` also installs explicit skill dependencies referenced from
   backticked slash commands in `SKILL.md`, such as `` `/domain-modeling` ``.
   Dependencies are resolved from the same source when available, then from the
   merged default in `skill-groups.yaml`.

5. Synchronize symlinks into the target project:

   ```bash
   bin/skillctl sync noeticai
   ```

## Project manifest

Project manifests live in `projects/<project-slug>.yaml`:

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
bin/skillctl alternatives grilling
```

Install the default variant:

```bash
bin/skillctl enable project-1 grilling
```

Install a variant from a specific source:

```bash
bin/skillctl enable project-1 grilling --source yugasun
```

Exact IDs still work when you need a fully explicit manifest:

```bash
bin/skillctl enable project-1 vendor/yugasun/grilling
```

After importing or manually vendoring skills, refresh the merge index:

```bash
bin/skillctl refresh-groups
```

When adding a same-name skill to a project, prefer the skill name first so the
merged default is used:

```bash
bin/skillctl enable project-1 grilling
```

Use `--source` only when the project intentionally wants a non-default source.

## Safety model

- The registry is outside `.agents/skills`, so storing a skill here does not
  make it visible to Codex.
- Only project symlinks under `.agents/skills` activate skills.
- `sync` only manages symlinks that point back into this registry.
- `audit` reports project manifests that omit explicit skill dependencies.
- By default, `sync` refuses skills that are not marked `approved` in source
  metadata. Use `--allow-candidate` only for explicit experiments.
