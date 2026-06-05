from agents.file_editor_agent import (
    file_editor_agent
)


async def self_repair_agent(
    task: str,
    verification_result: str
):

    text = task.lower()

    # =========================
    # DOCKERFILE REPAIR
    # =========================

    if (

        "dockerfile" in text

        and

        "failed" in verification_result.lower()

    ):

        return await file_editor_agent(
            "create dockerfile"
        )

    # =========================
    # FILE REPAIR
    # =========================

    if (

        "create file" in text

        and

        "failed" in verification_result.lower()

    ):

        return await file_editor_agent(
            task
        )

    return """
No repair strategy available.
"""