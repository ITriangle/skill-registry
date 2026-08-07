---
name: wayfinder
description: 将一次巨大工作——超过一个 agent 会话能 hold——规划为 issue tracker 上共享地图的决策 ticket，逐个解决直到通往目的地的路清晰。
disable-model-invocation: true
---

松散想法到了——太大放不下一个 agent 会话，且裹在 fog 中：从此处到**目的地**的路尚不可见。Wayfinding 是找那条路，不是冲向目的地。本 skill 在 repo issue tracker 上把路绘成**共享地图**，然后处理其**决策 ticket**——resolution 是决定、非要执行的构建切片——直到路线清晰。

目的地因努力而异，命名它是 charting 的第一动作——塑造每个 ticket。可能是 hand off 并迭代的 spec、规划前锁定的决定，或就地变更如数据结构迁移。地图 domain-agnostic——工程、课程内容，任何 fit 形状的。

## Plan, don't do

Wayfinder **默认是规划**：每个 ticket 解决一个决定，地图完成当路清晰——出发前没什么要决定。想直接做工作通常是已到地图边缘、该 hand off 的信号。努力可在 **Notes** 中 override——把执行带进地图本身——但 absent 那样，产出决定，非交付物。

## Refer by name

每个地图和 ticket 是 issue，故有**名称**——标题。人类读的一切——叙述、地图 Decisions-so-far——用该名称引用，从不是裸 id、编号或 slug。`#42, #43, #44` 墙 illegible；名称一眼可读。id 和 URL 不消失——名称包裹其 link——但骑在名称*内*，从不代替它。

## The Map

地图是本 repo issue tracker 上单个 issue，label `wayfinder:map`——canonical artifact。其 ticket 是地图的子 issue。

地图是**索引**，非仓库。它列出已做决定并指向持细节的 ticket；决定恰在一处——其 ticket——地图从不 restate，只 gist 并 link。

**地图、子 ticket、blocking、frontier 查询物理在哪是 tracker 特有。**issue tracker 应已提供——否则运行 `/setup-matt-pocock-skills`。查该 tracker doc 的「Wayfinding operations」看*本* repo 如何表达。未提供 tracker 则默认 local-markdown tracker。

### 地图 body

整张地图低分辨率，每会话加载一次。open ticket **不**列出——它们是 open 子 issue，靠查询找。

```markdown
## Destination

<地图尽头是什么样——此努力要找路的 spec、决定或变更。一两行；每会话选 ticket 前 orient 于此。>

## Notes

<领域；每会话应 consult 的 skill；此努力的 standing preferences>

## Decisions so far

<!-- 索引——每个 closed ticket 一行：够判相关性，再 zoom link 取 ticket 持的细节 -->

- [<closed ticket title>](link) — <answer 一行 gist>

## Not yet specified

<!-- 见 "Fog of war"：范围内尚不能 ticket 的 fog；frontier 推进时 graduate -->

## Out of scope

<!-- 见 "Out of scope"：判为超出目的地的 work；closed，永不 graduate -->
```

### Tickets

每个 ticket 是地图的**子 issue**；tracker issue id 是其身份。body 是问题，大小 fit 一个 100K token agent 会话：

```markdown
## Question

<此 ticket 解决的决定或调查>
```

每个 ticket 带 `wayfinder:<type>` label——`research`、`prototype`、`grilling`、`task` 之一（见 [Ticket Types](#ticket-types)）。

会话**claim** ticket 方式是把它分给驱动地图的 dev，**首先**，任何工作前，使并发会话跳过。assignee _即_ claim：open、未 assign 的 ticket 是 unclaimed。

Blocking 用 tracker **原生**依赖关系——essential，因在 tracker 自有 UI 可视化渲染 frontier，人类不用开地图就看到什么可取。仅缺原生 blocking 的 tracker 回退 body 惯例。ticket **unblocked** 当每个 blocking 它的 ticket 关闭；**frontier** 是 open、unblocked、unclaimed 子项——已知边缘。

答案不是 body 一部分——在 resolution 时记录（见 [Work through the map](#work-through-the-map)）。resolve ticket 时创建的 asset 从 issue link，不 paste 进 body。

## Ticket Types

每个 ticket 要么是 **HITL**——人类在 loop，与人类*一起*工作、人类为自己发言——要么是 **AFK**，agent 独自驱动。HITL ticket 只通过那次 live 交换 resolve；agent 从不代人类那一侧（grilling agent 自己答自己的 question 就破了此条）。

- **Research**（AFK）：读文档、第三方 API 或本地资源如知识库，surface 决定等待的事实。由 `/research` **subagent** resolve。需要当前 working directory 外知识时用。
- **Prototype**（HITL）：通过便宜粗糙具体 artifact 提高讨论保真度——outline、rough take、stub，或通过 /prototype skill 的 UI/logic 代码。把 prototype link 为 asset。当「应长什么样」或「应如何 behave」是关键 question 时用。
- **Grilling**（HITL）：对话。默认情形。始终 invoke /grilling 和 /domain-modeling skill。
- **Task**（HITL 或 AFK）：决定*之前*必须发生的手工工作——无要决定的、无要 prototype 或 research，但讨论 blocked 直到做完。注册服务以便 judge API、provision 访问、搬数据以便看形状。这是*做*而非决定的唯一类型——且因 unblock 决定而 earned，非交付目的地。agent 能独自驱动则 AFK；否则给人类精确 checklist（HITL）。工作完成时 resolve；answer 记录做了什么及后续 ticket 依赖的事实（凭据位置、新 URL、行数）。

## Fog of war

地图*故意*不完整：不要 chart 尚看不见的。live ticket 之外是 **fog of war**——你能感到要来、尚不能钉下的决定与调查的 dim view，因为它们挂在仍 open 的 question 上。resolve ticket 清其前方的 fog，把现已可 spec 的 graduate 成新 ticket——一次一个，直到通往目的地的路清晰、无 ticket 剩。

地图 **Not yet specified** 写下那 dim view：suspected question、稍后 revisit 的区域。它是朝向目的地的 undiscovered frontier——此处一切 in scope，只是不够 sharp 无法 ticket。按 view 允许写松或写满；也是 collaborator 读努力方向的 signpost。

**Fog 还是 ticket？**测试是你*现在*能否精确陈述 question——*不是*你现在能否回答。

- **Ticket when** question 已 sharp——即使 blocked、尚不能 act。
- **Not yet specified when** 尚不能那样 sharp phrase。不要把 fog pre-slice 成 ticket 大小：它比 ticket coarse，一片 fog 到 frontier 可能 graduate 成几个 ticket，或 none。

**Not yet specified** 排除已决定（Decisions so far）、已是 live ticket 的、以及 out of scope（下一节）。

## Out of scope

Fog 只朝目的地*聚集*。目的地固定 scope，超出它的工作是 **out of scope**——不是 fog，不属于 **Not yet specified**。consciously 判为超出*此*努力的 work 进地图自有 **Out of scope** section。超出 scope 的工作永不 graduate——frontier 止于目的地——仅当目的地重画时 return，且作为 fresh effort，非 resume。

判 out of scope 是 scoping act，非 route 上一步。已存在 ticket  turns out 在目的地之外——charting 时 mis-scope，或 resolution 暴露——**close it**（closed ticket 明确 off frontier），在 **Out of scope** 留一行：gist 加为何 out of scope，link closed ticket。不进 **Decisions so far**，它记录实际走过的 route——scope 边界不是其上一步。

## Invocation

两种模式。无论哪种，**每会话 resolve 不超过一个 ticket**——research ticket 例外。

### Chart the map

用户用松散想法调用。

1. **命名目的地。**跑 `/grilling` 和 `/domain-modeling` 会话钉住地图要找的路——spec、决定或变更。目的地固定 scope，故首先 settle。
2. **Map the frontier。**再 grill，这次 **breadth-first**：fan 出整个空间而非深钻任一线，surface open 决定与现在可走的第一步。**若此步 surface 无 fog**——路已清晰、全程小到一会话——不需要地图。停下问用户想如何继续。
3. **创建地图**（label `wayfinder:map`）：填 Destination 和 Notes，Decisions-so-far 空，fog sketch 进 **Not yet specified**。
4. **创建现在能 specify 的 ticket** 为地图子 issue——然后**第二轮** wire blocking edges（issue 需 id 才能互引）。wiring 把它们排成 frontier 和 blocked；尚不能 specify 的留 fog——**Not yet specified** section。
5. **Fire research subagents。**对每个刚建的 `research` ticket，spin `/research` subagent 并行 resolve，findings capture 在 throwaway `research/<name>` branch，ticket 上 context pointer。
6. 停——charting 是一会话的工作；它 hand-resolve  nothing。

### Work through the map

用户用地图（URL 或编号）调用。ticket **可选**——无则你选下一个决定，非用户。

1. 加载**地图**——低分辨率视图，非每个 ticket body。
2. 选 ticket。用户命名则用。否则按顺序取第一个 frontier ticket。**Claim**：任何工作前 assign 给自己。
3. Resolve——**按需 zoom**：fetch 相关或 closed ticket 完整 body；invoke `## Notes` 命名的 skill。不确定则用 `/grilling` 和 `/domain-modeling`。
4. 记录 resolution：answer 作为 **resolution comment** 发帖，**close** issue，**append context pointer** 到地图 Decisions-so-far。
5. 加新 surface 的 ticket（create-then-wire）；graduate answer 使可 specify 的 fog，从 **Not yet specified** 清掉每片 graduated patch，使其只作为新 ticket 存在。若 answer 揭示 ticket——此或其他——在目的地之外，**rule out of scope** 而非在 route 上 resolve。若决定 invalidate 地图其他部分，更新或删那些 ticket。

用户可并行跑 unblocked ticket，预期其他会话并发编辑 tracker。
