import pygetwindow as gw


async def application_state_agent():

    windows = []

    for win in gw.getAllWindows():

        try:

            if win.title:

                windows.append({

                    "title": win.title,

                    "active": win.isActive
                })

        except Exception:

            pass

    active_window = None

    for item in windows:

        if item["active"]:

            active_window = item["title"]

            break

    return {

        "active_window": active_window,

        "window_count": len(
            windows
        ),

        "windows": windows[:50]
    }