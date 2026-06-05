import os


async def screen_vision_agent(
    task: str
):

    screenshot_dir = (
        "screenshots"
    )

    if not os.path.exists(
        screenshot_dir
    ):

        return """
No screenshots directory found.
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
Detected Screenshots

{chr(10).join(images)}
"""