from workflows.workflow_engine import (
    get_workflow
)

from agents.workflow_execution_agent import (
    workflow_execution_agent
)


async def autonomous_task_agent(
    task: str
):

    text = task.lower()

    workflow_name = None

    if "docker" in text:

        workflow_name = "docker"

    elif "deploy" in text:

        workflow_name = "deployment"

    elif "test" in text:

        workflow_name = "testing"

    elif "refactor" in text:

        workflow_name = "refactor"

    if not workflow_name:

        return """
No autonomous workflow found.
"""

    workflow = get_workflow(
        workflow_name
    )

    return await workflow_execution_agent(

        workflow_name,

        workflow
    )