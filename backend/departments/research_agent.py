from llm.llm_router import (
    ask_llm
)


async def research_agent(
    objective: str
):

    prompt = f"""
You are assisting development of AURA AI.

AURA AI is an autonomous AI operating system project.

Do NOT interpret AURA as Salesforce Aura Framework.

Research this objective:

{objective}

Provide:

1. Best practices
2. Risks
3. Recommendations
4. Architecture suggestions
"""

    return await ask_llm(
        prompt
    )