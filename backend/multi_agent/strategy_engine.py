from multi_agent.department_reputation import (
    get_reputation
)


def choose_strategy():

    reputation = get_reputation()

    strongest = max(

        reputation,

        key=reputation.get
    )

    return {

        "focus_department":
        strongest,

        "strategy":
        f"Prioritize {strongest}"
    }