import os
import subprocess


async def application_control_agent(
    task: str
):

    text = task.lower()

    try:

        # =========================
        # NOTEPAD
        # =========================

        if "notepad" in text:

            subprocess.Popen(
                ["notepad.exe"]
            )

            return "Notepad launched."

        # =========================
        # CHROME
        # =========================

        elif "chrome" in text:

            chrome_paths = [

                r"C:\Program Files\Google\Chrome\Application\chrome.exe",

                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            ]

            for path in chrome_paths:

                if os.path.exists(path):

                    subprocess.Popen([path])

                    return "Chrome launched."

            return "Chrome executable not found."

        # =========================
        # VS CODE
        # =========================

        elif "vscode" in text or "visual studio code" in text:

            vscode_paths = [

                r"C:\Users\Vishal\AppData\Local\Programs\Microsoft VS Code\Code.exe",

                r"C:\Program Files\Microsoft VS Code\Code.exe",

                r"C:\Program Files (x86)\Microsoft VS Code\Code.exe"
            ]

            for path in vscode_paths:

                if os.path.exists(path):

                    subprocess.Popen([path])

                    return "VS Code launched."

            return "VS Code executable not found."

        return "Application not recognized."

    except Exception as e:

        return f"""
Application Launch Error

{e}
"""