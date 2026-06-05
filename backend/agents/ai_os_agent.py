from multi_agent.ai_os_kernel import (
    boot_ai_os
)

from multi_agent.autonomous_runtime import (
    get_runtime_state
)


async def ai_os_agent(
    task: str
):

    if "status" in task.lower():

        return get_runtime_state()

    return await boot_ai_os()