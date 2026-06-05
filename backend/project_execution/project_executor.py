from project_os.project_manager import (
    get_project
)


def execute_project(
    project_name: str
):

    project = get_project(
        project_name
    )

    if not project:

        return {

            "status": "failed",

            "reason": "project not found"
        }

    return {

        "project": project_name,

        "status": "executing",

        "milestones":

        len(
            project[
                "milestones"
            ]
        )
    }