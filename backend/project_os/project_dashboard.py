from project_os.project_manager import (
    list_projects,
    get_project
)


def project_dashboard():

    dashboard = {}

    for name in list_projects():

        data = get_project(
            name
        )

        if not data:

            continue

        total = len(

            data.get(
                "milestones",
                []
            )

        )

        completed = len([

            m

            for m in data.get(
                "milestones",
                []
            )

            if m.get(
                "completed",
                False
            )

        ])

        dashboard[name] = {

            "status":
            data.get(
                "status",
                "unknown"
            ),

            "milestones":
            total,

            "completed":
            completed
        }

    return dashboard