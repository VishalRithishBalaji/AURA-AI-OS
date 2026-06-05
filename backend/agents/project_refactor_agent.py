import os


async def project_refactor_agent(
    task: str
):

    suggestions = []

    try:

        for root, dirs, files in os.walk("."):

            py_files = [

                f

                for f in files

                if f.endswith(".py")
            ]

            if len(py_files) > 15:

                suggestions.append(

                    f"Large folder detected: {root}"
                )

        if not suggestions:

            return """
No major refactoring opportunities detected.
"""

        return "\n".join(
            suggestions
        )

    except Exception as e:

        return str(e)