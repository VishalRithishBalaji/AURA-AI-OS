import psutil


PROTECTED_PROCESSES = [

    "system",

    "explorer.exe",

    "ollama.exe",

    "python.exe"
]


async def process_control_agent(
    task: str
):

    text = task.lower()

    # =========================
    # LIST TOP PROCESSES
    # =========================

    if "top processes" in text:

        processes = []

        for proc in psutil.process_iter(

            ["pid", "name"]

        ):

            try:

                processes.append({

                    "pid":
                    proc.info["pid"],

                    "name":
                    proc.info["name"]
                })

            except Exception:

                pass

        return processes[:20]

    # =========================
    # KILL PROCESS
    # =========================

    if "kill process" in text:

        target = (

            text.replace(
                "kill process",
                ""
            )

            .strip()
        )

        for proc in psutil.process_iter(

            ["pid", "name"]

        ):

            try:

                name = str(

                    proc.info["name"]

                ).lower()

                if target == name:

                    if name in PROTECTED_PROCESSES:

                        return f"""
Protected Process

{name}
cannot be terminated.
"""

                    proc.kill()

                    return f"""
Process Terminated

{name}
"""

            except Exception:

                pass

        return f"""
Process Not Found

{target}
"""

    return """
Process Control Agent

Commands:

- top processes
- kill process <name>
"""