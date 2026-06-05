from agents.application_control_agent import (
    application_control_agent
)

from agents.window_focus_agent import (
    window_focus_agent
)

from agents.keyboard_mouse_agent import (
    keyboard_mouse_agent
)


async def desktop_workflow_agent(
    task: str
):

    text = task.lower()

    # =========================
    # VSCODE WORKFLOW
    # =========================

    if "open vscode" in text:

        launch = await (
            application_control_agent(
                "open vscode"
            )
        )

        focus = await (
            window_focus_agent(
                "focus vscode"
            )
        )

        return f"""
WORKFLOW COMPLETE

{launch}

{focus}
"""

    # =========================
    # CHROME WORKFLOW
    # =========================

    elif "open chrome" in text:

        launch = await (
            application_control_agent(
                "open chrome"
            )
        )

        focus = await (
            window_focus_agent(
                "focus chrome"
            )
        )

        return f"""
WORKFLOW COMPLETE

{launch}

{focus}
"""

    # =========================
    # NOTEPAD WORKFLOW
    # =========================

    elif "open notepad" in text:

        launch = await (
            application_control_agent(
                "open notepad"
            )
        )

        focus = await (
            window_focus_agent(
                "focus notepad"
            )
        )

        return f"""
WORKFLOW COMPLETE

{launch}

{focus}
"""

    return """
Desktop Workflow Agent

Examples:

- open vscode
- open chrome
- open notepad
"""