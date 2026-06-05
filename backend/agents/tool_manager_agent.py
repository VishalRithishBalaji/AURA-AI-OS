from runtime.plugin_loader import (
    load_plugin
)

from runtime.tool_registry import (
    list_tools
)


async def tool_manager_agent(
    task: str
):

    text = task.lower()

    # =========================
    # GITHUB PLUGIN
    # =========================

    if any(keyword in text for keyword in [

        "clone repository",
        "github repository",
        "github actions",
        "github workflow",
        "github pipeline",
        "create github workflow"

    ]):

        plugin = load_plugin(
            "github_plugin"
        )

    # =========================
    # DOCKER PLUGIN
    # =========================

    elif any(keyword in text for keyword in [

        "docker",
        "docker image",
        "dockerfile",
        "container",
        "containerize",
        "docker deployment"

    ]):

        plugin = load_plugin(
            "docker_plugin"
        )

    # =========================
    # BROWSER PLUGIN
    # =========================

    elif any(keyword in text for keyword in [

        "browser automation",
        "automated browsing",
        "browser plugin"

    ]):

        plugin = load_plugin(
            "browser_plugin"
        )

    # =========================
    # TOOL LISTING
    # =========================

    elif any(keyword in text for keyword in [

        "list tools",
        "show tools",
        "available tools"

    ]):

        tools = list_tools()

        return "\n".join(tools)

    else:

        return """
No suitable plugin found.

Available plugins:
- github_plugin
- docker_plugin
- browser_plugin
"""

    return plugin.run(task)