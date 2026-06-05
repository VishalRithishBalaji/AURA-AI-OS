import os


async def desktop_agent(
    task: str
):

    text = task.lower()

    try:

        if "open vscode" in text:

            os.system(
                "code"
            )

            return "VS Code launched."

        elif "open chrome" in text:

            os.system(
                "start chrome"
            )

            return "Chrome launched."

        elif "open explorer" in text:

            os.system(
                "explorer ."
            )

            return "Explorer launched."

        return """
Desktop Agent:
No action detected.
"""

    except Exception as e:

        return str(e)