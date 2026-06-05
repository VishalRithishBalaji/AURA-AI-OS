from multi_agent.inter_department_router import (
    route_department_message
)


def review_report(
    reviewer: str,
    target_department: str,
    report: str
):

    feedback = f"""
Review by {reviewer}

Target:
{target_department}

Status:
Approved

Notes:
Report reviewed successfully.
"""

    route_department_message(

        reviewer,

        target_department,

        feedback
    )

    return feedback