from workspace.workspace_manager import (

    activate_project,

    workspace_status,

    resume_workspace
)

from memory.project_memory import (
    list_projects
)


async def workspace_agent(
    task: str
):

    text = task.lower()

    # =========================
    # ACTIVATE PROJECT
    # =========================

    if text.startswith(
        "activate project"
    ):

        project = (

            task.replace(

                "activate project",

                ""

            ).strip()
        )

        return activate_project(
            project
        )

    # =========================
    # LIST PROJECTS
    # =========================

    elif "workspace projects" in text:

        return {

            "projects":
            list_projects()
        }

    # =========================
    # STATUS
    # =========================

    elif "workspace status" in text:

        return workspace_status()

    # =========================
    # RESUME
    # =========================

    elif "resume workspace" in text:

        return resume_workspace()

    return """
Workspace Agent

Commands:

activate project <name>

workspace projects

workspace status

resume workspace
"""