from workspace.workspace_state import (
    get_workspace_state
)


def resume_last_task():

    state = (
        get_workspace_state()
    )

    return {

        "project":
        state.get(
            "active_project"
        ),

        "last_task":
        state.get(
            "last_task"
        ),

        "status":
        state.get(
            "status"
        )
    }