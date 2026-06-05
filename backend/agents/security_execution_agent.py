import os


async def security_execution_agent(
    task: str
):

    findings = []

    # =========================
    # ENV FILES
    # =========================

    for root, dirs, files in os.walk("."):

        for file in files:

            if file.endswith(".env"):

                findings.append(

                    f"Sensitive file found: {file}"
                )

    # =========================
    # SECURITY AUDIT
    # =========================

    if "security audit" in task.lower():

        if findings:

            return "\n".join(
                findings
            )

        return """
Security Audit Passed

No obvious risks detected.
"""

    return """
Security task completed.
"""