from agents.autonomous_executor import (
    autonomous_executor
)

from agents.reflection_verification_agent import (
    reflection_verification_agent
)

from agents.self_repair_agent import (
    self_repair_agent
)

from workflows.task_logger import (
    log_task
)

from multi_agent.agent_bus import (
    publish_event
)


async def workflow_execution_agent(
    workflow_name: str,
    tasks: list
):

    results = []

    for task in tasks:

        publish_event(

            "WorkflowExecutionAgent",

            f"Executing: {task}"
        )

        # =========================
        # EXECUTE
        # =========================

        result = await autonomous_executor(
            task
        )

        # =========================
        # VERIFY
        # =========================

        verification = await (
            reflection_verification_agent(

                task,

                str(result)
            )
        )

        repair_result = ""

        reverification = ""

        # =========================
        # REPAIR IF NEEDED
        # =========================

        if "failed" in verification.lower():

            publish_event(

                "WorkflowExecutionAgent",

                f"Repairing: {task}"
            )

            repair_result = await (
                self_repair_agent(

                    task,

                    verification
                )
            )

            # =========================
            # RE-VERIFY
            # =========================

            reverification = await (
                reflection_verification_agent(

                    task,

                    str(repair_result)
                )
            )

        # =========================
        # LOGGING
        # =========================

        log_task(

            workflow_name,

            task,

            str(result)
        )

        # =========================
        # REPORT
        # =========================

        results.append(

            f"""
TASK:
{task}

RESULT:
{result}

VERIFICATION:
{verification}

REPAIR:
{repair_result}

RE-VERIFICATION:
{reverification}
"""
        )

    publish_event(

        "WorkflowExecutionAgent",

        f"Workflow Completed: {workflow_name}"
    )

    return "\n".join(results)