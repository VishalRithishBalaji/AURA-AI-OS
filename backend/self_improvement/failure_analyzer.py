from multi_agent.society_learning_engine import (
    get_failures
)


def analyze_failures():

    failures = get_failures()

    analysis = []

    for item in failures:

        task = item.get(
            "task",
            "unknown"
        )

        result = str(

            item.get(
                "result",
                ""
            )

        ).lower()

        category = "general"

        if "docker" in task.lower():

            category = "deployment"

        elif "security" in task.lower():

            category = "security"

        elif "monitoring" in task.lower():

            category = "monitoring"

        analysis.append({

            "task":
            task,

            "category":
            category,

            "result":
            result
        })

    return analysis