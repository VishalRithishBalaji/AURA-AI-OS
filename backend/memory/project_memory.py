from memory.persistent_memory import (
    remember,
    recall
)


PROJECT_KEY = "projects"


def save_project(
    name: str,
    data: dict
):

    projects = recall(
        PROJECT_KEY
    ) or {}

    projects[name] = data

    remember(

        PROJECT_KEY,

        projects
    )


def load_project(
    name: str
):

    projects = recall(
        PROJECT_KEY
    ) or {}

    return projects.get(
        name
    )


def list_projects():

    projects = recall(
        PROJECT_KEY
    ) or {}

    return list(
        projects.keys()
    )