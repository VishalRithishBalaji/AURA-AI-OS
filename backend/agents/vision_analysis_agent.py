import os

from llm.vision_client import (
    ask_vision
)


async def vision_analysis_agent(
    task: str
):

    screenshot_dir = "screenshots"

    if not os.path.exists(
        screenshot_dir
    ):
        return "No screenshots folder found."

    screenshots = [

        f

        for f in os.listdir(
            screenshot_dir
        )

        if f.lower().endswith(
            (
                ".png",
                ".jpg",
                ".jpeg"
            )
        )
    ]

    if not screenshots:

        return "No screenshots found."

    screenshots.sort()

    latest = screenshots[-1]

    image_path = os.path.join(

        screenshot_dir,

        latest
    )

    prompt = """
Analyze this desktop screenshot.

Provide:

1. Visible application
2. Visible buttons
3. Menus
4. Text shown
5. Recommended next actions
"""

    try:

        result = await ask_vision(

            image_path,

            prompt
        )

        return f"""
Vision Analysis

Image:
{latest}

{result}
"""

    except Exception as e:

        return f"""
Vision Analysis Error

{str(e)}
"""