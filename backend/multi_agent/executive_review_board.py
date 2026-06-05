from multi_agent.executive_analytics import (
    executive_analytics
)


def executive_review():

    analytics = (
        executive_analytics()
    )

    return {

        "review":
        analytics
    }