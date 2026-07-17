---
name: llm-wiki
description: 当用户需求匹配默认 skill 描述时使用：构建并维护由 LLM 维护的个人知识库。触发：摄取来源进 wiki、查询 wiki 知识、lint 质量、'加入 wiki'、'关于 X 我知道什么'，或提到 LLM wiki / Karpathy wiki。 当需求不匹配上述描述、只是普通对话，或已有更具体的 skill 覆盖时不要用。
---

# 中文导读

- 使用场景：当用户需求匹配默认 skill 描述时使用：构建并维护由 LLM 维护的个人知识库。触发：摄取来源进 wiki、查询 wiki 知识、lint 质量、'加入 wiki'、'关于 X 我知道什么'，或提到 LLM wiki / Karpathy wiki。
- 不适用：当需求不匹配上述描述、只是普通对话，或已有更具体的 skill 覆盖时不要用。

# 上游说明原文

# LLM Wiki（Karpathy 风格）

用 LLM 构建并维护个人知识库。你管理两个目录：`raw/`（不可变来源）与编译后的知识页（`wiki/` 主题目录，或本项目的 `entities/` / `concepts/` / `synthesis/` 等）。来源进入 `raw/`，再编译为文章；wiki 随时间复利增长。

Karpathy 核心观点：

- 「LLM 撰写并维护 wiki；人类阅读并提问。」
- 「Wiki 是持久、可复利的产物。」

操作化实践参考 [astro-han/karpathy-llm-wiki](https://github.com/astro-han/karpathy-llm-wiki)；理念参考 [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 与 [LLM Wiki Architecture](https://yugasun.com/post/llm-wiki-architecture)。

## 标准口令

| 口令 | 行为 |
|------|------|
| `加入 wiki：…` | Ingest |
| `关于 X 我知道什么` | Query（默认不写文件） |
| `lint wiki` | Lint（优先跑 `scripts/lint-wiki.sh`） |
| `本周回顾` / `本月回顾` | 运营回顾，见 [references/ops-loop.md](references/ops-loop.md) |

随手记先入 `raw/inbox/`，再 ingest。分通道摄取见 [references/source-adapters.md](references/source-adapters.md)。

## Architecture

三层，均在用户项目根（或已解析的 wiki 根）下：

**raw/** — 不可变来源（`inbox/` 除外可移动）。类型布局推荐子目录：`inbox/` `articles/` `papers/` `transcripts/` `notes/` `git/` `lark/` `mail/` `meeting/` `assets/`。

**编译知识层** — 你拥有完整写权限。两种兼容布局（以既有 `SCHEMA.md` / 目录为准，勿强行迁移）：

1. **主题布局**（与参考仓库一致）：`wiki/<topic>/<article>.md`，仅一层主题子目录。
2. **类型布局**（本仓库 PersonalWiki）：`entities/` `concepts/` `comparisons/` `queries/` `synthesis/`，外加 `_archive/`。

特殊文件（在 wiki 根，主题布局下即 `wiki/` 内）：

- `index.md` — 全局索引：每文一行，按主题/类型分组，含链接 + 摘要 + Updated。
- `log.md` — 追加式操作日志（`## [YYYY-MM-DD] <action> | <主题>`）。

**SCHEMA.md / 本 SKILL.md** — 约定层：结构与工作流规则。本项目 durable wiki 在 `PersonalWiki/`；文档默认中文。

模板在相对本文件的 `references/`。确定性脚本：`scripts/init-wiki.sh`、`lint-wiki.sh`、`new-raw.sh`、`rehash-raw.sh`。

### Initialization

默认在**首次 Ingest** 时触发。检查 `raw/` 与编译知识层是否存在；只创建缺失项，永不覆盖已有文件。

可用启动脚本（推荐本技能）：

```bash
bash "${SKILL_DIR}/scripts/init-wiki.sh" "$WIKI" "$DOMAIN"
printf '%s\n' "$WIKI" > "$HOME/.llm-wiki"
```

最小手建（主题布局）：

- `raw/`（可含 `.gitkeep`）
- `wiki/`（可含 `.gitkeep`）
- `wiki/index.md` — 标题 `# Knowledge Base Index` / `# Wiki 索引`，正文可空
- `wiki/log.md` — 标题 `# Wiki Log` / `# Wiki 日志`，正文可空

Wiki 根解析：用户显式路径 > `WIKI_PATH` > `~/.llm-wiki` > 当前目录（已有 `index.md` + `log.md` 且存在 `raw/` 或 `SCHEMA.md`）> `~/wiki`。

若 Query / Lint 找不到 wiki 结构：告知用户「先跑一次 ingest 以初始化 wiki」，不要自动创建。非空且无关目录勿初始化，除非用户批准。

---

## Ingest

把来源抓进 `raw/`，再编译进知识层。**两步都必须做，无例外。**

### Fetch（raw/）

1. 用环境提供的网页/文件工具取得内容；无法访问则请用户粘贴。
2. 选择主题目录：先复用已有 `raw/` 子目录；仅在主题确实不同时新建。
3. 保存为 `raw/<topic>/YYYY-MM-DD-descriptive-slug.md`。
   - slug 来自标题，kebab-case，最长 60 字符。
   - 发表日未知 → 文件名可省略日期前缀；元数据 `Published` 仍写，值为 `Unknown`。
   - 重名则加 `-2`、`-3` 后缀。
   - 元数据：来源 URL、Collected、Published；若 `SCHEMA.md` 要求，另加 YAML frontmatter 与正文 `sha256`。
   - 忠实保留原文；清理格式噪声；不改写观点。

   格式见 [references/raw-template.md](references/raw-template.md)。
   分通道字段与清洗规则见 [references/source-adapters.md](references/source-adapters.md)。
   可用 `bash "${SKILL_DIR}/scripts/new-raw.sh" "$WIKI" <source-type> "标题"` 生成骨架。

### Compile（知识页）

判断新内容归属：

- **与既有文章同一核心论题** → 合并进该文；把新来源加入 Sources/Raw；更新受影响章节。
- **新概念** → 在最相关主题（或类型）目录新建文章；文件名用概念名，不用 raw 文件名。
- **跨多主题** → 放最相关目录；用 See Also / `[[wikilink]]` 互链。

以上可并存：一次来源可「合并一文 + 另建一文」。始终检查事实冲突：矛盾处标注来源；合并时写在该文内；分属两文则两边都注并互链。

文章格式见 [references/article-template.md](references/article-template.md)。要点：

- Sources：作者/机构/出版物 + 日期，分号分隔。
- Raw：指向 `raw/` 的 markdown 链接（或 frontmatter `sources`），分号分隔。
- 主题布局下，从 `wiki/<topic>/` 出发的相对路径为 `../../raw/<topic>/<file>.md`。

### Cascade Updates

主文之后检查涟漪：

1. 扫描同主题（或同类型）目录中受影响的文章。
2. 扫描 `index.md` 中其他主题的相关条目。
3. 对内容实质受影响的文章全部更新，并刷新其 Updated。

**Archive 页永不级联更新**（时点快照）。未说明变更集时，勿盲改 10+ 页。

### Post-Ingest

更新 `index.md`：为每个触达文章增改条目；新主题节加一行描述。Updated = 知识内容最后实质变更日，不是文件系统 mtime。格式见 [references/index-template.md](references/index-template.md)。

追加 `log.md`：

```text
## [YYYY-MM-DD] ingest | <主文章标题>
- Updated: <级联更新的文章标题>
- Updated: <另一篇>
```

无级联则省略 `- Updated:` 行。

批量摄取：先读完全部来源，识别共享概念，再成批编译。

---

## Query

搜索 wiki 并回答。触发示例：

- 「关于 X 我知道什么？」
- 「总结与 Y 相关的一切」
- 「基于我的 wiki 比较 A 和 B」

### Steps

1. 读 `index.md` 定位相关文章；有 `SCHEMA.md` 时一并阅读。
2. 阅读这些文章并综合答案。
3. **优先 wiki 内容**，而非训练先验。对话中引用：`[文章标题](wiki/topic/article.md)` 或 `[[文章标题]]`（项目根相对路径用于对话；wiki 文件内用相对当前文件的路径 / wikilink）。
4. 答案输出在对话中。**除非被要求，否则不写文件。**

### Archiving

仅当用户明确要求归档或保存答案到 wiki：

1. 写成新 wiki 页。见 [references/archive-template.md](references/archive-template.md)。把对话中的项目根相对路径改写成文件相对路径（同目录用文件名；跨主题用 `../topic/file.md`）或 `[[wikilink]]`。
   - Sources：指向答案所引的 **wiki 文章**（不是 raw）。
   - **无 Raw 字段**。
   - 文件名反映查询主题，如 `transformer-architectures-overview.md`。
   - 放在最相关主题目录（或本项目的 `queries/`）。
2. **始终新建页**。永不把归档问答合并进既有文章。
3. 更新 `index.md`；Summary 前缀 `[Archived]` 或 `[归档]`。
4. 追加 `log.md`：

   ```text
   ## [YYYY-MM-DD] query | Archived: <page title>
   ```

不要归档琐碎查询。

---

## Lint

质量检查。两类权限不同。

### Deterministic Checks（自动修复）

优先运行：

```bash
bash "${SKILL_DIR}/scripts/lint-wiki.sh" "$WIKI"
```

脚本覆盖索引缺失/断链、知识页 frontmatter 必填字段、wikilink、raw 引用、孤儿页启发式。Agent 仍负责冲突与过期主张等启发式项。

**Index consistency** — 对比 `index.md` 与实际知识页文件（排除 `index.md`、`log.md`、`SCHEMA.md`）：

- 文件存在但不在索引 → 补条目，摘要用 `(no summary)` / `(无摘要)`；Updated 优先用文内元数据，否则用 mtime。
- 索引指向不存在文件 → 标 `[MISSING]` / `[缺失]`；不擅自删条目。

**Internal links** — 检查知识页正文与 Sources 中的链接 / `[[wikilink]]`（Raw 字段由下一项校验；index/log 由上一项处理）：

- 目标不存在 → 在知识层按同名搜索。
  - 恰好一个匹配 → 改路径/链接。
  - 零个或多个 → 报告用户。

**Raw references** — Raw / `sources` 中每个指向 `raw/` 的链接必须存在：

- 不存在 → 在 `raw/` 按同名搜索；唯一匹配则改路径；否则报告。

**See Also** — 在各主题/类型目录内：

- 补上明显缺失的相关文交叉引用。
- 删除指向已删文件的链接。

### Heuristic Checks（只报告）

- 跨文事实矛盾；来源分歧却缺少冲突标注
- 被更新来源取代的过期主张
- 无入链孤儿页
- 缺少跨主题引用
- 高频提及却无独立页的概念
- 归档页所引源文自归档后已 substantively 更新
- （若使用 frontmatter）`confidence: low` / `contested: true` / 非空 `contradictions`

### Post-Lint

```text
## [YYYY-MM-DD] lint | <N> issues found, <M> auto-fixed
```

---

## Conventions

- 标准 Markdown；链接在文件内用相对路径，或本项目约定的 `[[wikilink]]`。
- 主题布局：`wiki/` 仅一层主题子目录，不再嵌套。
- 日志 / Collected / Archived 用当天日期；Updated = 知识内容实质变更日；Published 来自来源（未知则 `Unknown`）。
- 对话引用用项目根相对路径；wiki 文件内用相对当前文件的路径。
- Ingest 更新 `index.md` + `log.md`。Archive（来自 Query）两者都更新。Lint 更新 `log.md`（自动修索引时才改 `index.md`）。纯 Query 不写任何文件。
- 优先更少但更强的页面；保留不确定性，勿用最新观点抹掉旧矛盾。
- 完整约定以该 wiki 的 `SCHEMA.md` 为准（若存在）。

## 参考模板

| 文件 | 用途 |
|------|------|
| [references/raw-template.md](references/raw-template.md) | 不可变来源 |
| [references/source-adapters.md](references/source-adapters.md) | 博客/PDF/对话/Git/飞书邮件会议适配 |
| [references/ops-loop.md](references/ops-loop.md) | 口令、inbox、周/月回顾 |
| [references/article-template.md](references/article-template.md) | 编译后的知识文章 |
| [references/archive-template.md](references/archive-template.md) | 查询归档（时点快照） |
| [references/index-template.md](references/index-template.md) | 全局索引 |
| [references/log-template.md](references/log-template.md) | 操作日志 |
| [references/entity-template.md](references/entity-template.md) 等 | 类型布局专用页 |
