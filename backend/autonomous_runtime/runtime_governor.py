runtime_state = {

    "running": False,

    "cycles": 0
}


def start_runtime():

    runtime_state[
        "running"
    ] = True

    return runtime_state


def stop_runtime():

    runtime_state[
        "running"
    ] = False

    return runtime_state


def increment_cycle():

    runtime_state[
        "cycles"
    ] += 1


def get_runtime_state():

    return runtime_state