import pygetwindow as gw


async def window_manager_agent(
    task: str
):

    text = task.lower()

    if "list windows" in text:

        windows = [

            w.title

            for w in gw.getAllWindows()

            if w.title
        ]

        return windows[:50]

    if "focus" in text:

        windows = gw.getAllWindows()

        for win in windows:

            try:

                if win.title:

                    win.activate()

                    return f"""
Focused Window

{win.title}
"""

            except Exception:

                pass

        return "No focusable window found."

    return """
Window Manager

Commands:

- list windows
- focus window
"""