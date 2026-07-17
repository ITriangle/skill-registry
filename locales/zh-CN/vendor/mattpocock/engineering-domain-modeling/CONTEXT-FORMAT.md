# CONTEXT.md 格式

## 结构

```md
# {上下文名称}

{用一两句话说明该上下文是什么，以及为什么存在。}

## 语言

**Order**：
{用一两句话描述该术语}
_避免使用_：Purchase、transaction

**Invoice**：
交付后发送给客户的付款请求。
_避免使用_：Bill、payment request

**Customer**：
下订单的个人或组织。
_避免使用_：Client、buyer、account
```

## 规则

- **明确表态。**同一概念有多个词可用时，选出最合适的一个，把其他词列在 `_避免使用_` 下。
- **定义务求精炼。**最多一两句话。定义它“是什么”，而不是“做什么”。
- **只包含本项目上下文特有的术语。**通用编程概念（超时、错误类型、工具模式）不属于这里，即使项目广泛使用它们。添加术语前先问：这是当前上下文独有的概念，还是通用编程概念？只有前者属于这里。
- 自然形成术语簇时，**用子标题分组**。如果所有术语都属于同一个紧密相关的领域，使用扁平列表即可。

## 单上下文与多上下文仓库

**单上下文（大多数仓库）：**仓库根目录只有一份 `CONTEXT.md`。

**多上下文：**仓库根目录的 `CONTEXT-MAP.md` 列出各上下文、所在位置及其相互关系：

```md
# 上下文映射

## 上下文

- [Ordering](./src/ordering/CONTEXT.md) — 接收并跟踪客户订单
- [Billing](./src/billing/CONTEXT.md) — 生成发票并处理付款
- [Fulfillment](./src/fulfillment/CONTEXT.md) — 管理仓库拣货和发货

## 关系

- **Ordering → Fulfillment**：Ordering 发出 `OrderPlaced` 事件；Fulfillment 消费事件并开始拣货
- **Fulfillment → Billing**：Fulfillment 发出 `ShipmentDispatched` 事件；Billing 消费事件并生成发票
- **Ordering ↔ Billing**：共享 `CustomerId` 和 `Money` 类型
```

技能会推断应采用哪种结构：

- 如果存在 `CONTEXT-MAP.md`，读取它来查找上下文
- 如果只有根目录 `CONTEXT.md`，则为单上下文
- 如果两者都不存在，在第一个术语确定时按需创建根目录 `CONTEXT.md`

存在多个上下文时，推断当前主题属于哪一个。不明确就询问。
