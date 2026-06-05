from cognition.cognitive_state import (

    update_goal,
    update_plan,
    update_status
)

from agents.planner_agent import (
    planner_agent
)


def create_goal(
    user_input: str
):

    update_status(
        "PLANNING"
    )

    update_goal(
        user_input
    )

    plan = planner_agent(
        user_input
    )

    update_plan(
        plan
    )

    return plan