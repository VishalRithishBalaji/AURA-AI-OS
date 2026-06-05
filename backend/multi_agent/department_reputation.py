department_reputation = {

    "planner": 100,
    "research": 100,
    "deployment": 100,
    "security": 100,
    "memory": 100
}


def reward_department(
    department: str
):

    department_reputation[
        department
    ] += 1


def penalize_department(
    department: str
):

    department_reputation[
        department
    ] -= 1


def get_reputation():

    return department_reputation