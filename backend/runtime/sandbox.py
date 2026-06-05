import subprocess


ALLOWED_COMMANDS = [

    "python",
    "pip",
    "git",
    "uvicorn",
    "pytest"
]


BLOCKED_COMMANDS = [

    "shutdown",
    "format",
    "diskpart",
    "del",
    "rm",
    "rmdir",
    "taskkill"
]


def is_safe_command(
    command: str
):

    command = command.lower()

    for blocked in BLOCKED_COMMANDS:

        if blocked in command:

            return False

    return True


def execute_safe_command(
    command: str
):

    if not is_safe_command(
        command
    ):

        return {

            "success":
            False,

            "error":
            "Blocked by sandbox"
        }

    try:

        result = subprocess.run(

            command,

            shell=True,

            capture_output=True,

            text=True
        )

        return {

            "success":
            True,

            "stdout":
            result.stdout,

            "stderr":
            result.stderr
        }

    except Exception as e:

        return {

            "success":
            False,

            "error":
            str(e)
        }