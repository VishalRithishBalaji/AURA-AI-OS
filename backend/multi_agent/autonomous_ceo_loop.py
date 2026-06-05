from multi_agent.goal_queue import (
    add_goal,
    get_next_goal
)

from multi_agent.cross_cycle_decision_engine import (
    choose_next_goal
)

from multi_agent.executive_review_board import (
    executive_review
)

from multi_agent.department_budget_feedback import (
    update_department_budgets
)

from multi_agent.strategic_memory import (
    remember_strategy
)

from multi_agent.autonomous_society_v2 import (
    autonomous_society_v2
)


async def autonomous_ceo_loop():

    # =========================
    # DECIDE NEXT GOAL
    # =========================

    goal = choose_next_goal()

    add_goal(
        goal
    )

    current = (
        get_next_goal()
    )

    # =========================
    # EXECUTE SOCIETY
    # =========================

    result = await (
        autonomous_society_v2(
            current
        )
    )

    # =========================
    # STRATEGIC MEMORY
    # =========================

    remember_strategy(

        current,

        str(result)
    )

    # =========================
    # BUDGET FEEDBACK
    # =========================

    update_department_budgets()

    # =========================
    # EXECUTIVE REVIEW
    # =========================

    review = (
        executive_review()
    )

    return f"""
CEO LOOP

Goal:
{current}

RESULT:

{result}

REVIEW:

{review}
"""