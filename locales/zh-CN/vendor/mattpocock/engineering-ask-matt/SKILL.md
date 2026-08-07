---
name: ask-matt
description: 询问哪种技能或流程适合当前情形。它是此仓库技能的路由器。
disable-model-invocation: true
---

# Ask Matt

你不可能记住每个技能，所以直接问。

**流程（flow）**是穿过多个技能的一条路径。大多数路径沿一条**主流程**前进，另有两条**入口匝道**汇入。其他技能要么独立运行，要么是在底层工作的词汇层。

## 主流程：从想法到交付

大多数工作都会经过这条路线：你有一个想法，并希望把它构建出来。

1. **`/grill-with-docs`**——通过采访打磨想法。**在 working directory 中工作时**从这里开始：它有状态，会把学到的内容保存在 `CONTEXT.md` 和 ADR 中。（没有 working directory？用 `/grill-me`——见独立技能。两者都运行相同的 `/grilling` 原语；`grill-with-docs` 会留下书面轨迹，有 repo 可留时它是更好的选择。）
2. **分支——所有问题都能在对话中解决吗？**若某问题需要可运行答案（状态、业务逻辑、必须亲眼看到的 UI），就绕道原型，往返两个方向都用 **`/handoff`** 衔接（原型在独立目录，正是 `/handoff` 的用途——见 Phase boundaries）：
   - **`/handoff`** 导出，然后针对该文件打开新会话，
   - **`/prototype`** 用一次性代码回答问题，
   - **`/handoff`** 带回所学，并在原始想法线程中引用。
3. **分支——这是多会话构建吗？**
   - **是** → **`/to-spec`**（把线程转成 spec），再 **`/to-tickets`** 拆成 tracer-bullet ticket，每个声明自己的**阻塞边**。本地跟踪器上是 `.scratch/<feature>/issues/` 下每个 ticket 一个文件，手工按 blocker 优先处理；真实跟踪器上边成为原生阻塞链接，blocker 完成的 ticket 可被领取——对每个 ticket 启动 **`/implement`**，**每个之间 `/clear` 上下文**。每个 ticket 自包含，最后一个的上下文可丢弃。
   - **否** → 就在这里、同一上下文窗口中 **`/implement`**。

   无论哪种，**`/implement`** 构建每个 issue 时内部驱动 **`/tdd`**——每次一个 red-green 切片——然后在提交前运行 **`/code-review`**，对 diff 做 Standards + Spec 两轴评审。只想测试优先构建具体行为、不需要完整 spec 时单独用 **`/tdd`**；想相对固定基准评审分支或 PR 时单独用 **`/code-review`**。

### 上下文卫生

让步骤 1–3 处于**一个不中断的上下文窗口**——`/to-tickets` 前不要 compact 或 clear——使 grilling、spec 和 ticket 建立在同一套思考上。之后每次 `/implement` 从新鲜上下文开始，依据 ticket 工作。

限制是 **[smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone)**：模型仍 sharp 推理的窗口（前沿模型约 150k token）。若在 `/to-tickets` 前会话逼近它，不要在 degraded 状态下硬推——在最近 phase boundary **`/compact`** 并继续（见 Phase boundaries）。

## 入口匝道

产生工作然后汇入主流程的起始情形。

- **Bug 和请求堆积** → **`/triage`**。把 issue 移过 triage 角色，产出 agent-ready issue，供后续 **`/implement`** 领取。

  triage 仅针对**你没创建的** issue——bug 报告、incoming 功能请求、任何 raw 到达的内容。`/to-tickets` 产出的 ticket 已是 agent-ready，**不要 triage 它们**。

- **有东西坏了** → **`/diagnosing-bugs`**。针对难的：一眼看不出的 bug、间歇 flake、两个已知好状态之间 creep 进来的回归。它拒绝在拥有 **tight feedback loop**——一条已在*此* bug 上变红的命令——之前 theorise，然后用回归测试修复。事后分析在真正发现是缺少好 seam 锁 bug 时，hand off 到 **`/improve-codebase-architecture`**。

- **巨大、迷雾重重的努力——绿地项目或巨大功能构建，一次会话放不下** → **`/wayfinder`**，此处认知要求最高的流程。从此处到目的地的路尚不可见时，它在 issue tracker 上绘制**决策 ticket** 的**共享地图**，逐个解决——产出**决定，而非交付物**——直到迷雾退散、路清晰。`**/grill-with-docs`** 打磨一次会话能 hold 的想法；wayfinder 给 hold 不住的想法——更慢更密，只留给恰好那种情形，从不是 well-scoped feature。

  地图清晰后，**它 hand off，不构建**：在主流程 **`/to-spec`** 汇入，把地图链接的决定 collapse 成可构建计划，然后照常 `/to-tickets` 和 `/implement`。把地图直接 loop 进 `/implement` 跳过 collapse、扔掉链接细节——仅当努力确实很小时才直接去 `/implement`。

## 代码库健康

非功能工作——维护。

- **`/improve-codebase-architecture`**——有空就跑，保持代码库适合 agent 操作。它 surface **deepening opportunities**；选一个会*生成想法*，可在主流程 `/grill-with-docs` 继续。它是找候选的 survey；**`/codebase-design`**（下）是设计所选候选的工作台。

## 底层词汇

两个模型调用参考，在其他 skill *之下*运行——各自是其词汇的单一真相来源。当**词**（而非流程）是问题时直接取用；或让上面 skill 拉入。

- **`/domain-modeling`**——打磨项目*领域*语言：挑战模糊术语、解决 overloaded 词（「account」干三件事）、把难逆转决定记为 ADR。它是 `/grill-with-docs` 驱动以保持 `CONTEXT.md` 干净 glossary 的 active discipline。
- **`/codebase-design`**——deep-module 词汇（module、interface、depth、seam、adapter、leverage、locality），用于设计 module 的*形状*：大量行为藏在 clean seam 上的小接口之后。`/tdd` 和 `/improve-codebase-architecture` 都讲它。

## Phase boundaries

**phase** 是会话内的一块工作——grilling、实现、QA。两个 phase 之间的**边界**你有五个选项，在此整张地图中是最 fuzzy 的决定：

- **Continue**——留下。不花、不丢。
- **`/clear`**——清空窗口，此处对后续无关时。
- **`/handoff`**——写可移植 markdown。范围窄：仅**新 harness**、**新目录**、**同事**，或 **phase 中途** fork 旁路。换来的是可移植性。
- **Subagent**——把紧范围任务发到自己的窗口，收回报告。
- **`/compact`**——压缩此上下文，seed 新会话。**默认**，在树底而非首选。

阅读 [PHASE-BOUNDARIES.md](PHASE-BOUNDARIES.md) 了解有序决策树——五个问题、每支背后的推理，以及 primary-source 成本为何让 **Continue** 要首先排除。在边界**处**做决定；phase 中途，继续或把剩余拆成 subagent。

## 独立技能

完全离开主流程。

- **`/grill-me`**——与 `/grill-with-docs` 相同的 relentless 采访，但**无状态**：本地不保存、不建 `CONTEXT.md`。**不在 working directory 中**时取用——打磨计划、设计、写作，任何其下无 repo 的内容。在 working directory 中用 `/grill-with-docs`：同一采访且留书面轨迹，严格更好。
- **`/grilling`**——采访原语本身：轮次、frontier、事实是 agent 的工作、决定是你的。`/grill-me` 和 `/grill-with-docs` 是两个命名入口；`/triage`、`/wayfinder`、`/improve-codebase-architecture` 内部都运行它。仅当你要无 wrapper 的采访时直接取用。
- **`/resolving-merge-conflicts`**——逐 hunk 处理进行中的 merge 或 rebase 冲突，按每侧 primary source 追溯的**意图**解决而非挑行，然后完成操作。从不运行 `--abort`。独立、离开每条 flow：已在冲突中途时取用。
- **`/prototype`**——回答一个设计问题的小型一次性程序：状态模型是否 feel right，或 UI 应什么样。throwaway 是写代码方式的约束，非销毁承诺：答案 fold 进真实代码，原型本身作为 **primary source** 留在 main 外的 `prototype/<name>` 分支，在实现 issue 上留指针。主流程步骤 2 的绕道，但任何纸上难 settle 的设计问题都可取用。
- **`/research`**——把阅读苦工委托给**后台 agent**：针对**primary sources** 调查问题，在 repo 留 cited Markdown。你继续工作。产出文件带入主流程 `/grill-with-docs`——research 喂养思考，不替代它。
- **`/to-questionnaire`**——挡路的东西不在你脑海或代码库，而在**别人那里**时，给他们写问卷填写。是 `/grill-me` 的 inverse：不采访你关于主题，而采访你关于**发送**——给谁、需要收回什么——问题瞄准缺口。收回的是 `/grill-with-docs` 或 `/to-spec` 的材料。
- **`/wizard`**——仅**人类**能做的步骤：配置基础设施、设置凭据或 CI secrets、点陌生第三方 dashboard、一次性迁移或 cutover。生成交互 bash 脚本，打开每个 URL、捕获每个值、写入 `.env` 和 GitHub secrets——流程不再每次向 agent 重讲。模型调用，agent 碰到只有你能过的墙时自取。agent 能自己做就应自己做；这是人类 genuinely 在 loop 的地方。
- **`/wait-what`**——消息没 land 时的纠正。对话中途、任何 skill 内使用，agent 用你缺的背景、plain English、`CONTEXT.md` 词汇 re-pitch 刚说的。事后有效；`/grill-with-docs` 是 upfront cure，早期 agreed 共享语言阻止 jargon 出现。
- **`/teach`**——多会话学概念，以当前目录为状态工作区。
- **`/writing-for-agents`**——为 agent 消费文档的参考：skill、AGENTS.md、被指向的 doc。

## 前置条件

**`/setup-matt-pocock-skills`**——首次 engineering flow 前运行，配置 issue tracker、triage 标签、其他 skill 假设的 doc 布局。自定义 issue tracker 也可。
