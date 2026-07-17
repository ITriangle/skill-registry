# 领域文档

工程技能探索代码库时，应如何使用本仓库的领域文档。

## 探索前先阅读

- 仓库根目录的 **`CONTEXT.md`**；或者
- 如果仓库根目录存在 **`CONTEXT-MAP.md`**，它会指向每个上下文各自的 `CONTEXT.md`。读取与当前主题有关的每一份。
- **`docs/adr/`**——读取涉及即将处理区域的 ADR。在多上下文仓库中，还要检查 `src/<context>/docs/adr/` 中限定于该上下文的决策。

如果这些文件不存在，**静默继续**。不要指出缺失，也不要预先建议创建。`/domain-modeling`（通过 `/grill-with-docs` 或 `/aiops` 的架构健康检查）会在术语或决策明确后按需创建它们。

## 文件结构

单上下文仓库（大多数仓库）：

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
    │   └── docs/adr/                  ← 特定上下文的决策
    └── billing/
        ├── CONTEXT.md
        └── docs/adr/
```

## 使用词汇表中的词

输出中为领域概念命名时（issue 标题、重构建议、假设、测试名称），使用 `CONTEXT.md` 定义的术语。不要漂移到词汇表明确要求避免的同义词。

如果词汇表中还没有所需概念，这就是一个信号——要么你正在发明项目不用的语言（重新考虑），要么确有空缺（记下来交给 `/domain-modeling`）。

## 标记 ADR 冲突

如果输出与现有 ADR 冲突，明确展示冲突，不要静默覆盖：

> *与 ADR-0007（事件溯源订单）冲突——但值得重新讨论，因为……*
