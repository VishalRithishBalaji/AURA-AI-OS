learning_history = []


def learn_from_execution(
    task: str,
    result: str,
    success: bool
):

    learning_history.append({

        "task": task,

        "result": result,

        "success": success
    })

    # Keep memory bounded

    if len(
        learning_history
    ) > 1000:

        learning_history.pop(0)


def get_learnings():

    return learning_history[-100:]


def get_failures():

    return [

        item

        for item in learning_history

        if item.get(
            "success",
            False
        ) is False
    ]


def get_successes():

    return [

        item

        for item in learning_history

        if item.get(
            "success",
            False
        ) is True
    ]


def learning_summary():

    return {

        "total":
        len(
            learning_history
        ),

        "successes":
        len(
            get_successes()
        ),

        "failures":
        len(
            get_failures()
        )
    }