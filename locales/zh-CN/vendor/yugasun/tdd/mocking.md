# 何时使用 Mock

只在**系统边界**使用 mock：

- 外部 API（支付、邮件等）
- 数据库（有时需要——优先使用测试数据库）
- 时间/随机性
- 文件系统（有时需要）

不要 mock：

- 自己的类/模块
- 内部协作者
- 任何你能控制的部分

## 为可 Mock 性而设计

在系统边界设计易于 mock 的接口：

**1. 使用依赖注入**

从外部传入依赖，不要在内部创建：

```typescript
// 易于 mock
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// 难以 mock
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

**2. 优先使用 SDK 风格接口，而不是通用 fetcher**

为每项外部操作创建专用函数，不要使用一个带条件逻辑的通用函数：

```typescript
// 好：每个函数均可独立 mock
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};

// 差：mock 内部需要条件逻辑
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

SDK 方式意味着：

- 每个 mock 只返回一种明确的数据结构
- 测试设置中没有条件逻辑
- 更容易看出测试调用了哪些端点
- 每个端点都有类型安全
