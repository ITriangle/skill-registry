# Wiki 运营闭环

## 口令

| 口令 | 行为 | 写文件？ |
|------|------|----------|
| `加入 wiki：…` | Ingest：raw + 编译 + index + log | 是 |
| `关于 X 我知道什么` | Query：只读综合 | 默认否；用户要求归档才写 `queries/` |
| `lint wiki` | `scripts/lint-wiki.sh` + 启发式 | 是（log；自动修索引时改 index） |
| `本周回顾` | 冲突 / 开放问题 / 高频未建页 | 是 |
| `本月回顾` | 工作地图类 synthesis + 覆盖范围 | 是 |

## Inbox

1. `scripts/new-raw.sh <wiki> inbox "标题"` 或手写 `raw/inbox/YYYY-MM-DD-slug.md`
2. 积累到可编译粒度后执行「加入 wiki」
3. 编译完成后移入 `articles|notes|transcripts|git|…`，避免 inbox 与正式 raw 双份真相

## 周回顾检查单

- [ ] `contested: true` 与 `contradictions` 是否仍未解决
- [ ] 覆盖范围 / 开放问题页是否需追加缺口
- [ ] 本周日志里高频出现但无独立页的概念（达阈值再建）
- [ ] inbox 是否清空或降为正式来源
- [ ] 跑一次 `lint wiki`

## 月回顾检查单

- [ ] 更新工作地图 / 时间线类 synthesis
- [ ] 校正各 entity 的开放问题
- [ ] 评估是否有权衡决策值得写入 `comparisons/`
- [ ] 将稳定流程回流 skill 包（模板 / 脚本）

## 页面纪律

- 少而强；顺带事实合并进既有页
- `comparisons/` 仅用于真实权衡
- 约 200 行且混目的时拆分
- 未说明变更集不批量改 10+ 页
