from memory.persistent_memory import (
    remember,
    recall
)


WORKFLOW_KEY = "workflows"


def save_workflow(
    name: str,
    steps: list
):

    workflows = recall(
        WORKFLOW_KEY
    ) or {}

    workflows[name] = steps

    remember(

        WORKFLOW_KEY,

        workflows
    )


def load_workflow(
    name: str
):

    workflows = recall(
        WORKFLOW_KEY
    ) or {}

    return workflows.get(
        name
    )


def list_workflows():

    workflows = recall(
        WORKFLOW_KEY
    ) or {}

    return list(
        workflows.keys()
    )