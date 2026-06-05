from multi_agent.society_metrics import (
    generate_society_metrics
)

from multi_agent.department_reputation import (
    get_reputation
)

from multi_agent.society_learning_engine import (
    get_learnings
)


def executive_dashboard():

    metrics = (
        generate_society_metrics()
    )

    reputation = (
        get_reputation()
    )

    learnings = (
        get_learnings()
    )

    return {

        "metrics": metrics,

        "reputation": reputation,

        "learning_count": len(
            learnings
        )
    }