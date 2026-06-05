from multi_agent.department_performance import (
    get_performance
)


def generate_society_metrics():

    performance = (
        get_performance()
    )

    total_success = 0
    total_failure = 0

    for dept in performance.values():

        total_success += (
            dept.get("success", 0)
        )

        total_failure += (
            dept.get("failure", 0)
        )

    return {

        "total_success":
        total_success,

        "total_failure":
        total_failure,

        "departments":
        performance
    }
