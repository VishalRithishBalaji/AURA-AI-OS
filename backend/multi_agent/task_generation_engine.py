def generate_tasks(
    objective: str
):

    objective = objective.lower()

    tasks = []

    if "deployment" in objective:

        tasks.extend([

            {
                "department": "deployment",
                "task": "create Dockerfile"
            },

            {
                "department": "deployment",
                "task": "create docker-compose"
            },

            {
                "department": "security",
                "task": "security audit deployment"
            }
        ])

    elif "api" in objective:

        tasks.extend([

            {
                "department": "research",
                "task": "research api best practices"
            },

            {
                "department": "deployment",
                "task": "deploy api"
            }
        ])

    else:

        tasks.append({

            "department": "research",

            "task": f"research {objective}"
        })

    return tasks