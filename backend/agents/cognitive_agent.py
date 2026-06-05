from cognition.reasoning_engine import (
    reasoning_engine
)

from agents.workflow_agent import (
    workflow_agent
)

async def cognitive_agent(
    user_input:str
):

    reasoning = await reasoning_engine(
        user_input
    )

    workflow_input = f"""
User Request:
{user_input}

Deep Cognitive Analysis:
{reasoning}
"""

    return await workflow_agent(
        workflow_input
    )