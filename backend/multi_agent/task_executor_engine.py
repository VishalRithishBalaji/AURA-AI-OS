from agents.autonomous_executor import (
    autonomous_executor
)


async def execute_marketplace_task(
    task_data: dict
):

    task = task_data.get(
        "task",
        ""
    )

    result = await (
        autonomous_executor(
            task
        )
    )

    return {

        "task": task,

        "result": str(result),

        "status": "executed"
    }