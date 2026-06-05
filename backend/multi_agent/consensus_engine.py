def build_consensus(
    reports: dict
):

    decision = []

    for department, report in reports.items():

        if report:

            decision.append(
                department
            )

    return f"""
Consensus Reached

Participating Departments:

{", ".join(decision)}
"""