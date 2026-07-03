---
name: skill-registry-control
description: Manage the central Codex skill registry workflows. Use when registering GitHub skill repositories, importing or refreshing vendored skills, comparing same-name skills, choosing or overriding default sources, enabling/disabling skills for a project, syncing project .agents/skills symlinks, auditing registry state, or updating skill-groups.yaml.
---

# Skill Registry Control

## Overview

Use the central registry as the source of truth for reusable skills. Store imported skills under the registry, keep them inert by default, and activate them in a project only through registry-managed `.agents/skills` symlinks.

默认用中文汇报操作、判断和结果；命令、路径、skill 名称和上游原文保持原样。

## Required Context

Before changing the registry, inspect:

- `AGENTS.md`
- `README.md`
- `bin/skillctl`
- `skill-groups.yaml`
- the relevant `sources/<source>.yaml`
- the relevant `projects/<project>.yaml`

Read [references/registry-operations.md](references/registry-operations.md) when performing registration, same-name merge decisions, project activation, refresh, or audit work.

## Workflow

1. Check `git status --short --branch` in the registry before changes.
2. Prefer `bin/skillctl` over ad hoc filesystem edits.
3. Keep central storage and project activation separate:
   - Registering or importing a skill must not activate it in any project.
   - Project activation must be represented in `projects/<project>.yaml`.
   - `sync` should create or remove only registry-managed symlinks.
   - Use `bin/skillctl enable` for activation so explicit `/skill-name` dependencies are added to the same project manifest.
4. For same-name skills, compare variants before enabling:
   - Run `bin/skillctl alternatives <skill-name>`.
   - Use the merged default unless the user names a source or exact ID.
   - Use `--source <source>` for an intentional non-default source.
   - Preserve exact IDs when the user provides one.
5. After registry changes, run focused validation:
   - `bin/skillctl refresh-groups` after imports or metadata edits.
   - `bin/skillctl alternatives <skill-name>` for duplicate-name work.
   - `bin/skillctl audit <project> --allow-candidate` for project manifests using candidate skills.
6. Commit registry changes with a concise message unless the user says not to commit.

## Decision Rules

- Do not install all skills from a source unless the user explicitly asks for all.
- When the user asks for a broad term like `grilling`, resolve by skill name through `skill-groups.yaml`; do not link every matching source.
- When a skill body explicitly invokes another skill, for example `` `/grilling` `` or `` `/domain-modeling` ``, install those dependencies together with the parent skill.
- When multiple sources share the same skill name, explain the difference and recommendation in the final answer.
- Keep `analysis-only` and `deprecated` skills out of project activation unless explicitly requested.
- Use `--allow-candidate` only because current registry entries are intentionally still candidates; do not silently promote them to `approved`.
