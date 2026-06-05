from multi_agent.task_generation_engine import (
    generate_tasks
)

from multi_agent.workforce_manager import (
    deploy_workforce
)

from multi_agent.society_scheduler import (
    run_society_cycle
)

from multi_agent.society_metrics import (
    generate_society_metrics
)


async def autonomous_society_loop(
    objective: str
):

    generated_tasks = (
        generate_tasks(
            objective
        )
    )

    workforce = (
        deploy_workforce(
            generated_tasks
        )
    )

    execution_report = await (
        run_society_cycle()
    )

    metrics = (
        generate_society_metrics()
    )

    return f"""
AUTONOMOUS SOCIETY REPORT

OBJECTIVE:
{objective}

GENERATED TASKS:
{generated_tasks}

WORKFORCE:
{workforce}

EXECUTION:
{execution_report}

METRICS:
{metrics}
"""