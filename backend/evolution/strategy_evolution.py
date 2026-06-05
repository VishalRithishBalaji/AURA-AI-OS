STRATEGIES = {

    "workflow_execution":

        {

            "parallel_execution":
                True,

            "max_tasks":
                3,

            "reflection":
                True
        }
}


def improve_strategy():

    strategy = STRATEGIES[
        "workflow_execution"
    ]

    # SIMPLE EVOLUTION RULES
    if strategy[
        "max_tasks"
    ] < 5:

        strategy[
            "max_tasks"
        ] += 1

    return strategy