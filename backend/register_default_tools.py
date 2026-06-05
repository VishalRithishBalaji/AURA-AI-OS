from runtime.tool_registry import (
    register_tool
)


register_tool(

    "browser",

    "Web browsing tool",

    ["network"]
)

register_tool(

    "filesystem",

    "Read and write files",

    ["disk"]
)

register_tool(

    "terminal",

    "Execute terminal commands",

    ["shell"]
)

register_tool(

    "python",

    "Python execution runtime",

    ["compute"]
)

register_tool(

    "github",

    "GitHub integration",

    ["network"]
)

register_tool(

    "docker",

    "Docker integration",

    ["container"]
)

print(
    "✅ Default tools registered"
)