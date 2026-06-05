from multi_agent.task_marketplace import (
    claim_tasks
)


def claim_department_tasks(
    department: str
):

    claimed = claim_tasks(
        department
    )

    return claimed