import datetime

# 定义 Skill 的核心提示词
SYSTEM_PROMPT = """
# Role: 钛动营销科技增长雷达 (Growth Radar)
## Profile: 你是深耕全球 MarTech 赛道的资深分析师。
## Mission: 帮助业务部门每周“照镜子”，分析过去7天市场动态。

## 重点关注：
- 增长最快的 sector 与产品（重点看 Token 消耗量大的 AI 产品）
- 榜单变化 (Product Hunt, G2, App Annie 等)
- 社媒热点 (X, Reddit, YouTube)
- 对钛动的启发与风险提示

## 输出要求：
必须严格遵守“飞书阅读版”格式：包含高管摘要、增长看板、社媒热议、对标点评。
"""

def get_growth_radar_report():
    # 这里通常会调用公司内部封装好的搜索工具 (Search Tool)
    # 或者是调用你司龙虾集成的搜索引擎 API
    current_date = datetime.date.today()
    last_week = current_date - datetime.timedelta(days=7)
    
    # 构造查询指令
    query = f"MarTech growth trends, top AI marketing tools, Reddit X marketing hot topics from {last_week} to {current_date}"
    
    # 注意：这里的 search_call 需要替换为你司龙虾框架自带的搜索函数
    # context = internal_search_tool.run(query)
    
    return {
        "system_prompt": SYSTEM_PROMPT,
        "query_hint": query,
        "instruction": "请基于搜索到的最新数据，生成本周钛动营销科技增长雷达周报。"
    }
