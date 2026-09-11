---
name: slides
description: 用精美模板生成高质量 HTML 演示文稿。用户提到 slides、presentation、PPT、deck、keynote、演示文稿或幻灯片时必须使用本技能，即使没有明确要求 HTML 或模板。同时覆盖多模板精修流程和快速自包含主题。任何创建、制作、生成演示文稿的请求都适用，不论文案怎么说。
license: MIT
author: yugasun
homepage: https://github.com/yugasun/slides-skills
version: 1.0.0
config:
  outputRoot: "~/slides"   # default output directory; override via --slides-root or user request
  previewOpen: true         # auto-open preview in browser after generation
---

# 交互式 HTML 幻灯片生成器

## 输出目录

生成的演示文稿默认保存在 `~/slides/<deck-name>/`。生成前，本技能会：

1. 把 `~` 展开成用户主目录
2. 若输出目录不存在则创建（`mkdir -p`）
3. 创建 `slides/<deck-name>/previews/`，存放工作流 A 的预览文件
4. 创建 `slides/<deck-name>/`，存放最终成稿

**自定义根目录**：用户指定了路径（例如「存到 `~/my-decks`」或「输出到 `/tmp/slides`」）就用用户的路径，不要盖掉明确要求。

**目录初始化示例**：
```bash
mkdir -p ~/slides/my-deck/previews
mkdir -p ~/slides/my-deck/previews
```

---

## 两条工作流

本技能支持 **两条工作流**：

- **工作流 A — Beautiful HTML Templates**（推荐）：32 套专业设计模板。适合要视觉辨识度、成稿更精致的演示。先问场合和气质，给出 3 个候选，再按真实模板的 HTML/CSS/JS 制作。
- **工作流 B — 内置 CSS 主题**：4 套 CSS 主题（Cyberpunk、Corporate、Minimal、Nature）。快，单文件自包含，无外部依赖。

**默认走工作流 A**，除非用户点名某个主题，或明确要最简/轻量输出。

---

## 工作流 A — Beautiful HTML Templates（推荐）

### 第 1 步 — 问清口味

选模板之前先问两件事：

> "选模板前先确认两件小事：
> 1. **用在什么场合？**（例如产品发布、研究分享、品牌宣言、课堂、团队复盘等）
> 2. **想要什么气质 / vibe？**（例如自信偏编辑感、温暖好玩、暗黑沉郁、安静文学等）"

等用户回答。不要跳过——用户亲口说的口味，推断简报补不回来。

### 第 2 步 — 读 index.json，短名单出 3 个候选

读取 `skills/ppt/beautiful-html-templates/index.json`。用用户说的 **场合 + 气质** 去对每套模板的 `mood`、`tone`、`formality`、`density`、`scheme`。

选出 **三套** 气质真的对得上、且彼此够不一样的模板（例如不要三套都是编辑风——选一套编辑风、一套更暖的备选、再加一套跳脱一点的 wildcard）。

### 第 3 步 — 给每个候选做标题页预览

对 3 个候选分别：

1. 读取 `skills/ppt/beautiful-html-templates/templates/<slug>/template.html`
2. 只抽出 **第一页**（封面/标题页）
3. 用 **用户真实的主题/标题/副标题/作者/日期** 替换占位内容
4. 存为 `~/slides/<deck-name>/previews/01-<slug>.html`
5. 初始化 `~/slides/<deck-name>/`，供后续成稿使用

用 `open <path>`（macOS）打开每个预览，并给用户发：

> "三套可以对比：
> 1. **<Template A>** — <一句话气质>
>    `~/slides/<deck-name>/previews/01-template-a.html`
> 2. **<Template B>** — <一句话气质>
>    `~/slides/<deck-name>/previews/02-template-b.html`
> 3. **<Template C>** — <一句话气质>
>    `~/slides/<deck-name>/previews/03-template-c.html`
>
> 哪套感觉对？"

等用户选。

### 第 4 步 — 做完整演示文稿

用户选定后：

1. 完整读取 `skills/ppt/beautiful-html-templates/templates/<slug>/template.html`
2. 按 [AGENTS.md](./beautiful-html-templates/AGENTS.md) §3 的规则改每一页——保住设计系统，只换占位内容
3. 按用户大纲增/删/拆页
4. **缺某种版式时**，用该模板的字体、色板、装饰语汇和间距节奏现做——见 [AGENTS.md](./beautiful-html-templates/AGENTS.md) §5
5. 确认导航（键盘/点击）正常
6. 最终成稿存为 `~/slides/<deck-name>/index.html`

### 第 5 步 — 打开并交付

用 `open <path>` 打开成稿。发送：

> "做好了。文稿在 `~/slides/<deck-name>/index.html` — 已在浏览器里打开。"

---

## 工作流 B — 内置 CSS 主题（兜底）

用户点名某个主题，或要自包含的最简输出时用这条。

### 主题选择

| 主题 | 风格 | 何时用 |
|---|---|---|
| **Cyberpunk** | 暗色、霓虹、未来感 | 默认——科技、游戏、创新 |
| **Corporate** | 浅色、专业、蓝/灰蓝 | 商务、正式汇报 |
| **Minimal** | 黑白、瑞士平面 | 学术、冷峻、编辑感 |
| **Nature** | 奶油/绿色、优雅衬线 | 温暖、有机、文学 |

**未指定主题时默认 Cyberpunk。**

### 组装流程

1. **读参考文件**：所选 CSS 主题 + `templates/template.html` + `templates/scripts.js` + `templates/layouts.md`
2. **载入模板**：从 `template.html` 起步
3. **注入 CSS**：把 `/* CSS_INJECTION_POINT */` 换成所选主题 CSS
4. **注入 JS**：把 `/* JS_INJECTION_POINT */` 换成 `scripts.js`，再把 `[TOTAL_SLIDES_COUNT]` 换成实际页数
5. **生成幻灯片**：按 `layouts.md` 的模式写 HTML
6. **注入幻灯片**：替换 `<!-- SLIDES_INJECTION_POINT -->`
7. **保存**：`~/slides/<deck-name>/index.html`

---

## 溢出防护（工作流 B）

幻灯片固定 **1280×720px**。溢出被隐藏，内容会被悄悄裁掉。

| 元素 | 上限 | 超出时 |
|---|---|---|
| 要点 | **5** | 拆成 2 页 |
| 卡片 | **3** | 用 `.compact` 或拆页 |
| 代码行 | **10** | 在 content-area 上用 `.scrollable` |
| 卡片正文 | 2 行 | 缩短 |

**规则**：
- 每页最多 5 条要点，每条最多 1–2 行
- 网格页最多 3 张卡片
- 不要在同一页叠要点 + 卡片 + 代码
- 用 `.compact` 缩小字号和间距
- 宁可拆页，不要硬塞

---

## 模板索引摘要

| Slug | 名称 | 气质 | 明暗 |
|---|---|---|---|
| 8-bit-orbit | 8-Bit Orbit | retro-tech, playful, cyberpunk | dark |
| biennale-yellow | Biennale Yellow | editorial, atmospheric, warm | light |
| block-frame | BlockFrame | neobrutalist, pastel-neon | mixed |
| blue-professional | Blue Professional | clean, modern, professional | light |
| bold-poster | Bold Poster | editorial, massive display | light |
| broadside | Broadside | dark editorial, orange accent | dark |
| capsule | Capsule | modular, pastel-pop | light |
| cartesian | Cartesian | quiet, warm, classical | light |
| cobalt-grid | Cobalt Grid | electric, graph-paper | dark |
| coral | Coral | cream/coral, oversized display | dark |
| creative-mode | Creative Mode | confident, multi-color | light |
| daisy-days | Daisy Days | cheerful, pastel, hand-drawn | light |
| editorial-tri-tone | Editorial Tri-Tone | dusty pink, mustard, burgundy | light |
| grove | Grove | forest-green, classical serif | dark |
| long-table | Long Table | cream/rust, supper-club | light |
| mat | Mat | dark sage, mid-century modern | dark |
| monochrome | Monochrome | ivory, all-black, literary | light |
| neo-grid-bold | Neo-Grid Bold | neo-brutalist, neon yellow | light |
| peoples-platform | People's Platform | activist, bold colors | light |
| pin-and-paper | Pin & Paper | yellow paper, handwritten | light |
| pink-script | Pink Script | hot pink, late-night luxury | dark |
| playful | Playful | sun-warm, indie launch | light |
| raw-grid | Raw Grid | neo-brutalist, thick borders | light |
| retro-windows | Retro Windows | Windows 95, pixel nostalgia | light |
| retro-zine | Retro Zine | riso-printed, beige/green | light |
| sakura-chroma | Sakura Chroma | vintage Japanese cassette | light |
| scatterbrain | Scatterbrain | post-it, pastel handwriting | light |
| signal | Signal | navy, bone, muted-gold | dark |
| soft-editorial | Soft Editorial | serif, warm paper, sage/blush | light |
| stencil-tablet | Stencil & Tablet | stencil-cut, earth palette | light |
| studio | Studio | black canvas, electric yellow | dark |
| vellum | Vellum | navy, yellow italic serif | dark |

完整元数据见 `beautiful-html-templates/index.json`。
