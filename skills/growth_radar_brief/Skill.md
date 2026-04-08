# Skill: 钛动营销增长雷达简报 (Briefing Layer)

## 1. 核心定位
本 Skill 负责将结构化的营销情报转化为面向高管的飞书决策简报。它不负责原始数据的搜集，仅负责**业务层面的翻译与行动建议生成**。

## 2. 触发与依赖
- **触发条件**: 在 `martech_signal_intelligence` 输出结构化 JSON 后触发。
- **上游依赖**: 强依赖 `martech_signal_intelligence` 提供的 `signals` 与 `topics` 字段。

## 3. 输入规范 (Input Schema)
Skill 严格接收以下 JSON 结构：
```json
{
  "signals": [{"type": "...", "content": "...", "metric": "..."}],
  "topics": [{"name": "...", "summary": "..."}],
  "entities": ["..."]
}
