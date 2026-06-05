from multi_agent.strategic_memory import (
    get_strategy_history
)


def choose_next_goal():

    history = (
        get_strategy_history()
    )

    if not history:

        return "optimize planning"

    last_goal = history[-1][
        "goal"
    ]

    if "planning" in last_goal:

        return "improve deployment"

    elif "deployment" in last_goal:

        return "improve security"

    elif "security" in last_goal:

        return "expand research"

    return "optimize planning"