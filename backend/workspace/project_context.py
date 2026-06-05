from memory.project_memory import (
    save_project,
    load_project
)


def save_project_context(
    project_name: str,
    context: dict
):

    save_project(

        project_name,

        context
    )


def load_project_context(
    project_name: str
):

    return load_project(
        project_name
    )