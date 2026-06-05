from history.history_manager import (
    load_execution_history
)


FAILURE_PATTERNS = [

    "unexpected issue",
    "quota",
    "429",
    "503",
    "reflection unavailable",
    "workflow planning failed",
    "task failed"
]


def detect_failures():

    history = load_execution_history()

    failures = []

    for item in history:

        result = item.get(
            "result",
            ""
        ).lower()

        for pattern in FAILURE_PATTERNS:

            if pattern in result:

                failures.append(item)

                break

    return failures