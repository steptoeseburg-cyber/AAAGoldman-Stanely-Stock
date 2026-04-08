import json

# 1. 定义输出的固定骨架（约束模型不乱飘）
REPORT_TEMPLATE = """
# 🌊 钛动增长雷达 | 周报 {date}

## 🚀 一、高管摘要 (Executive Summary)
{summary_points}

## 📊 二、增长看板 (Growth Leaderboard)
- **Sector**: {top_sector}
- **Top Product**: {top_product}
- **Token Usage**: {token_trend}

## 🔍 三、对标点评 (Competitor Insights)
{competitor_analysis}

## 💡 四、业务行动建议 (Action Plan)
{action_suggestions}
"""

def run(structured_data):
    """
    这是 Skill 的真正入口，负责处理来自 signal_intelligence 的输入
    """
    # A. 基础输入校验 (防御性编程)
    if not structured_data or "signals" not in structured_data:
        return "错误：输入数据格式不正确，缺少 Signals 列表。"
    
    signals = structured_data.get("signals", [])
    topics = structured_data.get("topics", [])
    
    if len(signals) == 0:
        return "提示：过去 7 天未发现显著的 MarTech 信号，无需生成周报。"

    # B. 构造引导 Prompt (带上硬约束)
    execution_prompt = f"""
    你现在是钛动增长简报官。基于以下结构化情报，严格按照 Markdown 模板生成周报。
    
    【输入情报】:
    Signals: {json.dumps(signals, ensure_ascii=False)}
    Topics: {json.dumps(topics, ensure_ascii=False)}
    
    【输出约束】:
    - 摘要不少于 3 条
    - 行动建议必须结合钛动的出海营销业务
    - 禁止编造输入中不存在的数据点
    
    【指定模板】:
    {REPORT_TEMPLATE}
    """
    
    # 这里通常会调用模型接口，并传入 execution_prompt
    return execution_prompt # 实际运行中返回模型生成的 Markdown
