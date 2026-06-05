from multi_agent.shared_memory import (
    search_shared_memory
)


def get_collaboration_context(
    task: str
):

    memories = search_shared_memory(
        task
    )

    if not memories:

        return ""

    context = "\n".join([

        f"{m['agent']}: {m['content']}"

        for m in memories

    ])

    return context