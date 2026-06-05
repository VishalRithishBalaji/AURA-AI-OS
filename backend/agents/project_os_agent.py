from project_os.project_manager import (

    create_project,

    list_projects
)

from project_os.milestone_tracker import (

    add_milestone,

    complete_milestone
)

from project_os.project_dashboard import (
    project_dashboard
)

from project_os.project_scheduler import (

    schedule_project,

    get_schedule
)


async def project_os_agent(
    task: str
):

    text = task.lower()

    # =========================
    # CREATE PROJECT
    # =========================

    if text.startswith(
        "create project"
    ):

        name = (

            task.replace(

                "create project",

                ""

            ).strip()
        )

        return create_project(
            name
        )

    # =========================
    # LIST PROJECTS
    # =========================

    elif text == "list projects":

        return list_projects()

    # =========================
    # ADD MILESTONE
    # =========================

    elif text.startswith(
        "add milestone"
    ):

        parts = task.split(
            "|"
        )

        if len(parts) != 3:

            return """
Usage:

add milestone|project|milestone
"""

        return add_milestone(

            parts[1].strip(),

            parts[2].strip()
        )

    # =========================
    # COMPLETE MILESTONE
    # =========================

    elif text.startswith(
        "complete milestone"
    ):

        parts = task.split(
            "|"
        )

        if len(parts) != 3:

            return """
Usage:

complete milestone|project|milestone
"""

        return complete_milestone(

            parts[1].strip(),

            parts[2].strip()
        )

    # =========================
    # DASHBOARD
    # =========================

    elif text == "project dashboard":

        return project_dashboard()

    # =========================
    # SCHEDULER
    # =========================

    elif text.startswith(
        "schedule project"
    ):

        project = (

            task.replace(

                "schedule project",

                ""

            ).strip()
        )

        return schedule_project(
            project
        )

    elif text == "project schedule":

        return get_schedule()

    return """
Project OS Agent

Commands:

create project <name>

list projects

add milestone|project|milestone

complete milestone|project|milestone

project dashboard

schedule project <name>

project schedule
"""