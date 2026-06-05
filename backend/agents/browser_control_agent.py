from agents.browser_agent import (
    browser_agent
)


async def browser_control_agent(
    task: str
):

    return await browser_agent(
        task
    )