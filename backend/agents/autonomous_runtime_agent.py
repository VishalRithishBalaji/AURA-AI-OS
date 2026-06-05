from autonomous_runtime.autonomous_loop import (
    run_autonomous_cycle
)

from autonomous_runtime.runtime_governor import (

    start_runtime,

    stop_runtime,

    get_runtime_state
)

from autonomous_runtime.goal_scheduler import (
    get_scheduled_goals
)


async def autonomous_runtime_agent(
    task: str
):

    text = task.lower()

    # =========================
    # START
    # =========================

    if text == "start runtime":

        return start_runtime()

    # =========================
    # STOP
    # =========================

    elif text == "stop runtime":

        return stop_runtime()

    # =========================
    # STATUS
    # =========================

    elif text == "runtime status":

        return get_runtime_state()

    # =========================
    # RUN CYCLE
    # =========================

    elif text == "run cycle":

        return await (
            run_autonomous_cycle()
        )

    # =========================
    # GOALS
    # =========================

    elif text == "scheduled goals":

        return get_scheduled_goals()

    return """
Autonomous Runtime Agent

Commands:

start runtime

stop runtime

runtime status

run cycle

scheduled goals
"""