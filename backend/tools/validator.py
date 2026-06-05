BLOCKED_COMMANDS = [

    "del",
    "format",
    "shutdown",
    "rd /s",
    "taskkill",
]


def validate_command(
    command: str
):

    command = command.lower()

    for blocked in BLOCKED_COMMANDS:

        if blocked in command:

            return False

    return True