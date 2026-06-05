import os
import webbrowser


async def desktop_automation_agent(
    task: str
):

    text = task.lower()

    try:

        if "open github" in text:

            webbrowser.open(

                "https://github.com"
            )

            return """
GitHub opened.
"""

        elif "open chatgpt" in text:

            webbrowser.open(

                "https://chatgpt.com"
            )

            return """
ChatGPT opened.
"""

        elif "open downloads" in text:

            os.system(
                "explorer shell:Downloads"
            )

            return """
Downloads opened.
"""

        elif "open desktop" in text:

            os.system(
                "explorer shell:Desktop"
            )

            return """
Desktop opened.
"""

        return """
Desktop Automation Agent

No automation task detected.
"""

    except Exception as e:

        return str(e)