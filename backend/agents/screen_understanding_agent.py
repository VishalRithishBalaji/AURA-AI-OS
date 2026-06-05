import os


async def screen_understanding_agent(
    task: str
):

    try:

        screenshot_dir = (
            "screenshots"
        )

        if not os.path.exists(
            screenshot_dir
        ):

            return """
No screenshots folder found.
"""

        images = [

            f

            for f in os.listdir(
                screenshot_dir
            )

            if f.endswith(

                (
                    ".png",
                    ".jpg",
                    ".jpeg"
                )
            )
        ]

        if not images:

            return """
No screenshots found.
"""

        return f"""
Detected screenshots:

{chr(10).join(images)}
"""

    except Exception as e:

        return str(e)