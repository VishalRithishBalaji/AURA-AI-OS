from multi_agent.autonomous_goal_engine import (
    generate_subgoals
)

from multi_agent.autonomous_task_creator import (
    create_tasks_from_goal
)


goals = generate_subgoals(
    "production deployment"
)

print("\nGOALS")
print(goals)

for goal in goals:

    tasks = create_tasks_from_goal(
        goal
    )

    print("\nTASKS")
    print(tasks)