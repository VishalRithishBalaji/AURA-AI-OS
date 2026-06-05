from tools.tool_executor import (

    execute_python,
    execute_terminal

)

from tools.validator import (
    validate_command
)


def execution_agent(
    task: str
):

    text = task.lower()

    # PYTHON EXECUTION
    if "run python" in text:

        code = task.replace(
            "run python",
            ""
        )

        return execute_python(
            code
        )

    # TERMINAL EXECUTION
    elif "run terminal" in text:

        command = task.replace(
            "run terminal",
            ""
        )

        # SAFETY CHECK
        if not validate_command(
            command
        ):

            return """
❌ Unsafe terminal command blocked.
"""

        return execute_terminal(
            command
        )

    return """
❌ No executable task detected.
"""