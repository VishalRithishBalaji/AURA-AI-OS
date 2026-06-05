from datetime import datetime

runtime_state = {

    "running": False,

    "start_time": None,

    "cycles": 0
}


async def start_runtime():

    runtime_state["running"] = True

    runtime_state["start_time"] = str(
        datetime.now()
    )

    return runtime_state


def stop_runtime():

    runtime_state["running"] = False


def increment_cycle():

    runtime_state["cycles"] += 1


def get_runtime_state():

    return runtime_state