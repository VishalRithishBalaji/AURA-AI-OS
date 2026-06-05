from multi_agent.society_manager import (
    society_manager
)


async def ceo_agent(
    objective: str
):

    return await society_manager(
        objective
    )