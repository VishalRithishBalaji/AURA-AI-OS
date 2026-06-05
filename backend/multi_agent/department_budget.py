department_budget = {

    "planner": 100,
    "research": 100,
    "deployment": 100,
    "security": 100,
    "memory": 100
}


def reward_budget(
    department: str,
    amount: int = 5
):

    department_budget[department] = (

        department_budget.get(
            department,
            100
        ) + amount
    )


def penalize_budget(
    department: str,
    amount: int = 5
):

    department_budget[department] = max(

        0,

        department_budget.get(
            department,
            100
        ) - amount
    )


def get_budgets():

    return department_budget