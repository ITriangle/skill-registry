---
name: setup-ts-deep-modules
description: 在 TypeScript 仓库中接入 dependency-cruiser，使每个包成为 deep module——实现隐藏在子文件夹中，只能通过入口文件访问。由用户调用。
disable-model-invocation: true
---

# Setup TS Deep Modules

让本仓库中每个包都成为 **deep module**：大量行为藏在小型接口之后。包的公开面是其**入口点**——包根目录的文件——子文件夹中的一切都被隐藏。本技能安装 [dependency-cruiser](https://github.com/sverweij/dependency-cruiser) 及使入口点成为唯一入口的规则，并证明规则会生效。

关于词汇（deep module、interface、seam、depth），运行 `/codebase-design` 技能——全程使用其语言。

## 本技能强制的形状

```
src/packages/
  <name>/
    index.ts        ← 入口点（公开）。从外部导入此文件。
    client.ts       ← 另一个入口点。包可以暴露多个。
    lib/            ← 实现：对外隐藏，内部可自由相互导入。
    tests/          ← 同位测试 + fixtures（子文件夹，因此私有）。
```

公开面是包的**根文件**——不是唯一的 `index.ts`。按惯例实现放在 `lib/`，测试放在 `tests/`，给每个包统一的两个文件夹形状。规则本身是通用的：*任何*子文件夹中的*任何*内容都是私有的，因此永远不必为新增文件夹扩展配置。

四条规则，均为 `error`：

1. **入口点边界**——包外代码（应用代码或其他包）只能导入该包的入口点（其根文件），绝不能导入子文件夹中的任何内容。
2. **包内自由**——包内文件可自由相互导入。
3. **测试通过入口点**——`<pkg>/tests/` 下的文件可导入任何包的入口点及自己的 `tests/` fixtures，但绝不能导入任何包子文件夹内部（包括自己的）。跨包集成测试可以；深层导入不行。
4. **无循环**——无依赖环。

**入口点，而非 barrel。**因为公开面是*每个*根文件，包可以暴露多个小入口点（`index.ts`、`client.ts`、`server.ts`），而不是把所有东西 funnel 进一个巨大的 `index.ts`。重新导出整棵子树的 barrel 文件不推荐——保持入口点小，把实现藏在子文件夹中。

分层（哪些包可以依赖哪些包）是*不同* concern，在配置中留为注释 stub，由本仓库自行填写。

## 步骤

### 1. 检测环境

- **包管理器**——`pnpm-lock.yaml` → pnpm，`yarn.lock` → yarn，`bun.lockb` → bun，否则 npm。以下所有命令都用它（`pnpm`/`yarn`/`npm run`/`bunx`）。
- **包根目录**——若存在 `src/` 则用 `src/packages`，否则 `packages`。若仓库已有明显不同惯例，与用户确认选择。
- **现有配置**——检查 `.dependency-cruiser.*` 文件。若已存在，**不要**覆盖：合并四条规则及选项，并告知用户你添加了什么。

**完成条件：**包管理器、包根目录、现有配置状态均已知。

### 2. 安装 dependency-cruiser

用检测到的包管理器将 `dependency-cruiser` 安装为 devDependency。

**完成条件：**`dependency-cruiser` 在 `devDependencies` 中。

### 3. 写入配置

将 [`dependency-cruiser.config.cjs`](./dependency-cruiser.config.cjs) 复制到仓库根目录为 `.dependency-cruiser.cjs`。将 `PACKAGES_ROOT` 设为步骤 1 检测到的根。规则基于路径深度且与扩展名无关，无需其他适配。

**完成条件：**`.dependency-cruiser.cjs` 存在且 `PACKAGES_ROOT` 正确，四条禁止规则齐全。

### 4. 接入检查

- 添加 `lint:boundaries` 脚本：`depcruise <packages-root>`（或 `depcruise src`）。
- 并入仓库的 umbrella 检查命令——已运行 typecheck 的那个（如 `check` / `ci` / `validate`）。**不要**动 `tsconfig` 或添加 path alias。
- 若无 umbrella 脚本，添加 `lint:boundaries` 并告知用户纳入 CI。

**完成条件：**`lint:boundaries` 存在，且与 typecheck 在同一命令中运行。

### 5. 脚手架示例包

创建已提交的 `<packages-root>/example/` 作为可复制模板：

- `index.ts`——入口点。导出一个委托给内部文件的函数（使包明显*深*，而非直通）。
- `lib/impl.ts`——**子文件夹**中的内部文件，由 `index.ts` 导入，外部不可达。
- `tests/example.test.ts`——**仅**导入 `../index`（入口点），并对公开函数断言。

告知用户这是可复制或删除的 starter 模板。

**完成条件：**示例包存在，通过根入口点暴露行为，并将 `impl` 藏在子文件夹中。

### 6. 证明规则会咬人

这是整个技能的完成标准——违规时不失败的配置毫无价值。

1. 运行 `lint:boundaries`。在干净示例上必须**通过**。
2. 临时在 `tests/example.test.ts` 添加深层导入（如 `import { thing } from "../lib/impl"`）。再次运行 `lint:boundaries`——必须**失败**并报告 `tests-through-entrypoints`。
3. 撤销深层导入。再运行一次——必须**通过**。

**完成条件：**你已观察到通过、深层导入失败、再通过后。若步骤 2 未失败，规则未正确接入——修复后再结束。

### 7. 记录约定

在包文件夹中写 `README.md`（`<packages-root>/README.md`）——与其管辖的包并列——涵盖：`src/packages/<name>/` 布局（根入口点、`lib/` 实现、`tests/` 测试）、「仅通过包的入口点（根文件）导入」，以及如何运行 `lint:boundaries`。**明确 discouraging barrel 文件**——暴露多个小入口点，而非通过一个 index 重新导出整棵子树。保持为可复制片段加四条规则各一段。

然后从仓库的 agent 说明文件添加**上下文指针**——优先 `CLAUDE.md`，否则 `AGENTS.md`（两者都不存在则创建 `AGENTS.md`）。一行即可，例如 `Packages are deep modules — see [src/packages/README.md](./src/packages/README.md) before adding or importing one.` 这使 agent 能发现边界规则，而不是踩上去。

**完成条件：**`<packages-root>/README.md` 存在且 discouraging barrels，且仓库 `CLAUDE.md`/`AGENTS.md` 链接到它。

## 备注

- 配置中的 `$1` 反向引用（dependency-cruiser 的组匹配）让包能访问自己的内部，而外部不能——不要把它们展平成按包分开的规则。
- 公开 vs 私有由**深度**决定：包的根文件是入口点；子文件夹中的一切是私有的。惯例子文件夹是 `lib/`（实现）和 `tests/`，但规则不硬编码它们——任何子文件夹都是私有的，新文件夹无需改配置。添加入口点只是添加根文件——无需 barrel。
- 包是**扁平**的：根下仅一层直接子目录。包内部可嵌套任意深；包内不能再包含另一个包。
- 使用 `.cjs`（非 `.js`），使配置的 `module.exports` 在 `"type": "module"` 仓库中也能工作。
