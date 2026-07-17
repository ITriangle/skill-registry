# 设计词汇

供 `/architect-design`、`/improve-codebase-architecture` 和 design-mode `/review` 共享的术语。必须准确使用——不要替换成“component”“service”“API”或“boundary”。

## 术语表

**Module**——任何具有 interface 和 implementation 的事物（function、class、package 或贯穿多层的 slice）。

**Interface**——调用方必须知道的一切：type signature、invariant、顺序约束、错误模式、必需配置、性能特征。

**Implementation**——module 内部的内容。不同于 **Adapter**（它是在 seam 处扮演的角色，而非实体本身）。

**Depth**——调用方每学习一单位 interface 所能使用的行为量。**Deep** = 小 interface + 丰富 implementation。**Shallow** = interface ≈ implementation（应避免）。

**Seam**——module 的 interface 所在之处；无需在该处编辑即可改变行为的位置。

**Adapter**——在 seam 处满足 interface 的具体事物。

**Leverage**——每学习一单位 interface 获得的能力。一个 implementation 在 N 个调用点和 M 个测试中产生回报。

**Locality**——变更、bug、知识和验证集中在一个地方。修复一次，处处修复。

## 原则

- **Depth 是 interface 的属性**，不是 implementation 的属性。内部 seam 可以私有存在；它们不属于外部 interface。
- **删除测试。** 删除 module。复杂度消失 → pass-through。复杂度在 N 个调用方重新出现 → 该 module 发挥了价值。
- **Interface 就是测试表面。** 调用方和测试穿过同一个 seam。
- **一个 adapter = 假设性 seam；两个 adapter = 真实 seam。** 除非某些内容确实会在 seam 两侧变化，否则不要引入 seam。

## 为可测试性而设计

1. **接收依赖，不要创建依赖**——注入 gateway，不要在内部 `new StripeGateway()`。
2. **返回结果，不要制造副作用**——优先使用 `calculateDiscount(cart): Discount`，而不是修改 `cart.total`。
3. **小表面积**——method 和 param 越少，测试越简单。
