from autonomous_runtime.goal_scheduler import (
    schedule_goal
)

from autonomous_runtime.task_dispatcher import (
    dispatch_goal
)

from autonomous_runtime.runtime_governor import (

    increment_cycle,

    get_runtime_state
)


async def run_autonomous_cycle():

    goal = schedule_goal()

    result = dispatch_goal(
        goal
    )

    increment_cycle()

    return {

        "goal":
        goal,

        "result":
        result,

        "runtime":
        get_runtime_state()
    }