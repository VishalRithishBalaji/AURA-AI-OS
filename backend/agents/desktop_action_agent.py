import pyautogui
import os


async def desktop_action_agent(
    task: str
):

    text = task.lower()

    os.makedirs(
        "screenshots",
        exist_ok=True
    )

    try:

        if "take screenshot" in text:

            path = (
                "screenshots/current.png"
            )

            pyautogui.screenshot(
                path
            )

            return f"""
Screenshot saved:

{path}
"""

        elif "type text" in text:

            content = task.replace(
                "type text",
                ""
            )

            pyautogui.write(
                content,
                interval=0.05
            )

            return "Text typed."

        elif "press enter" in text:

            pyautogui.press(
                "enter"
            )

            return "Enter pressed."

        elif "ctrl s" in text:

            pyautogui.hotkey(
                "ctrl",
                "s"
            )

            return "Ctrl+S pressed."

        return """
Unknown desktop action.
"""

    except Exception as e:

        return str(e)
    