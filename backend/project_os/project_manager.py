from memory.project_memory import (
    save_project,
    load_project,
    list_projects as memory_projects
)


def create_project(
    name: str
):

    existing = load_project(
        name
    )

    if existing:

        return existing

    project = {

        "status": "active",

        "goals": [],

        "milestones": []
    }

    save_project(

        name,

        project
    )

    return project


def get_project(
    name: str
):

    return load_project(
        name
    )


def update_project(
    name: str,
    project_data: dict
):

    save_project(

        name,

        project_data
    )


def list_projects():

    return memory_projects()