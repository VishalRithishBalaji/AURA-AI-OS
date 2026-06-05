from history.performance_analyzer import (
    analyze_performance
)

from llm.llm_router import ask_llm


async def self_improvement_agent():

    report = analyze_performance()

    prompt = f"""
You are an AI self-improvement system.

Analyze this execution report.

Suggest:
- architecture improvements
- optimization ideas
- reliability improvements
- workflow enhancements

REPORT:
{report}
"""

    suggestions = await ask_llm(prompt)

    return f"""
# 🧠 Self-Improvement Analysis

{report}

---

# 🚀 Suggested Improvements

{suggestions}
"""