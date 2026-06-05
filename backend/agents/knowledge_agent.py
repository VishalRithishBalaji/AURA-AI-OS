from brain.brain_manager import (
    search_knowledge
)


async def knowledge_agent(
    query: str
):

    results = search_knowledge(
        query
    )

    if not results:

        return """
No relevant knowledge found.
"""

    output = "# 🧠 AURA Knowledge Base\n\n"

    for item in results:

        output += f"""
## CATEGORY
{item['category']}

## PROBLEM
{item['problem']}

## SOLUTION
{item['solution']}

---
"""

    return output