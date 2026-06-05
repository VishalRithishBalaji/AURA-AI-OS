import json
import os


HISTORY_FILE = (
    "history/execution_history.json"
)


def load_execution_history():

    if not os.path.exists(
        HISTORY_FILE
    ):

        return []

    try:

        with open(

            HISTORY_FILE,

            "r",

            encoding="utf-8"

        ) as f:

            return json.load(f)

    except:

        return []


def save_execution_history(

    task: str,
    result: str,
    success: bool

):

    history = (
        load_execution_history()
    )

    history.append({

        "task": task,

        "result": result,

        "success": success
    })

    with open(

        HISTORY_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            history,

            f,

            indent=2
        )