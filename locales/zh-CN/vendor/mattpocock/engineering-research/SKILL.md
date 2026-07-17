---
name: research
description: 当用户要基于高可信一手资料研究技术问题、API 事实或背景信息，并把结论写成 Markdown 时使用。 当问题可从本地代码直接回答，或用户要立即实现而非调研报告时不要用。
---

# 中文导读

- 使用场景：当用户要基于高可信一手资料研究技术问题、API 事实或背景信息，并把结论写成 Markdown 时使用。
- 不适用：当问题可从本地代码直接回答，或用户要立即实现而非调研报告时不要用。

# 上游说明原文

Spin up a **background agent** to do the research, so you keep working while it reads.

Its job:

1. Investigate the question against **primary sources** — official docs, source code, specs, first-party APIs — not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Write the findings to a single Markdown file, citing each claim's source.
3. Save it where the repo already keeps such notes; match the existing convention, and if there is none, put it somewhere sensible and say where.
