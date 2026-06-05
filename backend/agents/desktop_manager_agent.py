from agents.application_control_agent import (
    application_control_agent
)

from agents.window_manager_agent import (
    window_manager_agent
)

from agents.keyboard_mouse_agent import (
    keyboard_mouse_agent
)

from agents.application_state_agent import (
    application_state_agent
)

from agents.window_focus_agent import (
    window_focus_agent
)

from agents.desktop_workflow_agent import (
    desktop_workflow_agent
)


async def desktop_manager_agent(
    task: str
):

    text = task.lower()

    # =========================
    # APPLICATION STATE
    # =========================

    if any(word in text for word in [

        "application state",
        "desktop state",
        "active window"

    ]):

        return await (
            application_state_agent()
        )

    # =========================
    # SMART WORKFLOWS
    # =========================

    elif any(word in text for word in [

        "open vscode",
        "open chrome",
        "open notepad"

    ]):

        return await (
            desktop_workflow_agent(
                task
            )
        )

    # =========================
    # WINDOW FOCUS
    # =========================

    elif "focus" in text:

        return await (
            window_focus_agent(
                task
            )
        )

    # =========================
    # WINDOW MANAGEMENT
    # =========================

    elif any(word in text for word in [

        "list windows",
        "window list"

    ]):

        return await (
            window_manager_agent(
                task
            )
        )

    # =========================
    # KEYBOARD & MOUSE
    # =========================

    elif any(word in text for word in [

        "type",
        "click",
        "press"

    ]):

        return await (
            keyboard_mouse_agent(
                task
            )
        )

    # =========================
    # APPLICATION CONTROL
    # =========================

    elif any(word in text for word in [

        "open",
        "launch",
        "start"

    ]):

        return await (
            application_control_agent(
                task
            )
        )

    return """
Desktop Manager

Commands:

- application state
- active window

- open vscode
- open chrome
- open notepad

- focus vscode
- focus chrome
- focus notepad

- list windows

- type hello world
- press enter
"""