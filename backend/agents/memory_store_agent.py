from memory.project_memory import (
    save_project
)

from memory.workflow_memory import (
    save_workflow
)

from memory.persistent_memory import (
    remember
)


async def memory_store_agent(
    task: str
):

    text = task.lower()

    # =========================
    # SAVE PROJECT
    # =========================

    if text.startswith(
        "remember project"
    ):

        content = task.replace(

            "remember project",

            ""

        ).strip()

        parts = content.split()

        if len(parts) < 2:

            return """
Usage:

remember project <name> <value>
"""

        project_name = parts[0]

        project_data = {

            "description":
            " ".join(
                parts[1:]
            )
        }

        save_project(

            project_name,

            project_data
        )

        return f"""
Project Saved

Name:
{project_name}

Data:
{project_data}
"""

    # =========================
    # SAVE WORKFLOW
    # =========================

    elif text.startswith(
        "remember workflow"
    ):

        content = task.replace(

            "remember workflow",

            ""

        ).strip()

        workflow_name = content

        save_workflow(

            workflow_name,

            [
                "stored"
            ]
        )

        return f"""
Workflow Saved

{workflow_name}
"""

    # =========================
    # GENERIC MEMORY
    # =========================

    elif text.startswith(
        "remember "
    ):

        content = task.replace(

            "remember",

            ""

        ).strip()

        remember(

            content,

            True
        )

        return f"""
Memory Stored

{content}
"""

    return """
Memory Store Agent

Examples:

remember project aura phase12

remember workflow deployment

remember meeting tomorrow
"""