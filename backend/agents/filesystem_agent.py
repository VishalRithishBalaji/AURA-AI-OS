import os


async def filesystem_agent(
    task: str
):

    text = task.lower()

    try:

        if "list files" in text:

            files = []

            for root, dirs, filenames in os.walk("."):

                for file in filenames:

                    files.append(

                        os.path.join(
                            root,
                            file
                        )
                    )

            return "\n".join(
                files[:200]
            )

        elif "current directory" in text:

            return os.getcwd()

        elif "list folders" in text:

            return "\n".join(

                os.listdir(".")
            )

        return """
Filesystem task not recognized.
"""

    except Exception as e:

        return str(e)