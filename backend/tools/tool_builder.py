from llm.gemini_client import (
    ask_gemini
)

import os
import re


def clean_code(code: str):

    # REMOVE ```python
    code = re.sub(

        r"```python",

        "",

        code
    )

    # REMOVE ```
    code = re.sub(

        r"```",

        "",

        code
    )

    return code.strip()


async def create_tool(task: str):

    prompt = f"""
Generate clean Python code for:

{task}

Return ONLY executable Python code.
"""

    code = await ask_gemini(prompt)

    # CLEAN MARKDOWN
    code = clean_code(code)

    # CREATE DIRECTORY
    os.makedirs(

        "generated_tools",

        exist_ok=True
    )

    filepath = (
        "generated_tools/generated_tool.py"
    )

    # SAVE FILE
    with open(

        filepath,

        "w",

        encoding="utf-8"

    ) as f:

        f.write(code)

    return f"""
# 🛠 Tool Generated

Saved to:
{filepath}

```python
{code}
"""