WORKFLOWS = {

    "docker": [

        "analyze project",
        "create Dockerfile",
        "verify deployment structure"
    ],

    "deployment": [

        "analyze project",
        "generate fastapi route",
        "prepare deployment configuration"
    ],

    "testing": [

        "find function",
        "run tests"
    ],

    "refactor": [

        "analyze project",
        "find function",
        "refactor project"
    ]
}


def get_workflow(
    workflow_name: str
):

    return WORKFLOWS.get(

        workflow_name.lower(),

        []
    )