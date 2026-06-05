from project_execution.project_executor import (
    execute_project
)

from project_execution.milestone_executor import (
    execute_milestones
)

from project_execution.project_health import (
    project_health
)

from project_execution.roadmap_generator import (
    generate_roadmap
)


async def project_execution_agent(
    task: str
):

    text = task.lower()

    # =========================
    # EXECUTE PROJECT
    # =========================

    if text.startswith(
        "execute project"
    ):

        project = (

            task.replace(

                "execute project",

                ""

            ).strip()
        )

        return execute_project(
            project
        )

    # =========================
    # EXECUTE MILESTONES
    # =========================

    elif text.startswith(
        "execute milestones"
    ):

        project = (

            task.replace(

                "execute milestones",

                ""

            ).strip()
        )

        return execute_milestones(
            project
        )

    # =========================
    # HEALTH
    # =========================

    elif text.startswith(
        "project health"
    ):

        project = (

            task.replace(

                "project health",

                ""

            ).strip()
        )

        return project_health(
            project
        )

    # =========================
    # ROADMAP
    # =========================

    elif text.startswith(
        "generate roadmap"
    ):

        project = (

            task.replace(

                "generate roadmap",

                ""

            ).strip()
        )

        return generate_roadmap(
            project
        )

    return """
Project Execution Agent

Commands:

execute project <name>

execute milestones <name>

project health <name>

generate roadmap <name>
"""