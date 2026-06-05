
from llm.llm_router import ask_llm


async def reasoning_engine(
    task: str
):

    prompt = f"""
You are an advanced reasoning engine.

TASK:
{task}

Perform:
- deep analysis
- step-by-step reasoning
- architectural thinking
- bottleneck detection
- scalability analysis

Be concise and technical.
"""

    return await ask_llm(
        prompt
    )
