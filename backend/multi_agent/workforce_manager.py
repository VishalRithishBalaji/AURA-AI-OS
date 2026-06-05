from multi_agent.task_marketplace import (
    create_task
)


def deploy_workforce(
    tasks: list
):

    created = []

    seen = set()

    for task in tasks:

        try:

            department = task.get(
                "department"
            )

            task_name = task.get(
                "task"
            )

            if (

                not department

                or

                not task_name

            ):

                continue

            task_key = (
                department,
                task_name
            )

            # =========================
            # DUPLICATE PROTECTION
            # =========================

            if task_key in seen:

                continue

            seen.add(
                task_key
            )

            item = create_task(

                department,

                task_name
            )

            created.append(
                item
            )

        except Exception as e:

            created.append({

                "department":
                task.get(
                    "department",
                    "unknown"
                ),

                "task":
                task.get(
                    "task",
                    "unknown"
                ),

                "status":
                f"error: {e}"
            })

    return created