from project_os.project_manager import (
    get_project
)


def project_health(
    project_name: str
):

    project = get_project(
        project_name
    )

    if not project:

        return {

            "health":
            "unknown"
        }

    milestones = project.get(
        "milestones",
        []
    )

    total = len(
        milestones
    )

    completed = len([

        m

        for m in milestones

        if m.get(
            "completed",
            False
        )

    ])

    progress = 0.0

    if total > 0:

        progress = round(

            (
                completed
                /
                total
            )
            * 100,

            2
        )

    if progress >= 100:

        health = "excellent"

    elif progress >= 50:

        health = "good"

    else:

        health = "needs attention"

    return {

        "project":
        project_name,

        "total_milestones":
        total,

        "completed_milestones":
        completed,

        "progress":
        progress,

        "health":
        health
    }