---
name: tdd
description: 当用户要 test-first 构建功能或修 bug，强调 red-green-refactor、集成测试或通过公共接口验证时使用。 当没有可测试行为、用户要求先快速探索，或只需要文档和配置修改时不要用。
---

# 中文导读

- 使用场景：当用户要 test-first 构建功能或修 bug，强调 red-green-refactor、集成测试或通过公共接口验证时使用。
- 不适用：当没有可测试行为、用户要求先快速探索，或只需要文档和配置修改时不要用。

# 上游说明原文

# TDD

Tests verify **behavior through public interfaces**, not implementation. Good tests survive refactors; bad tests break on rename.

See [tests.md](tests.md) and [mocking.md](mocking.md) for examples.

## Anti-pattern: horizontal slices

Don't write all tests then all code. One behavior: RED → GREEN → repeat.

## Workflow

1. **Plan** — read `CONTEXT.md`/ADRs. Confirm interface changes and behaviors to test with user.
2. **Tracer bullet** — one test, one minimal implementation, passes.
3. **Loop** — one test at a time; only code to pass current test; no speculation.
4. **Refactor** — only when GREEN; see [refactoring.md](refactoring.md).

## Per-cycle checklist

- [ ] Describes behavior, not implementation
- [ ] Uses public interface only
- [ ] Minimal code for this test
