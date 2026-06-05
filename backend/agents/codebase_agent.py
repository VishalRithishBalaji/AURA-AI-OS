import os


async def codebase_agent(
    task: str
):

    text = task.lower()

    try:

        results = []

        if "todo" in text:

            search_term = "todo"

        elif "class" in text:

            search_term = "class"

        elif "function" in text:

            search_term = "def "

        else:

            return """
Codebase Agent

Supported:
- find todo
- find class
- find function
"""

        for root, dirs, files in os.walk("."):

            for file in files:

                if not file.endswith(".py"):
                    continue

                path = os.path.join(
                    root,
                    file
                )

                try:

                    with open(
                        path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content = f.read()

                    if search_term in content.lower():

                        results.append(
                            path
                        )

                except:
                    pass

        if not results:

            return "No matches found."

        return "\n".join(
            results[:100]
        )

    except Exception as e:

        return str(e)