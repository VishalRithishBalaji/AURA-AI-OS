from pathlib import Path


async def multi_file_editor_agent(
    task: str
):

    try:

        created_files = []

        if "create api module" in task.lower():

            targets = [

                "api/generated_api.py",
                "tests/test_generated_api.py",
                "docs/generated_api.md"
            ]

            for file in targets:

                path = Path(file)

                path.parent.mkdir(

                    parents=True,

                    exist_ok=True
                )

                path.touch(
                    exist_ok=True
                )

                created_files.append(
                    file
                )

        if not created_files:

            return """
No multi-file operation detected.
"""

        return "\n".join(
            created_files
        )

    except Exception as e:

        return str(e)