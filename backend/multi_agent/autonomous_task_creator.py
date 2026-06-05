def create_tasks_from_goal(
    goal: str
):

    tasks = []

    goal = goal.lower()

    # =========================
    # DEPLOYMENT
    # =========================

    if goal == "deployment":

        tasks.append({

            "department": "deployment",

            "task": "create Dockerfile"
        })

        tasks.append({

            "department": "deployment",

            "task": "create docker-compose"
        })

    # =========================
    # SECURITY
    # =========================

    elif goal == "security":

        tasks.append({

            "department": "security",

            "task": "security audit deployment"
        })

    # =========================
    # MONITORING
    # =========================

    elif goal == "monitoring":

        tasks.append({

            "department": "deployment",

            "task": "setup monitoring"
        })

    # =========================
    # DOCUMENTATION
    # =========================

    elif goal == "documentation":

        tasks.append({

            "department": "research",

            "task": "generate deployment documentation"
        })

    return tasks