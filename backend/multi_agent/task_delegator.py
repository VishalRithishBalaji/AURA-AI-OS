def delegate_tasks(
    objective: str
):

    objective = objective.lower()

    assignments = []

    assignments.append(
        "planner"
    )

    assignments.append(
        "research"
    )

    if any(word in objective for word in [

        "deploy",
        "deployment",
        "docker",
        "production"

    ]):

        assignments.append(
            "deployment"
        )

    assignments.append(
        "security"
    )

    assignments.append(
        "memory"
    )

    return assignments