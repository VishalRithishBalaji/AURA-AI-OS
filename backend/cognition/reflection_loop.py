from cognition.cognitive_state import (
    update_reflection
)

from agents.reflection_agent import (
    reflection_agent
)


def run_reflection(
    result: str
):

    reflection = reflection_agent(
        result
    )

    update_reflection(
        reflection
    )

    return reflection