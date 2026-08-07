---
name: prototype
description: 构建一次性原型回答设计问题。当用户想 sanity-check 状态模型或逻辑是否 feel right，或探索 UI 应什么样时使用。
---

# Prototype

原型是**回答一个问题的一次性代码**。问题决定形状。

## 选分支

识别正在回答的问题——来自用户 prompt、周围代码，或用户在时询问：

- **「这逻辑 / 状态模型 feel right 吗？」** → [LOGIC.md](LOGIC.md)。构建单个可分享 HTML 文件——自由玩按钮 + 分 tab 引导 walkthrough——把状态机推过纸上难推理的 case，非开发者可驱动。
- **「这应该长什么样？」** → [UI.md](UI.md)。在单一路由上生成几种 radically different UI 变体，通过 URL search param 和底部浮动 bar 切换。

两分支产出很不同的 artifact——搞错浪费整个原型。问题真模糊且用户 unreachable 时，默认选与周围代码更匹配的分支（backend module → logic；page 或 component → UI），并在原型顶部陈述假设。

## 两分支共同规则

1. **从第一天 throwaway，且清楚标记。**把原型代码放在将实际使用处附近（module 或 page 旁）使上下文 obvious——但命名使 casual reader 看出是原型非生产。throwaway UI route 遵守项目已有 routing 惯例；不要发明新顶层结构。
2. ** trivial 运行。**UI 原型从项目 task runner 一条命令启动——`pnpm <name>`、`python <path>`、`bun <path>` 等。logic demo 是用户双击的单个 HTML。启动无需思考。
3. **默认无持久化。**状态在内存。持久化是原型在*检查*的东西，不应依赖。若问题明确涉及数据库，打 scratch DB 或本地文件，名带清楚「PROTOTYPE — wipe me」。
4. **跳过 polish。**无测试、无超出使原型*runnable* 的错误处理、无抽象。目的是快速学东西。
5. **Surface 状态。**每次动作后（logic）或每次变体切换（UI），打印或渲染完整相关状态，使用户看到变了什么。
6. **完成时 capture。**把 validated 决定 fold 进真实代码，然后把原型本身 capture 为 **primary source**：commit 到 throwaway branch、main 外，在实现 issue 上留指向该 branch 的 context pointer。也 capture 答案——verdict 及 settled 的问题——在 issue 或 commit。main branch 只留 validated 决定。
