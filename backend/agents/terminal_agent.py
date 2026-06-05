from runtime.sandbox import (
    execute_safe_command
)


async def terminal_agent(
    task: str
):

    command = task.strip()

    result = execute_safe_command(
        command
    )

    if result["success"]:

        return f"""
# Terminal Output

{result["stdout"]}
"""

    return f"""
# Terminal Error

{result.get("error")}
"""