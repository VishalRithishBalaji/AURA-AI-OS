from multi_agent.department_performance import (
    record_performance
)

from multi_agent.society_learning_engine import (
    learn_from_execution
)

from multi_agent.department_reputation import (
    reward_department,
    penalize_department
)


completed_tasks = []


def complete_task(
    department: str,
    execution_result: dict
):

    completed_tasks.append({

        "department": department,

        "result": execution_result
    })

    # =========================
    # SUCCESS DETECTION
    # =========================

    success = True

    if isinstance(
        execution_result,
        dict
    ):

        status = str(

            execution_result.get(
                "status",
                ""
            )

        ).lower()

        result_text = str(

            execution_result.get(
                "result",
                ""
            )

        ).lower()

        if status not in [

            "executed",
            "success",
            "completed"

        ]:

            success = False

        elif (

            "no autonomous execution path"

            in result_text

        ):

            success = False

    else:

        result_text = str(
            execution_result
        ).lower()

        success = (

            "no autonomous execution path"

            not in result_text
        )

    # =========================
    # PERFORMANCE
    # =========================

    record_performance(

        department,

        success
    )

    # =========================
    # REPUTATION
    # =========================

    if success:

        reward_department(
            department
        )

    else:

        penalize_department(
            department
        )

    # =========================
    # LEARNING
    # =========================

    if isinstance(
        execution_result,
        dict
    ):

        learn_from_execution(

            execution_result.get(
                "task",
                ""
            ),

            execution_result.get(
                "result",
                ""
            ),

            success
        )

    else:

        learn_from_execution(

            "unknown",

            str(
                execution_result
            ),

            success
        )

    # =========================
    # REPORT
    # =========================

    return f"""
Task Completed

Department:
{department}

Success:
{success}
"""


def get_completed_tasks():

    return completed_tasks
