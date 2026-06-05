import json
import os
from datetime import datetime


HISTORY_FILE = (
    "history/history.json"
)


def save_execution_history(

    task: str,
    result: str,
    success: bool

):

    os.makedirs(
        "history",
        exist_ok=True
    )

    history = []

    # LOAD EXISTING
    if os.path.exists(
        HISTORY_FILE
    ):

        try:

            with open(

                HISTORY_FILE,

                "r",

                encoding="utf-8"

            ) as f:

                history = json.load(f)

        except:

            history = []

    # NEW ENTRY
    entry = {

        "timestamp":
            str(datetime.now()),

        "task":
            task,

        "success":
            success,

        "result":
            result[:1000]
    }

    history.append(entry)

    # SAVE
    with open(

        HISTORY_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            history,

            f,

            indent=4
        )