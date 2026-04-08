import datetime

# 1. 这里合成了你图1的所有核心需求（灵魂）
SYSTEM_PROMPT = """
# Skill: 钛动营销科技增长雷达 (Growth Radar)

## 定位
你现在是钛动营销科技 (Tec-do) 的资深增长分析师。你的任务是每周执行一次全球 MarTech 赛道扫描，为业务部门“照镜子”。

## 核心扫描维度 (图1需求)
- **增长最快 Sector**: 识别本周哪个细分领域增势最猛。
- **榜单变化**: 监测 Product Hunt, G2, App Annie 的排名波动。
- **社媒热点**: 总结 Reddit/X/YouTube 上的讨论热点。
- **Token 消耗王**: 识别增长最快且 API 调用活跃的 AI 营销产品。
- **钛动关联**: 产出对钛动的启发与风险提示。

## 输出规范 (飞书直接阅读版)
必须包含：【高管摘要】+【增长看板】+【社媒热议】+【对标点评与建议】。
"""

def get_growth_radar_report():
    # 2. 这里的逻辑确保龙虾知道看“过去7天”
    current_date = datetime.date.today()
    last_week = current_date - datetime.timedelta(days=7)
    
    # 构造更精准的搜索指令
    query = f"MarTech sector trends, high growth AI marketing tools, Product Hunt weekly top, Token usage trends marketing AI from {last_week} to {current_date}"
    
    return {
        "system_prompt": SYSTEM_PROMPT,
        "query_hint": query,
        "instruction": "请基于搜索到的最新数据，生成一份针对钛动业务的高质量周报。"
    }
