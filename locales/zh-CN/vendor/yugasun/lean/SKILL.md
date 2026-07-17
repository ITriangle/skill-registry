---
name: lean
description: >
  最小方案纪律：YAGNI 阶梯、标准库与原生能力优先、最短可用 diff。编写交付代码时使用；
  用户提到 lean、lean mode、yagni、ponytail、lazy mode，或抱怨过度工程时也使用。
license: MIT
---

# Lean

改编自 ponytail 纪律。Lazy 意味着高效，而不是粗心。在 aiops bundle 的**交付**阶段启用；在 grill/对齐阶段**关闭**。

## 阶梯

遇到第一个足以支撑需求的层级就停止：

1. 这真的需要存在吗？（YAGNI）
2. 标准库能做吗？
3. 平台原生功能能做吗？
4. 已安装的依赖能做吗？
5. 一行能完成吗？
6. 编写能工作的最少代码

## 规则

- 不添加未要求的抽象、样板代码或为“以后”准备的臆测代码
- 删除优先于新增；采用最短的可用 diff
- 标记有意采用的捷径：`// lean: <ceiling and upgrade path>`

## 输出

先给代码，之后最多三行：省略了什么、何时应补上。

## 绝不能削减

信任边界验证、数据丢失防护、安全性、无障碍，以及明确要求的行为。

## 强度

`/lean lite|full|ultra`——默认 **full**。关闭：“stop lean”/“normal mode”。
