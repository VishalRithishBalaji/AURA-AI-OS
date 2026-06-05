from multi_agent.shared_memory import (
    get_shared_memory
)


async def shared_memory_agent():

    memories = get_shared_memory()

    if not memories:

        return """
No shared memory available.
"""

    output = "# 🧠 Shared Agent Memory\n\n"

    for memory in memories:

        output += f"""
## AGENT
{memory['agent']}

## EVENT
{memory['content']}

---
"""

    return output