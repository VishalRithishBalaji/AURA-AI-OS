from agents.workflow_execution_agent import (
    workflow_execution_agent
)


async def dynamic_workflow_agent(
    goal: str
):

    text = goal.lower()

    workflow = []

    if "deployment" in text:

        workflow = [

            "analyze project",
            "find function",
            "create Dockerfile",
            "verify deployment structure"
        ]

    elif "refactor" in text:

        workflow = [

            "analyze project",
            "find function",
            "refactor project"
        ]

    elif "testing" in text:

        workflow = [

            "find function",
            "run tests"
        ]

    else:

        workflow = [

            "analyze project"
        ]

    return await workflow_execution_agent(

        "dynamic",

        workflow
    )