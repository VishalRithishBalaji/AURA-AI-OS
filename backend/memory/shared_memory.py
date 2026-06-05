from memory.semantic_search import (
    search_memory
)


def get_shared_memory_context(
    query: str
):

    try:

        memories = search_memory(
            query
        )

        if not memories:

            return ""

        return "\n".join(
            memories
        )

    except Exception as e:

        print(
            f"Shared Memory Error: {e}"
        )

        return ""