from multi_agent.society_metrics import (
    generate_society_metrics
)

from multi_agent.department_reputation import (
    get_reputation
)

from multi_agent.society_learning_engine import (
    learning_summary
)


def executive_analytics():

    return {

        "metrics":
        generate_society_metrics(),

        "reputation":
        get_reputation(),

        "learning":
        learning_summary()
    }