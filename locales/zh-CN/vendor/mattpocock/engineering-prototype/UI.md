# UI Prototype

在单一路由上生成**几种 radically different UI 变体**，从底部浮动 bar 切换。用户在浏览器里翻变体，选一个（或从每个偷一点），其余扔掉。

若问题是 logic/state 而非长什么样——错分支。用 [LOGIC.md](LOGIC.md)。

## 何时是正确形状

- 「这页应该长什么样？」
- 「commit 前想看 dashboard 几个选项。」
- 「给 settings 屏试不同 layout。」
- 用户否则会在脑子里花一天在三张模糊 mock 间选。

## 两种子形状——强烈偏好子形状 A

UI prototype **贴着 app 其余部分**时更易判断——真 header、真 sidebar、真数据、真密度。孤立 throwaway route 是真空：每个变体单独看都 fine。有 plausible 现有 page 可 host 变体时默认子形状 A。仅当原型真无附近 home 时才子形状 B。

### 子形状 A——对现有页的 adjustment（首选）

route 已存在。变体在**同一路由**渲染，由 `?variant=` URL search param 门控。现有 data fetching、params、auth 都留——只 swap 渲染。默认；无具体理由不选。

若原型是给尚无 page 但*自然住在某页内*的东西（dashboard 新区块、settings 新 card、现有 flow 新步）——仍是子形状 A。在 host page 内 mount 变体。

### 子形状 B——新 page（最后手段）

仅当被原型东西真无现有 page 可住——如全新顶层 surface，或无法 sensible embed 的 flow。

创建**throwaway route**，遵守项目已有 routing 惯例——不要发明新顶层结构。命名明显是原型（path 或文件名含 `prototype`）。同样 `?variant=` 模式。

commit 子形状 B 前 sanity-check：真无现有 page 可 embed？空 route 藏 populated 会暴露的设计问题。

两子形状底部浮动 bar 相同。

## 流程

### 1. 陈述问题并选 N

默认 **3 个变体**。超过 5 不再 radically different 而成 noise——cap 在那里。

一行写下计划，在原型位置或文件顶 comment：

> "Three variants of the settings page, switchable via `?variant=`, on the existing `/settings` route."

用户在场 push back 与否都 work。

### 2. 生成 radically different 变体

起草每个变体。每个遵守：

- 页面目的及可访问数据。
- 项目 component library / 样式系统（TailwindCSS、shadcn、MUI、plain CSS 等）。
- 清晰 exported component 名，如 `VariantA`、`VariantB`、`VariantC`。

变体必须**结构不同**——不同 layout、信息层次、不同 primary affordance，不只是颜色。三个略调 card grid 不是 UI prototype，是 wallpaper。两 draft 太像，用明确「不要用 card grid」guidance 重做其一。

### 3. 接线在一起

在 route 上建单一 switcher：

```tsx
// pseudo-code — adapt to the project's framework
const variant = searchParams.get('variant') ?? 'A';
return (
  <>
    {variant === 'A' && <VariantA {...data} />}
    {variant === 'B' && <VariantB {...data} />}
    {variant === 'C' && <VariantC {...data} />}
    <PrototypeSwitcher variants={['A','B','C']} current={variant} />
  </>
);
```

子形状 A（现有 page）：switcher 上方保留所有现有 data fetching；仅 rendered subtree 按变体变。

子形状 B（新 page）：throwaway route 在 `/prototype/<name>` mount 同一 switcher。

### 4. 构建浮动 switcher

屏幕底部中央小 fixed bar，三块：

- **左箭头**——前一变体（wrap）。
- **变体 label**——当前变体 key，若变体 export 名则一并显示。如 `B — Sidebar layout`。
- **右箭头**——下一变体（wrap）。

行为：

- 点箭头更新 URL search param（用框架 router——Next 上 `router.replace`，React Router 上 `navigate` 等），变体可分享、reload-stable。
- 键盘：`←` `→` 也可 cycle。`<input>`、`<textarea>`、`[contenteditable]` focus 时不 intercept。
- 与页面视觉区分（如高对比 pill、轻 shadow），明显不是被评估设计的一部分。
- 生产 build 隐藏——`process.env.NODE_ENV !== 'production'` 或等价 gate，避免 stray 原型 merge ship bar。

switcher 放单一共享 component，两子形状复用。位置在项目 shared UI 所在处。

### 5. 交付

给出 URL（及 `?variant=` keys）。用户有空时翻。有趣反馈通常是**「我要 B 的 header 加 C 的 sidebar」**——那才是他们真想要的设计。

### 6. Capture 答案并清理

变体胜出后，capture 答案——哪个变体及为何——再按 [SKILL](SKILL.md) capture 原型。winner fold 进真实代码，其余移到 throwaway branch，不进 main：

- **子形状 A**——winner fold 进现有 page；从 main drop 输家变体和 switcher。
- **子形状 B**——胜出变体 promote 到真 route；从 main drop throwaway route 和 switcher。

完整变体集是 primary source，故 landing 在 throwaway branch 非 bin——变体 component 和 switcher 留 main 会 fast rot、迷惑下一位读者。

## Anti-patterns

- **仅颜色或 copy 不同的变体。**那是 tweak，非原型。真变体在结构上 disagree。
- **变体间共享太多代码。**共享 `<Header>` fine；共享 `<Layout>` defeat 目的。每变体应能扔掉 layout。
- **变体接真实 mutation。**只读原型 fine。变体若要 mutate，指 stub——问题是「应长什么样」，非「backend 是否 work」。
- **直接把原型 promote 到生产。**变体代码在原型约束下写（无测试、minimal 错误处理）。fold 时正经重写。
