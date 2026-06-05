CURRENT_GOAL = None

CURRENT_PLAN = []

CURRENT_STEP = None

LAST_REFLECTION = None

SYSTEM_STATUS = "IDLE"


def update_goal(
    goal: str
):

    global CURRENT_GOAL

    CURRENT_GOAL = goal


def update_plan(
    plan
):

    global CURRENT_PLAN

    CURRENT_PLAN = plan


def update_step(
    step
):

    global CURRENT_STEP

    CURRENT_STEP = step


def update_reflection(
    reflection
):

    global LAST_REFLECTION

    LAST_REFLECTION = reflection


def update_status(
    status
):

    global SYSTEM_STATUS

    SYSTEM_STATUS = status


def get_cognitive_state():

    return {

        "goal":
            CURRENT_GOAL,

        "plan":
            CURRENT_PLAN,

        "current_step":
            CURRENT_STEP,

        "reflection":
            LAST_REFLECTION,

        "status":
            SYSTEM_STATUS
    }