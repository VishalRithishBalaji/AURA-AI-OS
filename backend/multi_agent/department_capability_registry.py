department_capabilities = {

    "planner": [

        "planning",
        "workflow optimization"
    ],

    "research": [

        "research",
        "documentation"
    ],

    "deployment": [

        "deployment",
        "monitoring"
    ],

    "security": [

        "security"
    ],

    "memory": [

        "memory"
    ]
}


def can_execute(
    department,
    goal
):

    return goal in (

        department_capabilities.get(
            department,
            []
        )
    )
