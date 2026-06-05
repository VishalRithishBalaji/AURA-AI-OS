from agents.self_repair_agent import (
    self_repair_agent
)


async def recover_task(
    task: str,
    failure_reason: str
):

    repair = await (
        self_repair_agent(

            task,

            failure_reason
        )
    )

    return {

        "task": task,

        "repair": repair
    }