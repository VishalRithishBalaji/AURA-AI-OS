goal_queue = []


def add_goal(
    goal: str
):

    goal_queue.append(
        goal
    )


def get_next_goal():

    if not goal_queue:

        return None

    return goal_queue.pop(0)


def get_goals():

    return goal_queue