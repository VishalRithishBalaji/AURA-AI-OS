from multi_agent.autonomous_goal_engine import (
    generate_subgoals
)

from multi_agent.autonomous_task_creator import (
    create_tasks_from_goal
)

from multi_agent.workforce_manager import (
    deploy_workforce
)


def execute_goal(
    objective: str
):

    goals = generate_subgoals(
        objective
    )

    workforce_tasks = []

    for goal in goals:

        tasks = create_tasks_from_goal(
            goal
        )

        workforce_tasks.extend(
            tasks
        )

    deployed = deploy_workforce(
        workforce_tasks
    )

    return {

        "goals": goals,

        "tasks": workforce_tasks,

        "workforce": deployed
    }