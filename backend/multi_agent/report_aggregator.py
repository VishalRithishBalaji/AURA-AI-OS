def aggregate_reports(
    reports: dict
):

    output = []

    output.append(

        "\nEXECUTIVE REPORT\n"
    )

    for department, report in reports.items():

        output.append(

            f"""
=========================
{department.upper()}
=========================

{report}
"""
        )

    return "\n".join(
        output
    )