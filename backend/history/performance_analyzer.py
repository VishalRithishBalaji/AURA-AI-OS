import json
import os


HISTORY_FILE = (
    "history/history.json"
)


def analyze_performance():

    if not os.path.exists(
        HISTORY_FILE
    ):

        return "No execution history found."

    with open(

        HISTORY_FILE,

        "r",

        encoding="utf-8"

    ) as f:

        history = json.load(f)

    total = len(history)

    success_count = sum(

        1 for h in history

        if h["success"]
    )

    failed = total - success_count

    success_rate = (
        success_count / total * 100
    )

    return f"""
# 📊 AURA Performance Report

Total Executions:
{total}

Successful:
{success_count}

Failed:
{failed}

Success Rate:
{success_rate:.2f}%
"""