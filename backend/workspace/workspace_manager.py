from workspace.project_context import (
    save_project_context,
    load_project_context
)

from workspace.workspace_state import (
    set_workspace_state,
    get_workspace_state
)

from workspace.task_resume_engine import (
    resume_last_task
)


def activate_project(
    project_name: str
):

    set_workspace_state(

        "active_project",

        project_name
    )

    set_workspace_state(

        "status",

        "active"
    )

    return f"""
Project Activated

{project_name}
"""


def save_context(
    project_name: str,
    context: dict
):

    save_project_context(

        project_name,

        context
    )

    return "Context Saved"


def load_context(
    project_name: str
):

    return load_project_context(
        project_name
    )


def workspace_status():

    return get_workspace_state()


def resume_workspace():

    return resume_last_task()