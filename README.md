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
   bin/skillctl enable noeticai vendor/openai/example-skill
   ```

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

## Safety model

- The registry is outside `.agents/skills`, so storing a skill here does not
  make it visible to Codex.
- Only project symlinks under `.agents/skills` activate skills.
- `sync` only manages symlinks that point back into this registry.
- By default, `sync` refuses skills that are not marked `approved` in source
  metadata. Use `--allow-candidate` only for explicit experiments.

