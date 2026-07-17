---
name: migrate-to-shoehorn
description: 将测试文件从 `as` 类型断言迁移到 @total-typescript/shoehorn。当用户提到 shoehorn、希望替换测试中的 `as`，或需要不完整测试数据时使用。
---

# 迁移到 Shoehorn

## 为什么使用 shoehorn？

`shoehorn` 让你能在测试中传入不完整数据，同时让 TypeScript 保持满意。它用类型安全的替代方案取代 `as` 断言。

**只用于测试代码。**绝不要在生产代码中使用 shoehorn。

测试中使用 `as` 的问题：

- 我们一贯不鼓励使用它
- 必须手动指定目标类型
- 故意传入错误数据时需要双重断言（`as unknown as Type`）

## 安装

```bash
npm i @total-typescript/shoehorn
```

## 迁移模式

### 只需少量属性的大对象

迁移前：

```ts
type Request = {
  body: { id: string };
  headers: Record<string, string>;
  cookies: Record<string, string>;
  // ……还有 20 个属性
};

it("gets user by id", () => {
  // 只关心 body.id，却必须伪造整个 Request
  getUser({
    body: { id: "123" },
    headers: {},
    cookies: {},
    // ……伪造全部 20 个属性
  });
});
```

迁移后：

```ts
import { fromPartial } from "@total-typescript/shoehorn";

it("gets user by id", () => {
  getUser(
    fromPartial({
      body: { id: "123" },
    }),
  );
});
```

### `as Type` → `fromPartial()`

迁移前：

```ts
getUser({ body: { id: "123" } } as Request);
```

迁移后：

```ts
import { fromPartial } from "@total-typescript/shoehorn";

getUser(fromPartial({ body: { id: "123" } }));
```

### `as unknown as Type` → `fromAny()`

迁移前：

```ts
getUser({ body: { id: 123 } } as unknown as Request); // 故意使用错误类型
```

迁移后：

```ts
import { fromAny } from "@total-typescript/shoehorn";

getUser(fromAny({ body: { id: 123 } }));
```

## 各函数的使用时机

| 函数            | 用例                                       |
| --------------- | ------------------------------------------ |
| `fromPartial()` | 传入仍能通过类型检查的不完整数据           |
| `fromAny()`     | 传入故意错误的数据（仍保留自动补全）       |
| `fromExact()`   | 强制要求完整对象（之后可换成 fromPartial） |

## 工作流

1. **收集需求**——询问用户：
   - 哪些测试文件中的 `as` 断言造成了问题？
   - 是否在处理只需少量属性的大对象？
   - 是否需要为错误测试传入故意错误的数据？

2. **安装和迁移**：
   - [ ] 安装：`npm i @total-typescript/shoehorn`
   - [ ] 查找包含 `as` 断言的测试文件：`grep -r " as [A-Z]" --include="*.test.ts" --include="*.spec.ts"`
   - [ ] 将 `as Type` 替换为 `fromPartial()`
   - [ ] 将 `as unknown as Type` 替换为 `fromAny()`
   - [ ] 添加从 `@total-typescript/shoehorn` 导入的语句
   - [ ] 运行类型检查进行验证
