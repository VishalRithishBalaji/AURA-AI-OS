
from llm.llm_router import ask_llm


async def planner_agent(
    task: str
):

    prompt = f"""
You are an AI Planning Agent.

Break the following task into concise executable subtasks.

TASK:
{task}

RULES:
- Return short actionable subtasks
- One task per line
- No explanations
- No markdown
- No numbering
"""

    response = await ask_llm(
        prompt
    )

    tasks = []

    for line in response.split("\n"):

        line = line.strip()

        if line:

            tasks.append(line)

    return tasks
