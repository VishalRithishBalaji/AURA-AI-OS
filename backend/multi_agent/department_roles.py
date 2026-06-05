DEPARTMENT_ROLES = {

    "planner": [
        "task planning",
        "roadmaps",
        "workflow design"
    ],

    "research": [
        "analysis",
        "benchmarking",
        "documentation"
    ],

    "deployment": [
        "docker",
        "ci cd",
        "infrastructure"
    ],

    "security": [
        "security audits",
        "credential scanning",
        "risk assessment"
    ],

    "memory": [
        "knowledge retention",
        "decision history",
        "context tracking"
    ]
}


def get_role(
    department: str
):

    return DEPARTMENT_ROLES.get(
        department,
        []
    )