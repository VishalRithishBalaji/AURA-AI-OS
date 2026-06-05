from memory.shared_memory import (
    get_shared_memory_context
)


async def memory_agent(
    objective: str
):

    try:

        context = (
            get_shared_memory_context(
                objective
            )
        )

        return f"""
Memory Context

{context}
"""

    except Exception as e:

        return f"""
Memory Error

{str(e)}
"""