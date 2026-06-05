from multi_agent.executive_analytics import (
    executive_analytics
)

from multi_agent.strategy_engine import (
    choose_strategy
)


async def autonomous_ceo_agent():

    analytics = (
        executive_analytics()
    )

    strategy = (
        choose_strategy()
    )

    return f"""
CEO REPORT

Analytics:

{analytics}

Strategy:

{strategy}
"""