# 领域文档

工程技能在探索代码库时，应按以下规则使用当前仓库的领域文档。

## 探索前先读取

- 根目录的 **`CONTEXT.md`**；或者
- 如果根目录存在 **`CONTEXT-MAP.md`**，它会指向每个上下文的 `CONTEXT.md`。读取与当前主题相关的每一份。
- **`docs/adr/`**——读取涉及即将处理区域的 ADR。在多上下文仓库中，还要检查 `src/<context>/docs/adr/` 中限定上下文范围的决策。

如果其中任何文件不存在，**静默继续**。不要把缺失列为问题，也不要预先建议创建。`/domain-modeling` 技能（可通过 `/grill-with-docs` 和 `/improve-codebase-architecture` 到达）会在术语或决策真正得到确认时按需创建它们。

## 文件结构

单上下文仓库（多数仓库）：

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

多上下文仓库（根目录存在 `CONTEXT-MAP.md`）：

```
/
├── CONTEXT-MAP.md
├── docs/adr/                          ← 系统级决策
└── src/
    ├── ordering/
    │   ├── CONTEXT.md
    │   └── docs/adr/                  ← 上下文特有决策
    └── billing/
        ├── CONTEXT.md
        └── docs/adr/
```

## 使用词汇表中的术语

当输出中出现领域概念（例如 issue 标题、重构建议、假设或测试名称）时，使用 `CONTEXT.md` 中定义的术语。不要改用词汇表明确要求避免的同义词。

如果需要的概念尚未出现在词汇表中，这本身就是一个信号：要么你正在创造项目并未使用的语言（应重新考虑），要么确实存在空缺（记录下来交给 `/domain-modeling`）。

## 标明 ADR 冲突

如果输出与现有 ADR 冲突，应明确指出，而不是静默覆盖：

> _与 ADR-0007（事件溯源订单）冲突——但值得重新讨论，因为……_
