from llm.llm_router import ask_llm


async def reflection_agent(
    content: str
):

    prompt = f"""
You are an AI reflection system.

Analyze the workflow results.

RULES:
- Keep response concise
- Maximum 5 improvement points
- Focus on:
  - reliability
  - performance
  - architecture
  - failures
  - optimization
- Avoid long explanations
- Avoid repeating workflow content
- Return clean markdown

CONTENT:
{content}
"""

    return await ask_llm(prompt)