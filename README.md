# 🌊 高摩证券分析师之营销科技增长雷达

本仓库提供一套基于两层架构的 AI Agent 技能组，用于自动化监测全球 MarTech 赛道动态。

## 🛠 体系架构
1. **底层 (Intelligence Layer)**: `martech_signal_intelligence`
   - 职责：抓取原始信息 -> 提取标准化信号 -> 聚合趋势主题。
2. **顶层 (Presentation Layer)**: `martech_growth_radar_brief`
   - 职责：结构化数据 -> 钛动业务翻译 -> 飞书高管简报。

## 🔄 调用顺序
用户输入(URL/文本) ➔ `signal_intelligence` ➔ 结构化 JSON ➔ `growth_radar_brief` ➔ 飞书周报。

## 📋 适用场景
- 每周一例行全网营销情报扫描。
- 竞品动态、融资热点、AI Token 消耗异常监测。
