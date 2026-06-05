from llm.llm_router import ask_llm


async def summarize_memory(text: str):

    try:

        prompt = f"""
Summarize the following memory into a concise,
long-term useful knowledge statement.

RULES:
- Keep important information
- Remove unnecessary details
- Keep it short
- Keep technical context
- Write in one concise paragraph

MEMORY:
{text}
"""

        summary = await ask_llm(prompt)

        return summary.strip()

    except Exception as e:

        print(
            f"Memory Summarization Error: {e}"
        )

        return text