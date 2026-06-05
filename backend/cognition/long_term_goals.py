import json
import os
from datetime import datetime

GOALS_FILE = "memory/long_term_goals.json"


def _ensure_file():

    os.makedirs("memory", exist_ok=True)

    if not os.path.exists(GOALS_FILE):

        with open(
            GOALS_FILE,
            "w"
        ) as f:

            json.dump([], f)


def load_goals():

    _ensure_file()

    with open(
        GOALS_FILE,
        "r"
    ) as f:

        return json.load(f)


def save_goals(goals):

    with open(
        GOALS_FILE,
        "w"
    ) as f:

        json.dump(
            goals,
            f,
            indent=4
        )


def add_goal(
    goal: str,
    priority="medium"
):

    goals = load_goals()

    goals.append({

        "goal": goal,

        "priority": priority,

        "status": "active",

        "created_at":
        datetime.now().isoformat()
    })

    save_goals(goals)


def complete_goal(
    goal: str
):

    goals = load_goals()

    for g in goals:

        if g["goal"] == goal:

            g["status"] = "completed"

    save_goals(goals)


def delete_goal(
    goal: str
):

    goals = [

        g

        for g in load_goals()

        if g["goal"] != goal
    ]

    save_goals(goals)