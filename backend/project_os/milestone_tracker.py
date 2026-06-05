from project_os.project_manager import (
    get_project,
    update_project
)


def add_milestone(
    project: str,
    milestone: str
):

    data = get_project(
        project
    )

    if not data:

        return "Project not found"

    data[
        "milestones"
    ].append({

        "name": milestone,

        "completed": False
    })

    update_project(

        project,

        data
    )

    return "Milestone added"


def complete_milestone(
    project: str,
    milestone: str
):

    data = get_project(
        project
    )

    if not data:

        return "Project not found"

    for item in data[
        "milestones"
    ]:

        if item["name"] == milestone:

            item[
                "completed"
            ] = True

            update_project(

                project,

                data
            )

            return "Milestone completed"

    return "Milestone not found"