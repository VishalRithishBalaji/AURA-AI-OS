from self_improvement.agent_optimizer import (
    optimize_agents
)

from self_improvement.strategy_memory import (

    get_all_strategies,

    get_strategies
)


async def meta_learning_agent(
    task: str
):

    text = task.lower()

    # =========================
    # RUN EVOLUTION
    # =========================

    if text in [

        "optimize agents",

        "run evolution",

        "meta learning"

    ]:

        improvements = (
            optimize_agents()
        )

        return {

            "status":
            "completed",

            "improvements":
            improvements
        }

    # =========================
    # ALL STRATEGIES
    # =========================

    elif text == "improvement strategies":

        return {

            "strategies":

            get_all_strategies()
        }

    # =========================
    # CATEGORY STRATEGIES
    # =========================

    elif text.startswith(
        "strategies "
    ):

        category = (

            text.replace(
                "strategies",
                ""
            )

            .strip()
        )

        return {

            "category":
            category,

            "strategies":

            get_strategies(
                category
            )
        }

    return """
Meta Learning Agent

Commands:

optimize agents

run evolution

meta learning

improvement strategies

strategies deployment

strategies security

strategies monitoring
"""