from memory.persistent_memory import (
    get_all_memory
)

from memory.project_memory import (
    list_projects
)

from memory.workflow_memory import (
    list_workflows
)


async def memory_recall_agent(
    task: str
):

    text = task.lower()

    if "all memory" in text:

        return get_all_memory()

    elif "projects" in text:

        return {

            "projects":
            list_projects()
        }

    elif "workflows" in text:

        return {

            "workflows":
            list_workflows()
        }

    return """
Memory Recall Agent

Commands:

- all memory
- projects
- workflows
"""