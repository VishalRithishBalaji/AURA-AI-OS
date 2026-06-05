from multi_agent.society_learning_engine import (
    get_failures,
    learning_summary
)


def evolve_society():

    failures = get_failures()

    improvements = []

    for failure in failures:

        task = failure.get(
            "task",
            "unknown"
        )

        # =========================
        # TASK-SPECIFIC IMPROVEMENTS
        # =========================

        if "dockerfile" in task.lower():

            improvements.append(

                f"""
Improve Docker Workflow:

{task}
"""
            )

        elif "monitoring" in task.lower():

            improvements.append(

                f"""
Improve Monitoring System:

{task}
"""
            )

        elif "security" in task.lower():

            improvements.append(

                f"""
Improve Security Agent:

{task}
"""
            )

        elif "documentation" in task.lower():

            improvements.append(

                f"""
Improve Documentation Generator:

{task}
"""
            )

        else:

            improvements.append(

                f"""
Improve Task:

{task}
"""
            )

    summary = learning_summary()

    return {

        "total_executions":
        summary["total"],

        "successes":
        summary["successes"],

        "failures":
        summary["failures"],

        "improvements":
        improvements
    }
