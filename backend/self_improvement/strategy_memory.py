from memory.persistent_memory import (
    remember,
    recall
)


STRATEGY_KEY = "improvement_strategies"


def save_strategy(
    task_type: str,
    strategy: str
):

    strategies = recall(
        STRATEGY_KEY
    ) or {}

    if task_type not in strategies:

        strategies[
            task_type
        ] = []

    strategies[
        task_type
    ].append(
        strategy
    )

    remember(

        STRATEGY_KEY,

        strategies
    )

    return strategy


def get_strategies(
    task_type: str
):

    strategies = recall(
        STRATEGY_KEY
    ) or {}

    return strategies.get(
        task_type,
        []
    )


def get_all_strategies():

    return recall(
        STRATEGY_KEY
    ) or {}