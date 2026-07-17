---
name: scaffold-exercises
description: 创建包含章节、习题、答案和讲解，并能通过 lint 的习题目录结构。当用户希望搭建习题、创建习题存根或设置新的课程章节时使用。
---

# 搭建习题

创建能通过 `pnpm ai-hero-cli internal lint` 的习题目录结构，然后用 `git commit` 提交。

## 目录命名

- **章节**：`exercises/` 内的 `XX-section-name/`（例如 `01-retrieval-skill-building`）
- **习题**：章节内的 `XX.YY-exercise-name/`（例如 `01.03-retrieval-with-bm25`）
- 章节编号 = `XX`，习题编号 = `XX.YY`
- 名称使用短横线格式（小写字母、连字符）

## 习题变体

每道习题至少需要以下一个子文件夹：

- `problem/`——带 TODO 的学员工作区
- `solution/`——参考实现
- `explainer/`——概念材料，不含 TODO

创建存根时，除非计划另有规定，否则默认使用 `explainer/`。

## 必需文件

每个子文件夹（`problem/`、`solution/`、`explainer/`）都需要一个满足以下条件的 `readme.md`：

- **非空**（必须有真实内容，即使只有一行标题也可以）
- 没有失效链接

创建存根时，生成包含标题和描述的最小 readme：

```md
# 习题标题

在此填写描述
```

如果子文件夹包含代码，还需要一个 `main.ts`（超过 1 行）。但对于存根，仅有 readme 的习题即可。

## 工作流

1. **解析计划**——提取章节名称、习题名称和变体类型
2. **创建目录**——对每个路径执行 `mkdir -p`
3. **创建 readme 存根**——在每个变体文件夹中创建一个带标题的 `readme.md`
4. **运行 lint**——执行 `pnpm ai-hero-cli internal lint` 验证
5. **修复所有错误**——迭代直到 lint 通过

## Lint 规则摘要

lint 工具（`pnpm ai-hero-cli internal lint`）检查：

- 每道习题都有子文件夹（`problem/`、`solution/`、`explainer/`）
- `problem/`、`explainer/` 或 `explainer.1/` 至少存在一个
- 主子文件夹中存在非空的 `readme.md`
- 没有 `.gitkeep` 文件
- 没有 `speaker-notes.md` 文件
- readme 中没有失效链接
- readme 中没有 `pnpm run exercise` 命令
- 除非子文件夹只有 readme，否则每个子文件夹都必须有 `main.ts`

## 移动/重命名习题

重新编号或移动习题时：

1. 使用 `git mv`（而不是 `mv`）重命名目录——保留 Git 历史
2. 更新数字前缀以维持顺序
3. 移动后重新运行 lint

示例：

```bash
git mv exercises/01-retrieval/01.03-embeddings exercises/01-retrieval/01.04-embeddings
```

## 示例：根据计划创建存根

假设计划如下：

```
第 05 章：记忆技能构建
- 05.01 记忆简介
- 05.02 短期记忆（explainer + problem + solution）
- 05.03 长期记忆
```

创建：

```bash
mkdir -p exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer
mkdir -p exercises/05-memory-skill-building/05.02-short-term-memory/{explainer,problem,solution}
mkdir -p exercises/05-memory-skill-building/05.03-long-term-memory/explainer
```

然后创建 readme 存根：

```
exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer/readme.md -> "# 记忆简介"
exercises/05-memory-skill-building/05.02-short-term-memory/explainer/readme.md -> "# 短期记忆"
exercises/05-memory-skill-building/05.02-short-term-memory/problem/readme.md -> "# 短期记忆"
exercises/05-memory-skill-building/05.02-short-term-memory/solution/readme.md -> "# 短期记忆"
exercises/05-memory-skill-building/05.03-long-term-memory/explainer/readme.md -> "# 长期记忆"
```
