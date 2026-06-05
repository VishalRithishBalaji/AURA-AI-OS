from multi_agent.task_claim_engine import (
    claim_department_tasks
)

from multi_agent.task_executor_engine import (
    execute_marketplace_task
)

from multi_agent.task_completion_engine import (
    complete_task
)


async def run_society_cycle():

    departments = [

        "planner",
        "research",
        "deployment",
        "security",
        "memory"
    ]

    report = []

    for department in departments:

        tasks = claim_department_tasks(
            department
        )

        for task in tasks:

            result = await (
                execute_marketplace_task(
                    task
                )
            )

            completion = (
                complete_task(

                    department,

                    result
                )
            )

            report.append(

                f"""
{department}

{result}

{completion}
"""
            )

    return "\n".join(
        report
    )