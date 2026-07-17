---
name: explore
description: 当用户要自由讨论想法、比较选项、梳理权衡，且不希望提交文件产物时使用。 当用户已经要求实现、写文件、提交改动或运行严格流程时不要用。
---

# 中文导读

- 使用场景：当用户要自由讨论想法、比较选项、梳理权衡，且不希望提交文件产物时使用。
- 不适用：当用户已经要求实现、写文件、提交改动或运行严格流程时不要用。

# 上游说明原文

Exploration mode — a conversation, not a generator.

## Process

1. **Listen** — understand the user's idea or question.
2. **Ground** — explore codebase if relevant (use code-graph when available).
3. **Challenge** — name tradeoffs, alternatives, risks.
4. **Synthesize** — summarize options with pros/cons (no decision forced).

## Rules

- No artifacts written to `.scratch/`.
- No phases advanced.
- Output is a structured comparison (markdown table or decision matrix) in chat only.
- User decides whether to proceed to alignment after exploration.
