import os


async def reflection_verification_agent(
    task: str,
    result: str
):

    text = task.lower()

    issues = []

    # =========================
    # DOCKERFILE
    # =========================

    if "dockerfile" in text:

        if not os.path.exists(
            "Dockerfile"
        ):

            issues.append(
                "Dockerfile not found"
            )

    # =========================
    # FILE CREATION
    # =========================

    if "create file" in text:

        if "error" in result.lower():

            issues.append(
                "File creation failed"
            )

    # =========================
    # RESULT
    # =========================

    if issues:

        return f"""
Verification Failed

Issues:
{chr(10).join(issues)}
"""

    return """
Verification Passed
"""