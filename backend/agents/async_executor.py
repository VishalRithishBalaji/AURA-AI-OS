import asyncio

from agents.autonomous_executor import (
    autonomous_executor
)

from history.execution_history import (
    save_execution_history
)


MAX_RETRIES = 2


async def execute_task(
    task: str
):

    for attempt in range(
        MAX_RETRIES
    ):

        try:

            print(
                f"\n⚙️ Executing: {task}"
            )

            # 🚀 Phase 8 Upgrade
            result = await autonomous_executor(
                task
            )

            # SAFETY
            if not isinstance(
                result,
                str
            ):

                result = str(result)

            # DETECT FAILED OUTPUT
            if any(
                keyword in result.lower()

                for keyword in [

                    "unexpected issue",
                    "try again later",
                    "quota",
                    "503",
                    "429",
                    "task failed"
                ]
            ):

                raise Exception(
                    "Execution failure"
                )

            save_execution_history(

                task=task,

                result=result,

                success=True
            )

            return f"""
## TASK
{task}

## RESULT
{result}
"""

        except Exception as e:

            print(
                f"\n⚠️ Task Retry {attempt + 1}"
            )

            print(str(e))

            await asyncio.sleep(

                2 * (attempt + 1)
            )

    # FINAL FAILURE

    error_message = (
        "Task failed after retries."
    )

    save_execution_history(

        task=task,

        result=error_message,

        success=False
    )

    return f"""
## TASK
{task}

## ERROR
{error_message}
"""
