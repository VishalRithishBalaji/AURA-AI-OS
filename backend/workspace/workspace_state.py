workspace_state = {

    "active_project": None,

    "last_task": None,

    "status": "idle"
}


def set_workspace_state(
    key: str,
    value
):

    workspace_state[
        key
    ] = value


def get_workspace_state():

    return workspace_state