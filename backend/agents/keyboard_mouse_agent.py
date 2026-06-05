import pyautogui


async def keyboard_mouse_agent(
    task: str
):

    text = task.lower()

    if text.startswith(
        "type "
    ):

        content = task[5:]

        pyautogui.write(

            content,

            interval=0.03
        )

        return f"""
Typed:

{content}
"""

    elif text.startswith(
        "press "
    ):

        key = task.replace(

            "press ",

            ""
        )

        pyautogui.press(
            key
        )

        return f"""
Pressed:

{key}
"""

    return """
Keyboard Mouse Agent

Commands:

- type hello
- press enter
"""