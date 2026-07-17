---
name: lean
description: 当用户要把工作拆成最小可验证增量，优先快速学习、降低浪费并持续收敛时使用。 当任务已经被明确拆好，或用户只要一次性执行不需要精益拆解时不要用。
---

# 中文导读

- 使用场景：当用户要把工作拆成最小可验证增量，优先快速学习、降低浪费并持续收敛时使用。
- 不适用：当任务已经被明确拆好，或用户只要一次性执行不需要精益拆解时不要用。

# 上游说明原文

# Lean

Adapted from ponytail discipline. Lazy means efficient, not careless. Active during **delivery** in the aiops bundle; **off** during grill/alignment.

## Ladder

Stop at the first rung that holds:

1. Does this need to exist? (YAGNI)
2. Stdlib does it?
3. Native platform feature?
4. Already-installed dependency?
5. One line?
6. Minimum code that works

## Rules

- No unrequested abstractions, boilerplate, or speculative "for later" code
- Deletion over addition; shortest working diff
- Mark deliberate shortcuts: `// lean: <ceiling and upgrade path>`

## Output

Code first, then at most three lines: what was skipped, when to add it.

## Never cut

Trust-boundary validation, data-loss prevention, security, accessibility, explicitly requested behavior.

## Intensity

`/lean lite|full|ultra` — default **full**. Off: "stop lean" / "normal mode".
