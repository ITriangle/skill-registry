# Operating Principles / 操作原则

This document expands on the core operating principles of the Domain Research skill. The agent should read this when performing domain research tasks.

## Principle 1: Do Not Start With the Final Answer

Avoid prompts like:

```text
帮我总结这个业务，并设计一个完整方案。
```

That usually produces generic output. Instead, first compile materials into a model:

```text
先不要生成最终方案。请基于这些材料，帮助一个不了解该领域的人建立第一版领域认知。
```

**Why:** Jumping to solutions skips the domain model. Without a model, the output is shallow and cannot be validated or reused.

## Principle 2: Separate Facts, Inferences, and Boundaries

Every research output should distinguish:

| Label | Meaning |
|-------|---------|
| **Facts** | Directly supported by the materials |
| **Rules** | Explicit methodology, policy, process, or technical constraints |
| **Calculations** | Derived values or transformations |
| **Inferences** | Reasoned conclusions from facts and rules |
| **Boundaries** | What cannot be concluded from current evidence |
| **Unknowns** | What must be confirmed with more source material or a human expert |

**Prompt pattern:**

```text
请明确区分：事实、规则、计算、推断、判断边界、待确认问题。
每条结论请标注 [事实]、[规则]、[推断] 或 [边界]。
```

## Principle 3: Compare Materials Instead of Summarizing One by One

If there are multiple reports, cases, examples, specs, or interviews, do not produce separate summaries. Ask for alignment:

```text
不要分别摘要这些材料。请对齐比较：哪些概念相同，哪些判断不同，哪些证据改变了结论，哪些模式可以迁移。
```

**Why:** Independent summaries hide contradictions and miss transferable patterns. Alignment surfaces what actually matters.

## Principle 4: Convert Understanding Into Work Assets

Domain research is incomplete until it creates downstream artifacts:

- Glossary and concept map
- Object model or process model
- Judgment chain or decision tree
- Risks, edge cases, and failure modes
- Expert question list
- Requirements and acceptance criteria
- Tests, Eval, Benchmark, or validation checklist
- Agent Skill, Runbook, or reusable template

## Prompt Patterns Library

### Compiling Methodology or Rules

```text
先不要生成最终方案，也不要写培训材料。

请读取 [methodology/rules/spec]，帮助一个不熟悉该领域的人建立第一版领域认知。

输出：
1. 这个方法论/规则试图解决的核心问题；
2. 涉及的关键业务对象或系统对象；
3. 必须观察的证据、字段、指标、事件或行为；
4. 每个指标/字段/规则背后的含义；
5. 可以形成的判断；
6. 证据不足时不能形成的判断；
7. 需要继续向专家或权威来源确认的问题。

请明确区分：事实、规则、计算、推断、判断边界。
```

### Aligning Cases Against Rules

```text
请读取 [case/report/example set] 和刚才编译的规则模型。

不要分别摘要这些材料。请对齐比较：
1. 每个案例中哪些内容对应规则模型中的判断维度；
2. 实际使用了哪些证据；
3. 哪些证据真正改变了判断；
4. 哪些内容只是背景描述，不应作为核心判断依据；
5. 哪些判断模式可以迁移到新任务；
6. 哪些结论只适用于原案例，不能迁移。

请输出"证据 → 指标/字段/事件 → 业务含义 → 判断 → 判断边界"的链路。
```

### Requesting Minimum Inputs

When no materials are provided:

```text
请至少提供：1 份规则/方法论/说明文档，1-3 个真实案例或样例，以及你最终想产出的工作产物。
```

### Generating Expert Questions

Do not ask broad questions like "请讲一下这个业务". Generate narrow questions:

```markdown
## Expert Calibration Questions

1. Is this object boundary correct: ...?
2. Which source is authoritative when ... conflicts with ...?
3. Are we allowed to conclude ... from ...?
4. What should the system do when evidence is missing?
5. Which failure would be unacceptable in production?
```

Questions should be few, specific, and tied to evidence.
