from multi_agent.strategic_goal_generator import (
    generate_strategic_goal
)


scheduled_goals = []


def schedule_goal():

    goal = generate_strategic_goal()

    scheduled_goals.append(
        goal
    )

    return goal


def get_scheduled_goals():

    return scheduled_goals