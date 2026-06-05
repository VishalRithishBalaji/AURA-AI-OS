from multi_agent.department_reputation import (
    get_reputation
)

from multi_agent.department_budget import (
    reward_budget,
    penalize_budget
)


def update_department_budgets():

    reputation = (
        get_reputation()
    )

    for dept, score in reputation.items():

        if score > 100:

            reward_budget(
                dept,
                10
            )

        elif score < 100:

            penalize_budget(
                dept,
                10
            )