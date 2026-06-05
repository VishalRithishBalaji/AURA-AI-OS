def generate_improvement(
    failure: dict
):

    category = failure.get(
        "category",
        "general"
    )

    if category == "deployment":

        return (
            "Use deployment executor "
            "instead of general executor"
        )

    elif category == "security":

        return (
            "Increase security audit "
            "coverage"
        )

    elif category == "monitoring":

        return (
            "Create monitoring agent "
            "for monitoring tasks"
        )

    return (
        "Improve routing and "
        "task classification"
    )