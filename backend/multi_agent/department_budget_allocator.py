from multi_agent.department_reputation import (
    get_reputation
)

from multi_agent.department_budget import (
    reward_budget,
    penalize_budget
)


def allocate_budget():

    reputation = (
        get_reputation()
    )

    for dept, score in reputation.items():

        if score > 100:

            reward_budget(
                dept
            )

        elif score < 100:

            penalize_budget(
                dept
            )
