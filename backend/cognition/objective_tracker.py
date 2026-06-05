from cognition.long_term_goals import (
    load_goals
)


CURRENT_OBJECTIVE = None

PROGRESS = 0

COMPLETED_TASKS = []

BLOCKED_TASKS = []


def set_objective(
    objective: str
):

    global CURRENT_OBJECTIVE

    CURRENT_OBJECTIVE = objective


def update_progress(
    value: int
):

    global PROGRESS

    PROGRESS = max(
        0,
        min(
            value,
            100
        )
    )


def add_completed_task(
    task: str
):

    COMPLETED_TASKS.append(
        task
    )


def add_blocked_task(
    task: str
):

    BLOCKED_TASKS.append(
        task
    )


def get_status():

    return {

        "objective":
        CURRENT_OBJECTIVE,

        "progress":
        PROGRESS,

        "completed":
        COMPLETED_TASKS,

        "blocked":
        BLOCKED_TASKS,

        "goals":
        load_goals()
    }