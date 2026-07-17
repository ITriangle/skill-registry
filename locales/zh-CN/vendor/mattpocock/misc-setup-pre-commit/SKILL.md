---
name: setup-pre-commit
description: 在当前仓库中设置 Husky pre-commit hook，包含 lint-staged（Prettier）、类型检查和测试。当用户希望添加 pre-commit hook、设置 Husky、配置 lint-staged，或在提交时执行格式化/类型检查/测试时使用。
---

# 设置 Pre-Commit Hook

## 本技能会设置什么

- **Husky** pre-commit hook
- **lint-staged**，对所有已暂存文件运行 Prettier
- **Prettier** 配置（如果缺失）
- pre-commit hook 中的 **typecheck** 和 **test** 脚本

## 步骤

### 1. 检测包管理器

检查 `package-lock.json`（npm）、`pnpm-lock.yaml`（pnpm）、`yarn.lock`（yarn）、`bun.lockb`（bun）。使用存在的包管理器；不明确时默认 npm。

### 2. 安装依赖

安装为 devDependencies：

```
husky lint-staged prettier
```

### 3. 初始化 Husky

```bash
npx husky init
```

这会创建 `.husky/` 目录，并向 package.json 添加 `prepare: "husky"`。

### 4. 创建 `.husky/pre-commit`

写入以下内容（Husky v9+ 无需 shebang）：

```
npx lint-staged
npm run typecheck
npm run test
```

**按需调整**：将 `npm` 替换为检测到的包管理器。如果仓库的 package.json 中没有 `typecheck` 或 `test` 脚本，则省略对应行并告知用户。

### 5. 创建 `.lintstagedrc`

```json
{
  "*": "prettier --ignore-unknown --write"
}
```

### 6. 创建 `.prettierrc`（如果缺失）

仅当不存在 Prettier 配置时创建。使用以下默认值：

```json
{
  "useTabs": false,
  "tabWidth": 2,
  "printWidth": 80,
  "singleQuote": false,
  "trailingComma": "es5",
  "semi": true,
  "arrowParens": "always"
}
```

### 7. 验证

- [ ] `.husky/pre-commit` 存在且可执行
- [ ] `.lintstagedrc` 存在
- [ ] package.json 中的 `prepare` 脚本为 `"husky"`
- [ ] Prettier 配置存在
- [ ] 运行 `npx lint-staged` 验证其有效

### 8. 提交

暂存所有变更/新文件，并使用以下消息提交：`Add pre-commit hooks (husky + lint-staged + prettier)`

这会触发新的 pre-commit hook——是验证一切正常的良好冒烟测试。

## 说明

- Husky v9+ 的 hook 文件不需要 shebang
- `prettier --ignore-unknown` 会跳过 Prettier 无法解析的文件（图片等）
- pre-commit 先运行 lint-staged（速度快，只处理已暂存文件），再运行完整类型检查和测试
