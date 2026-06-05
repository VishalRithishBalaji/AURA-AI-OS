from workflows.workflow_learning import (
    get_successful_patterns
)


def optimize_workflow():

    history = (
        get_successful_patterns()
    )

    return f"""
Workflow Optimizer

Known Executions:
{len(history)}
"""