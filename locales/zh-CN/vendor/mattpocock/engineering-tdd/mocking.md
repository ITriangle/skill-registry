# 何时使用 Mock

只在**系统边界**使用 mock：

- 外部 API（支付、邮件等）
- 数据库（有时使用——优先使用测试数据库）
- 时间/随机性
- 文件系统（有时使用）

不要 mock：

- 你自己的 class/module
- 内部协作者
- 任何你能控制的东西

## 为可 Mock 性而设计

在系统边界，设计容易 mock 的接口：

**1. 使用依赖注入**

从外部传入依赖，而不是在内部创建：

```typescript
// 容易 mock
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

为每个外部操作创建专用函数，而不是使用一个包含条件逻辑的通用函数：

```typescript
// 好：每个函数都可独立 mock
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};

// 差：mock 本身需要包含条件逻辑
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

SDK 方式意味着：
- 每个 mock 返回一种特定形态
- 测试设置中没有条件逻辑
- 更容易看出测试覆盖了哪些 endpoint
- 每个 endpoint 都有类型安全
