strategic_memory = []


def remember_strategy(
    goal: str,
    outcome: str
):

    strategic_memory.append({

        "goal": goal,

        "outcome": outcome
    })


def get_strategy_history():

    return strategic_memory[-100:]