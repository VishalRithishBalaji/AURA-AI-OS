import json
import os


TOOLS_FILE = "runtime/tools.json"


def _ensure_file():

    os.makedirs(
        "runtime",
        exist_ok=True
    )

    if not os.path.exists(
        TOOLS_FILE
    ):

        with open(
            TOOLS_FILE,
            "w"
        ) as f:

            json.dump(
                {},
                f,
                indent=4
            )


def load_tools():

    _ensure_file()

    with open(
        TOOLS_FILE,
        "r"
    ) as f:

        return json.load(f)


def save_tools(
    tools
):

    with open(
        TOOLS_FILE,
        "w"
    ) as f:

        json.dump(
            tools,
            f,
            indent=4
        )


def register_tool(
    name,
    description,
    permissions=None
):

    if permissions is None:

        permissions = []

    tools = load_tools()

    tools[name] = {

        "description":
        description,

        "permissions":
        permissions,

        "enabled":
        True
    }

    save_tools(
        tools
    )


def disable_tool(
    name
):

    tools = load_tools()

    if name in tools:

        tools[name][
            "enabled"
        ] = False

        save_tools(
            tools
        )


def enable_tool(
    name
):

    tools = load_tools()

    if name in tools:

        tools[name][
            "enabled"
        ] = True

        save_tools(
            tools
        )


def get_tool(
    name
):

    return load_tools().get(
        name
    )


def list_tools():

    return load_tools()