CURRENT_SYSTEM_PROMPT = """
You are AURA AI.

You are:
- intelligent
- calm
- technically accurate
- concise
- helpful
"""


PROMPT_IMPROVEMENTS = []


def evolve_prompt(
    improvement: str
):

    global CURRENT_SYSTEM_PROMPT

    PROMPT_IMPROVEMENTS.append(
        improvement
    )

    CURRENT_SYSTEM_PROMPT += f"""

# Improvement
{improvement}
"""


def get_evolved_prompt():

    return CURRENT_SYSTEM_PROMPT