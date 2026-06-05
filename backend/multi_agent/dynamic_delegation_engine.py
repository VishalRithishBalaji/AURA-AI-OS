from multi_agent.task_marketplace import (
    create_task
)


def dynamic_delegate(
    department: str,
    objective: str
):

    delegated = []

    objective = objective.lower()

    if "deployment" in objective:

        delegated.append(

            create_task(

                "deployment",

                "Create deployment plan"
            )
        )

    if "security" in objective:

        delegated.append(

            create_task(

                "security",

                "Perform security review"
            )
        )

    if "research" in objective:

        delegated.append(

            create_task(

                "research",

                "Research best practices"
            )
        )

    return delegated