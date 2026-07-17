---
name: code-graph
description: 当用户需要为代码库建立或查询结构化代码图，分析依赖、符号、调用关系或架构路径时使用。 当问题能通过普通搜索阅读解决，或不需要构建代码图索引时不要用。
---

# 中文导读

- 使用场景：当用户需要为代码库建立或查询结构化代码图，分析依赖、符号、调用关系或架构路径时使用。
- 不适用：当问题能通过普通搜索阅读解决，或不需要构建代码图索引时不要用。

# 上游说明原文

# Code Graph

Build, query, and incrementally update a persistent knowledge graph for the target project. **Infrastructure** — other skills consume it via query; Flow Conductor checks freshness on session start.

## Two-tier extraction

| Tier | Tool | Role |
| --- | --- | --- |
| **Structural** | [graphify](https://github.com/safishamsi/graphify) | AST nodes, edges, communities, confidence — deterministic |
| **Semantic** | Model | Purpose, depth, impact — contextual |

graphify parses; the model annotates. Never replace graphify structural data with grep guesses.

## Prerequisites

[prerequisites.md](prerequisites.md) — install `graphifyy` via uv/pipx/pip. Non-blocking if user declines.

## Storage

| Path | Source | Purpose |
| --- | --- | --- |
| `graphify-out/graph.json` | graphify | Structural graph |
| `.scratch/graph/annotations.json` | Model | Semantic layer |

Do not copy `graph.json` into `.scratch/`. Schema: [graph-schema.md](graph-schema.md).

## Operations

Detailed steps: [build-steps.md](build-steps.md).

- **`/code-graph build`** — full scan + semantic annotation
- **`/code-graph query <subcommand>`** — read-only; patterns in [query-patterns.md](query-patterns.md)
- **`/code-graph update`** — incremental via graphify cache

## Constraints

- graphify is the structural backbone — no grep-based dependency guessing
- Model adds semantic layer only; never override graphify edges
- Prefer `update` over `build` when graph exists
- Non-blocking on graphify failure — warn and continue
- Confidence-aware: EXTRACTED (1.0) vs INFERRED (0.5) vs AMBIGUOUS (0.2)

## Flow Conductor

`aiops-graph.js` hook suggests `/code-graph build` when stale. **Architecture health** runs `graph_build` phase first (`phases.py`) — build when missing/stale, skip when fresh, user may decline (organic fallback in `/improve-codebase-architecture`).
