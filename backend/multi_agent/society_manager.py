from departments.research_agent import (
    research_agent
)

from departments.deployment_agent import (
    deployment_agent
)

from departments.security_agent import (
    security_agent
)

from departments.memory_agent import (
    memory_agent
)

from agents.planner_agent import (
    planner_agent
)

from multi_agent.task_delegator import (
    delegate_tasks
)

from multi_agent.report_aggregator import (
    aggregate_reports
)

from multi_agent.consensus_engine import (
    build_consensus
)

from multi_agent.department_bus import (
    publish_department_message
)

from multi_agent.department_review_engine import (
    review_report
)

from multi_agent.executive_decision_engine import (
    executive_decision
)

from multi_agent.department_memory import (
    save_department_memory
)

from multi_agent.inter_department_router import (
    route_department_message
)

from multi_agent.dynamic_delegation_engine import (
    dynamic_delegate
)

from multi_agent.task_marketplace import (
    get_task_pool
)

from multi_agent.executive_board import (
    board_vote
)

from multi_agent.department_performance import (
    record_performance
)

async def society_manager(
    objective: str
):

    assignments = delegate_tasks(
        objective
    )

    print(
        f"\n🏢 Departments Assigned: {assignments}"
    )

    reports = {}

    # =========================
    # PLANNER
    # =========================

    if "planner" in assignments:

        try:

            publish_department_message(

                "CEO",

                "Planner assigned"
            )

            plan = await planner_agent(
                objective
            )

            reports["planner"] = plan

        except Exception as e:

            reports["planner"] = (
                f"Planner Error: {e}"
            )

    # =========================
    # RESEARCH
    # =========================

    if "research" in assignments:

        try:

            publish_department_message(

                "CEO",

                "Research assigned"
            )

            research = await (
                research_agent(
                    objective
                )
            )

            reports["research"] = (
                research
            )

        except Exception as e:

            reports["research"] = (
                f"Research Error: {e}"
            )

    # =========================
    # DEPLOYMENT
    # =========================

    if "deployment" in assignments:

        try:

            publish_department_message(

                "CEO",

                "Deployment assigned"
            )

            deployment = await (
                deployment_agent(
                    objective
                )
            )

            reports["deployment"] = (
                deployment
            )

        except Exception as e:

            reports["deployment"] = (
                f"Deployment Error: {e}"
            )

    # =========================
    # SECURITY
    # =========================

    if "security" in assignments:

        try:

            publish_department_message(

                "CEO",

                "Security assigned"
            )

            security = await (
                security_agent(
                    objective
                )
            )

            reports["security"] = (
                security
            )

        except Exception as e:

            reports["security"] = (
                f"Security Error: {e}"
            )

    # =========================
    # MEMORY
    # =========================

    if "memory" in assignments:

        try:

            publish_department_message(

                "CEO",

                "Memory assigned"
            )

            memory = await (
                memory_agent(
                    objective
                )
            )

            reports["memory"] = (
                memory
            )

        except Exception as e:

            reports["memory"] = (
                f"Memory Error: {e}"
            )

    # =========================
    # INTER-DEPARTMENT REVIEWS
    # =========================

    reviews = []

    if "planner" in reports and "research" in reports:

        review = review_report(

            "research",

            "planner",

            str(reports["planner"])
        )

        reviews.append(review)

    if "deployment" in reports and "research" in reports:

        review = review_report(

            "deployment",

            "research",

            str(reports["research"])
        )

        reviews.append(review)

    if "security" in reports and "deployment" in reports:

        review = review_report(

            "security",

            "deployment",

            str(reports["deployment"])
        )

        reviews.append(review)

    # =========================
    # STORE DEPARTMENT MEMORY
    # =========================

    for department, report in reports.items():

        save_department_memory(

            department,

            str(report)
        )

    # =========================
    # DEPARTMENT COMMUNICATION
    # =========================

    route_department_message(

        "Planner",

        "Research",

        "Plan ready for review"
    )

    route_department_message(

        "Research",

        "Deployment",

        "Research findings available"
    )

    route_department_message(

        "Deployment",

        "Security",

        "Deployment architecture ready"
    )

    # =========================
    # DYNAMIC DELEGATION
    # =========================

    delegated_tasks = dynamic_delegate(

        "CEO",

        objective
    )

    marketplace_tasks = (
        get_task_pool()
    )

    # =========================
    # CONSENSUS
    # =========================

    consensus = build_consensus(
        reports
    )

    # =========================
    # EXECUTIVE BOARD
    # =========================

    board_result = board_vote(

        objective,

        list(reports.keys())
    )

    # =========================
    # EXECUTIVE DECISION
    # =========================

    decision = executive_decision(

        objective,

        reports
    )

    # =========================
    # PERFORMANCE TRACKING
    # =========================

    for department in reports:

        record_performance(

            department,

            True
        )

    # =========================
    # EXECUTIVE REPORT
    # =========================

    executive_report = aggregate_reports(
        reports
    )

    return f"""
🏢 CEO REPORT

Objective:
{objective}

{consensus}

=========================
DEPARTMENT REVIEWS
=========================

{chr(10).join(reviews)}

=========================
EXECUTIVE BOARD
=========================

{board_result}

=========================
DYNAMIC DELEGATION
=========================

{delegated_tasks}

=========================
TASK MARKETPLACE
=========================

{marketplace_tasks}

=========================
EXECUTIVE DECISION
=========================

{decision}

=========================
EXECUTIVE REPORT
=========================

{executive_report}
"""