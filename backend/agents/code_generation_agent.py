from pathlib import Path


async def code_generation_agent(
    task: str
):

    text = task.lower()

    try:

        if "generate fastapi route" in text:

            code = '''
from fastapi import APIRouter

router = APIRouter()

@router.get("/generated")
def generated():

    return {
        "message": "Generated Route"
    }
'''

            filename = (
                "generated_route.py"
            )

            Path(
                filename
            ).write_text(

                code,

                encoding="utf-8"
            )

            return f"""
Generated:

{filename}
"""

        return """
No code generation task detected.
"""

    except Exception as e:

        return str(e)