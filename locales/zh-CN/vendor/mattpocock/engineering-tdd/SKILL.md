---
name: tdd
description: 测试驱动开发。当用户想测试优先构建功能或修 bug、提到「red-green-refactor」，或想要集成测试时使用。
---

# Test-Driven Development

TDD 是 red → green 循环。本 skill 是让该循环产出值得保留的测试的参考：好测试是什么、测试放哪、反模式、循环规则。每节在每个周期都适用——在循环前和循环中查阅，非之后。

探索代码库时，读 `CONTEXT.md`（若存在）使测试名与 interface 词汇匹配项目领域语言，并尊重触及区域 ADR。

## 好测试是什么

测试通过公开 interface 验证行为，非实现细节。代码可完全变；测试不应变。好测试读像规格——「user can checkout with valid cart」准确告诉你有什么能力——因不关心内部结构而在重构中存活。

示例见 [tests.md](tests.md)，mock 指引见 [mocking.md](mocking.md)。

## Seam——测试放哪

**seam** 是你测试的公开边界：观察行为而不伸进内部的 interface。测试在 seam，从不测内部。

**仅在事先同意的 seam 测试。**写任何测试前，写下被测 seam 并与用户确认。未确认的 seam 不写测试。你不能测一切——事先同意 seam 是如何把测试 effort 落在关键路径和复杂逻辑而非每个 edge case。

问：「公开 interface 是什么？应测哪些 seam？」

interface 形状本身成问题时——module 多深、seam 在哪、interface 应暴露什么——用 `/codebase-design` skill 的词汇。它是 module、interface、depth、seam、adapter、leverage、locality 术语的共享来源，是查阅的参考，非要跑的会话。

## 反模式

- **实现耦合**——mock 内部 collaborator、测 private 方法，或通过 side channel 验证（查数据库而非 interface）。tell：重构但行为未变时测试破。
- **同义反复**——断言按代码方式重算期望值（`expect(add(a, b)).toBe(a + b)`、手工同方式 snapshot、常量 assert 等于自身），按构造通过、永与代码 disagree。期望值须来自独立真相——已知好 literal、算例、spec。
- **水平切片**——先写全部测试再全部实现。bulk 测试验证*想象*行为：测*形状*而非用户面向行为，对真实变更不敏感，在理解实现前 commit 测试结构。改 **vertical slices**——一测试 → 一实现 → 重复，每测试是响应上一周期所学的 **tracer bullet**。

## 循环规则

- **Red before green。**先写失败测试，再只写够通过的代码。不要预期未来测试或加 speculative 功能。
- **一次一片。**每周期一个 seam、一个测试、一个最小实现。
- **重构不是循环一部分。**属于评审阶段（见 `code-review` skill），非 red → green 实现周期。
