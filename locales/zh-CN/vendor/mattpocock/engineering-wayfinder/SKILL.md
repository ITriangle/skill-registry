---
name: wayfinder
description: 将一大块工作——大到单个 agent 会话无法容纳——规划为 issue tracker 上由调查 ticket 组成的共享地图，并逐个解决，直到通往目的地的道路清晰。
disable-model-invocation: true
---

一个松散想法出现了——它大到单个 agent 会话无法容纳，并被迷雾包裹：从这里通往**目的地**的道路尚不可见。Wayfinding 的目标是找到道路，而不是径直冲向目的地。本技能在仓库 issue tracker 上将道路绘制成一张**共享地图**，然后逐个处理 ticket，直到路线清晰。

每项工作的目的地都不同，为其命名是绘图的第一个动作——它塑造每个 ticket。目的地可能是一份待交接和迭代的 spec、规划开始前必须锁定的决策，或直接完成的变更，例如数据结构迁移。地图与领域无关——工程工作、课程内容，任何符合这种形态的事项都可以。

## 规划，不执行

Wayfinder 默认用于**规划**：每个 ticket 解决一个决策；当道路清晰、在他人真正执行前没有任何待决事项时，地图完成。想要直接动手的冲动，通常意味着你已到达地图边缘，该交接了。一项工作可以在其 **Notes** 中覆盖默认行为——将执行本身纳入地图——但没有这种说明时，只产出决策，不产出交付物。

## 以名称引用

每张地图和每个 ticket 都是 issue，因此都有一个**名称**——即标题。在所有供人阅读的内容中——叙述、地图的 Decisions-so-far——通过名称引用，绝不要只写裸 id、数字或 slug。满墙的 `#42, #43, #44` 无法阅读；名称一眼可懂。id 和 URL 不会消失——名称包裹着链接——但它们位于名称*内部*，绝不能代替名称。

## 地图

地图是此仓库 issue tracker 上加有 `wayfinder:map` label 的单个 issue——规范工件。它的 ticket 是地图的子 issue。

地图是**索引**，不是存储。它列出已经做出的决策，并指向保存详情的 ticket；一个决策只存在于一个位置——它的 ticket——因此地图绝不重述，只提供要点并链接。

**地图、子 ticket、阻塞关系和 frontier query 在物理上如何存储，取决于 tracker。** issue tracker 应该已经提供；如果没有，运行 `/setup-matt-pocock-skills`。查阅 tracker 文档中的“Wayfinding operations”一节，了解*此*仓库如何表达这些内容。如果没有提供 tracker，默认使用 local-markdown tracker。

### 地图正文

整张地图的低分辨率视图，每个会话只加载一次。**不**列出未关闭 ticket——它们是 open child issue，通过 query 查找。

```markdown
## 目的地

<到达此地图终点是什么样——本项工作要寻找道路通往的 spec、决策或变更。一两行；每个会话选 ticket 前都先以此校准方向。>

## 备注

<领域；每个会话都应查阅的技能；本项工作的长期偏好>

## 迄今决策

<!-- 索引——每个已关闭 ticket 一行：信息足以判断相关性，然后通过链接放大查看该 ticket 保存的细节 -->

- [<已关闭 ticket 标题>](link) — <答案的一行要点>

## 尚未明确

<!-- 见“战争迷雾”：范围内但还无法建立 ticket 的迷雾；随着 frontier 推进而升级 -->

## 范围之外

<!-- 见“范围之外”：被排除在目的地之外的工作；已关闭，永不升级 -->
```

### Ticket

每个 ticket 都是地图的**子 issue**；tracker issue id 就是它的身份。正文是要回答的问题，大小控制在一个 100K token 的 agent 会话内：

```markdown
## 问题

<此 ticket 要解决的决策或调查>
```

每个 ticket 带有一个 `wayfinder:<type>` label——`research`、`prototype`、`grilling`、`task` 之一（见 [Ticket 类型](#ticket-types)）。

会话开始处理 ticket 前，要**首先**将其分配给推动地图的 dev，以此**认领** ticket，使并发会话跳过它。assignee *就是*认领标记：open 且 unassigned 的 ticket 尚未被认领。

阻塞关系使用 tracker 的**原生** dependency relationship——这至关重要，因为它会在 tracker 自身 UI 中*可视化*呈现 frontier，使用户无需打开地图就能看到哪些 ticket 可领取。只有缺少原生 blocking 的 tracker 才回退到正文约定。当所有阻塞某 ticket 的 ticket 都已关闭时，该 ticket **未被阻塞**；**frontier** 是所有 open、未阻塞且未认领的 child——已知世界的边缘。

答案不属于正文——它在解决时记录（见[处理整张地图](#work-through-the-map)）。解决 ticket 时创建的工件从 issue 链接，不要粘贴进去。

<a id="ticket-types"></a>

## Ticket 类型

每个 ticket 都属于 **HITL**（human in the loop，由能代表自己意见的人类共同处理）或 **AFK**（由 agent 独自推动）。HITL ticket 只能通过实时交流解决；agent 绝不能代替人类一方发言（自己回答问题的 grilling agent 已经破坏了规则）。

- **Research**（AFK）：阅读文档、第三方 API 或 knowledge base 等本地资源。创建一份 Markdown 摘要作为链接工件。当需要当前工作目录之外的知识时使用。
- **Prototype**（HITL）：制作便宜、粗糙、具体、可供反馈的工件来提升讨论保真度——outline、rough take、stub，或通过 `/prototype` 技能制作 UI/逻辑代码。将 prototype 作为工件链接。当关键问题是“应该长什么样”或“应该如何表现”时使用。
- **Grilling**（HITL）：通过 `/grilling` 和 `/domain-modeling` 技能进行对话，每次只问一个问题。默认类型。
- **Task**（HITL 或 AFK）：在做出*决策*前必须完成的手工作业——没有要决定、prototype 或 research 的内容，但在完成工作前讨论受阻。例如注册服务以便评估其 API、开通访问权限、搬移数据以观察其形态。这是唯一一种*执行*而非决策的类型——它的合理性来自解除决策阻塞，而不是交付目的地。agent 能独自推动时使用 AFK；否则向人类提供精确 checklist（HITL）。工作完成即解决；答案记录完成了什么，以及后续 ticket 所依赖的结果事实（credential 位置、新 URL、row count）。

## 战争迷雾

地图是*有意*不完整的：不要绘制尚且看不见的内容。实时 ticket 之外是**战争迷雾**——你能隐约看出即将出现某些决策和调查，却因它们依赖仍未解决的问题而无法准确界定。解决一个 ticket 会清除其前方迷雾，把现在可以明确的内容升级成新 ticket——一次一个，直到通往目的地的道路清晰且没有 ticket 剩余。

地图的 **Not yet specified** 一节记录这种模糊视野：疑似问题、以后需要回访的区域。它是*朝向*目的地、尚未发现的 frontier——这里的一切都在范围内，只是还不够清晰，无法成为 ticket。按视野允许的粗略或完整程度书写；它也为阅读本项工作方向的协作者充当路标。

**迷雾还是 ticket？** 判断标准是现在能否精确陈述问题——*不是*现在能否回答问题。

- 当问题已经清晰时建立 **ticket**——即使它被阻塞、目前无法处理。
- 当问题还无法如此清晰地表达时放入 **Not yet specified**。不要把迷雾预先切成 ticket 大小：它比 ticket 更粗；frontier 到达时，一片迷雾可能升级成多个 ticket，也可能一个都没有。

**Not yet specified** 不包括已经决定的内容（Decisions so far）、已有实时 ticket，以及范围外内容（下一节）。

## 范围之外

迷雾只会聚集在*通往*目的地的方向。目的地固定范围，因此超出目的地的工作属于**范围之外**——它不是迷雾，也不属于 **Not yet specified**。它在地图上拥有自己的 **Out of scope** 一节：记录你有意识排除在*本项工作*之外的内容。决定内容落在这里的是范围，而非清晰度。

范围外工作永远不会升级——frontier 在目的地停止——只有重绘目的地后它才会回来，而且应作为全新工作，而不是恢复旧工作。

排除范围是一项范围界定动作，不是路线上的一步。当一个已经存在的 ticket 后来被发现位于目的地之外——可能绘图时错误纳入，也可能解决其他 ticket 后才暴露——**关闭它**（关闭的 ticket 明确不在 frontier），并在 **Out of scope** 一节留一行：链接已关闭 ticket，说明要点及其为何超出范围。不要将其加入 **Decisions so far**，后者记录实际走过的路线——范围边界不是路线上的一步。

## 调用

有两种模式。无论哪种，**每个会话都绝不要解决超过一个 ticket。**

### 绘制地图

用户以松散想法调用。

1. **命名目的地。** 运行 `/grilling` 和 `/domain-modeling` 会话，明确这张地图要通往什么——spec、决策或变更。目的地固定范围，因此必须首先落定。
2. **绘制 frontier。** 再次 grill，这次采用**广度优先**：横跨整个空间展开，而不是深入某一条线，揭示待决事项和当前可执行的第一步。**如果这没有揭示任何迷雾**——通往目的地的道路已经清晰、整个旅程小到单个会话可以完成——就不需要地图。停止并询问用户希望如何继续。
3. **创建地图**（label `wayfinder:map`）：填写 Destination 和 Notes，Decisions-so-far 为空，在 **Not yet specified** 中勾勒迷雾。
4. **把当前能够明确的 ticket 创建为地图的 child issue**——然后在**第二遍**连接 blocking edge（issue 必须先有 id 才能相互引用）。连接会把它们分成 frontier 和 blocked；所有尚不能明确的内容继续留在迷雾中——即 **Not yet specified** 一节。
5. 停止——绘制地图占用一个完整会话；不要同时解决 ticket。

<a id="work-through-the-map"></a>

### 处理整张地图

用户以地图（URL 或编号）调用。ticket **可选**——如果没有指定，由你选择下一个决策，而不是让用户选。

1. 加载**地图**——低分辨率视图，而不是每个 ticket 的正文。
2. 选择 ticket。如果用户点名，使用它；否则按顺序选择第一个 frontier ticket。**认领它**：在开展任何工作前将其分配给自己。
3. 解决它——**按需放大**：需要时获取相关或已关闭 ticket 的完整正文；调用 `## Notes` block 中指定的技能。如有疑问，使用 `/grilling` 和 `/domain-modeling`。
4. 记录解决结果：将答案发布为**解决 comment**，**关闭** issue，并向地图 Decisions-so-far **追加上下文指针**。
5. 添加新发现的 ticket（先创建、后连接）；将答案使之变得明确的迷雾升级，并从 **Not yet specified** 中清除每一片已升级内容，使其只存在于新 ticket 中。如果答案揭示某个 ticket——当前 ticket 或其他 ticket——位于目的地之外，就将它**排除在范围外**，而不是把它当作路线的一部分解决。如果决策使地图其他部分失效，更新或删除对应 ticket。

用户可能并行运行未阻塞 ticket，因此要预期其他会话会同时编辑 tracker。
