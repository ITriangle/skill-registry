# {标题}

> Source: {URL 或来源说明}
> Collected: {YYYY-MM-DD}
> Published: {YYYY-MM-DD 或 Unknown}

{原文内容。忠实保留语义；可清理多余空白、坏掉的 HTML、导航噪音；不要改写观点或改变含义。}

---

## 命名

- 推荐：`raw/<topic>/YYYY-MM-DD-descriptive-slug.md`
- slug：来自标题，kebab-case，最长约 60 字符
- 发表日期未知：可省略日期前缀；`Published` 仍写 `Unknown`
- 重名：追加 `-2`、`-3` …

## PersonalWiki 变体（可选 frontmatter）

当 `SCHEMA.md` 要求 YAML 与正文哈希时，在标题块前增加：

```yaml
---
title: 来源标题
source_url: https://example.com
ingested: YYYY-MM-DD
published: YYYY-MM-DD
sha256: <frontmatter 后正文的哈希>
source_type: blog | pdf | chat-export | git | lark | mail | meeting | inbox | article | paper | transcript | note | file
---
```

`sha256` 只覆盖 frontmatter 之后的正文。重新摄取时比对哈希，报告未变或漂移。

分通道落点与清洗规则见 [source-adapters.md](source-adapters.md)。可用 `scripts/new-raw.sh` 生成骨架，`scripts/rehash-raw.sh` 重算哈希。
