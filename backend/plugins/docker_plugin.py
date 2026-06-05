PLUGIN_NAME = "Docker Plugin"

PLUGIN_DESCRIPTION = (
    "Provides Docker container operations"
)


def run(task: str):

    return f"""
Docker Plugin Executed

Task:
{task}
"""