from agents.desktop_manager_agent import (
    desktop_manager_agent
)


async def desktop_control_agent(
    task: str
):

    return await (
        desktop_manager_agent(
            task
        )
    )