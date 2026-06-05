import pygetwindow as gw


async def window_focus_agent(
    task: str
):

    text = task.lower()

    target = (

        text
        .replace("focus", "")
        .replace("window", "")
        .strip()

    )

    # =========================
    # COMMON ALIASES
    # =========================

    aliases = {

        "vscode": [
            "visual studio code",
            "code"
        ],

        "code": [
            "visual studio code",
            "code"
        ],

        "chrome": [
            "google chrome",
            "chrome"
        ],

        "notepad": [
            "notepad"
        ]
    }

    search_terms = [target]

    if target in aliases:

        search_terms = aliases[
            target
        ]

    windows = gw.getAllWindows()

    # =========================
    # SPECIFIC WINDOW
    # =========================

    if target:

        matches = []

        for win in windows:

            try:

                title = str(
                    win.title
                ).strip()

                if not title:

                    continue

                title_lower = (
                    title.lower()
                )

                if any(

                    term in title_lower

                    for term in search_terms

                ):

                    matches.append(
                        win
                    )

            except Exception:

                pass

        if matches:

            win = matches[0]

            try:

                if win.isMinimized:

                    win.restore()

            except Exception:

                pass

            try:

                win.activate()

            except Exception:

                pass

            return f"""
Focused Window

{win.title}
"""

        # =========================
        # DEBUG INFO
        # =========================

        available = []

        for win in windows:

            try:

                if win.title:

                    available.append(
                        win.title
                    )

            except Exception:

                pass

        return {

            "error":
            "Window Not Found",

            "target":
            target,

            "search_terms":
            search_terms,

            "available_windows":
            available
        }

    # =========================
    # FIRST VALID WINDOW
    # =========================

    for win in windows:

        try:

            title = str(
                win.title
            ).strip()

            if not title:

                continue

            try:

                if win.isMinimized:

                    win.restore()

            except Exception:

                pass

            try:

                win.activate()

            except Exception:

                pass

            return f"""
Focused Window

{title}
"""

        except Exception:

            pass

    return """
No focusable window found.
"""