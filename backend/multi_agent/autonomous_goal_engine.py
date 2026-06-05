def generate_subgoals(
    objective: str
):

    objective = objective.lower()

    goals = []

    # =========================
    # DEPLOYMENT
    # =========================

    if "deployment" in objective:

        goals.extend([

            "deployment",

            "security",

            "monitoring",

            "documentation"
        ])

    # =========================
    # API PROJECTS
    # =========================

    elif "api" in objective:

        goals.extend([

            "api design",

            "security",

            "deployment"
        ])

    # =========================
    # PLANNING
    # =========================

    elif "planning" in objective:

        goals.extend([

            "planning",

            "workflow optimization"
        ])

    # =========================
    # MEMORY
    # =========================

    elif "memory" in objective:

        goals.extend([

            "memory",

            "knowledge management"
        ])

    # =========================
    # RESEARCH
    # =========================

    elif "research" in objective:

        goals.extend([

            "research",

            "documentation"
        ])

    # =========================
    # SECURITY
    # =========================

    elif "security" in objective:

        goals.extend([

            "security",

            "compliance"
        ])

    # =========================
    # MONITORING
    # =========================

    elif "monitoring" in objective:

        goals.extend([

            "monitoring",

            "alerting",

            "dashboard"
        ])

    # =========================
    # FALLBACK
    # =========================

    else:

        goals.append(
            objective
        )

    return goals