def executive_decision(
    objective: str,
    reports: dict
):

    summary = []

    summary.append(

        f"""
EXECUTIVE DECISION

Objective:
{objective}
"""
    )

    summary.append(

        "\nDepartments Consulted:\n"
    )

    for department in reports:

        summary.append(
            f"- {department}"
        )

    summary.append(

        """
Final Decision:

Proceed with implementation.
Monitor execution.
Apply security controls.
Store all decisions.
"""
    )

    return "\n".join(
        summary
    )