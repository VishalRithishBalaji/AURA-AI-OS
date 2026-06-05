scheduled_projects = []


def schedule_project(
    project: str
):

    scheduled_projects.append(
        project
    )

    return {

        "scheduled":
        project
    }


def get_schedule():

    return scheduled_projects