---
name: gitops
description: >
  Git 操作封装：同步、暂存、提交、推送。生成引用 .scratch 产物的 Conventional Commits
  消息。用于用户提到 gitops、commit、push、同步代码，或需要版本控制操作时。
---

# Gitops

用于 aiops 交付链的 Git 版本控制操作。

## 操作

### sync

从远程拉取最新内容。默认策略：rebase。

```
git pull --rebase
```

如果发生合并冲突：报告给用户，不要自动解决。

### status

显示当前工作树状态。

```
git status
git diff --stat
```

### stage

暂存待提交文件。支持选择性暂存。

```
git add <files>
```

### commit

使用 Conventional Commits 消息创建提交。

**格式：**
```
<type>(<scope>): <subject>

<body>

Refs: .scratch/<feature-slug>/
```

**类型：** feat | fix | refactor | test | docs | chore

**消息生成：**
- 读取 `.scratch/<feature>/NOTES.md` 获取设计上下文
- 读取 `.scratch/<feature>/REVIEW.md` 确认评审通过
- Scope = feature-slug 或模块名
- Subject = 祈使语气、小写、不加句号
- Body = 引用上游产物，确保可追溯性

**提交前检查：**
- 所有阻塞性的 REVIEW.md 发现都已解决
- 提交中没有未跟踪的 .scratch 文件（需要时将其加入 .gitignore）

### push

推送到远程。需要用户确认。

```
git push origin <branch>
```

### branch

分支管理：创建、切换、列出。

```
git checkout -b <branch>   # 创建并切换
git checkout <branch>      # 切换
git branch                 # 列出
```

## 流程

1. `sync`——拉取最新内容
2. `status`——检查更改
3. `stage`——选择文件
4. `commit`——使用生成的消息提交
5. `push`——用户确认后推送

## 约束

- 绝不修改代码文件
- 绝不自动解决合并冲突
- 推送前始终向用户确认
- 有 .scratch 产物时，提交消息必须引用这些产物
- 如果存在 `.scratch/<feature>/REVIEW.md` 且 verdict 为 REQUEST_CHANGES，则阻止提交并报告
