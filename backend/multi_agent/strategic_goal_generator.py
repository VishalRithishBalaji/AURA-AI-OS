from multi_agent.strategy_engine import (
    choose_strategy
)


def generate_strategic_goal():

    strategy = choose_strategy()

    focus = strategy.get(
        "focus_department",
        "planner"
    )

    mapping = {

        "planner":
        "optimize planning",

        "deployment":
        "improve deployment",

        "security":
        "improve security",

        "research":
        "expand research",

        "memory":
        "improve memory"
    }

    return mapping.get(

        focus,

        "improve society"
    )