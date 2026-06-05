from multi_agent.inter_department_router import (
    route_department_message
)


def run_cross_department_workflow():

    workflow = []

    workflow.append(

        route_department_message(

            "Research",

            "Deployment",

            "Research completed"
        )
    )

    workflow.append(

        route_department_message(

            "Deployment",

            "Security",

            "Deployment ready for audit"
        )
    )

    workflow.append(

        route_department_message(

            "Security",

            "Memory",

            "Audit completed"
        )
    )

    return workflow