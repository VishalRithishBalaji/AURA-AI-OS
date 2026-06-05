def translate_goal(
    goal: str
):

    goal = goal.lower()

    tasks = []

    if goal == "planning":

        tasks.extend([

            {
                "department": "planner",
                "task": "analyze planning workflow"
            },

            {
                "department": "planner",
                "task": "optimize task delegation"
            }
        ])

    elif goal == "memory":

        tasks.extend([

            {
                "department": "memory",
                "task": "analyze memory usage"
            },

            {
                "department": "memory",
                "task": "improve memory retention"
            }
        ])

    elif goal == "research":

        tasks.extend([

            {
                "department": "research",
                "task": "generate research report"
            }
        ])

    return tasks