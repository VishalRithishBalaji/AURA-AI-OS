def refine_goals(
    completed_goal: str
):

    goal = completed_goal.lower()

    new_goals = []

    if "deployment" in goal:

        new_goals.extend([

            "monitoring",

            "alerting"
        ])

    elif "monitoring" in goal:

        new_goals.append(
            "dashboard"
        )

    elif "security" in goal:

        new_goals.append(
            "compliance"
        )

    return new_goals