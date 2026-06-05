import subprocess


async def task_agent(
    task: str
):

    text = task.lower()

    try:

        if "running processes" in text:

            result = subprocess.run(

                "tasklist",

                capture_output=True,

                text=True,

                shell=True
            )

            return result.stdout[:5000]

        elif "kill uvicorn" in text:

            subprocess.run(

                "taskkill /F /IM python.exe",

                shell=True
            )

            return """
Python processes terminated.
"""

        return """
Task Agent:
No supported operation.
"""

    except Exception as e:

        return str(e)