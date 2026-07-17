---
name: domain-modeling
description: 构建并打磨项目的领域模型——术语表、通用语言和 ADR。用于修改模型，而不是仅仅读取 CONTEXT.md。
---

# 领域建模

主动打磨领域模型：质疑术语、用场景进行压力测试，并在决策逐渐明确时将其记录下来。读取 `CONTEXT.md` 以了解词汇只是一个随手动作；此技能用于**改变**模型。

## 文件存放位置

单上下文：`CONTEXT.md` + `docs/adr/`。多上下文：`CONTEXT-MAP.md` 指向各区域的 `CONTEXT.md` 和 ADR。有内容可写时再按需创建文件。格式参见：[CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md)、[ADR-FORMAT.md](./ADR-FORMAT.md)。

## 会话期间

- **质疑术语表**——指出与 `CONTEXT.md` 冲突的术语。
- **打磨模糊语言**——提出精确的规范术语。
- **用场景进行压力测试**——用迫使边界决策的边缘情况检验模型。
- **与代码交叉核对**——揭示既定规则与实际实现之间的矛盾。
- **与代码图谱交叉核对**——如果存在 `graphify-out/graph.json`，告诉用户“用代码图谱验证模块边界假设”，然后查询模块边界和依赖密度，以验证概念边界假设。使用 `/code-graph query modules` 获取概览，并使用 `/code-graph query deps <module>` 验证拟议的领域边界是否与实际代码边界一致。
- **就地更新 CONTEXT.md**——一次处理一个术语；只写术语表，不写实现细节。

## ADR——仅当以下三项全部成立时才提出

1. 难以逆转
2. 缺少上下文时会令人意外
3. 是在真实权衡多个方案后作出的结果

否则跳过 ADR。
