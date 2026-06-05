import os


async def security_agent(
    objective: str
):

    findings = []

    for root, dirs, files in os.walk("."):

        for file in files:

            if file.endswith(".env"):

                findings.append(

                    f"Sensitive file: {file}"
                )

    if not findings:

        findings.append(
            "No obvious security risks found."
        )

    return "\n".join(
        findings
    )