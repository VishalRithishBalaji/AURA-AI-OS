from project_os.project_manager import (
    get_project,
    update_project
)


def execute_milestones(
    project_name: str
):

    project = get_project(
        project_name
    )

    if not project:

        return []

    results = []

    for milestone in project.get(
        "milestones",
        []
    ):

        milestone[
            "completed"
        ] = True

        results.append({

            "milestone":
            milestone["name"],

            "status":
            "completed"
        })

    # Persist changes

    update_project(

        project_name,

        project
    )

    return results