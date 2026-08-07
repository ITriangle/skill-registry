# Skill 机制

[`writing-for-agents`](SKILL.md) 的 skill 特有分支：当文档是 skill 时什么会变化——frontmatter、调用选择、router skill。关于如何写它的其余一切，在 `SKILL.md` 的通用参考中。

## 调用

两种选择，交易两种负载：

- **模型调用** skill 保留 `description`，agent 可自主触发——其他 skill 也可触及它。你仍可输入名称：模型调用始终*包含*用户触及；description 只增加 agent 发现，从不移除人类。description 是 skill 的顶层上下文指针，被迫始终加载——用永久上下文负载换取可发现性。内容全是参考的模型调用 skill 也是共享参考的一处归宿：另一 skill 可调用它，多个 skill 需要的参考集中在一处。机制：省略 `disable-model-invocation`，写面向模型的 description 携带触发分支（`SKILL.md` 中的指针写作规则完全适用）。
- **用户调用** skill 把 description 从 agent 触及范围剥离：只有人类输入名称可调用，其他 skill 不能。零上下文负载，但花费认知负载——你是必须记住它存在的索引。机制：设置 `disable-model-invocation: true`；`description` 变为面向人类——一行摘要，触发列表被剥离。

仅当 agent 必须自主触及 skill，或另一 skill 必须触及时，才选模型调用。若只手工触发，做成用户调用，不付上下文负载。

两个用户调用 skill 都需要的共享参考，不能放在任一之中——无 description 时，彼此无法触发。推到 skill 系统外的普通文件：任何 skill 可指向的外部参考。

## 按调用拆分

拆分的调用切割（序列切割在 `SKILL.md`）：当你有应独立触发的 distinct leading word——prompt 中实际使用的触发词——或另一 skill 必须触及时，拆出模型调用 skill。你为新的始终加载 description 付上下文负载，因此独立触及必须值得。

## Router skill

当用户调用 skill 多到记不住，堆积的认知负载由 **router skill** 治愈：一个用户调用 skill 命名其他 skill 及何时取用，人类只需记住一个 skill 而非许多。它只能 hint，不能触发它们：用户调用 skill 无 description，除人类外无人能触及它们。
