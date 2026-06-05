import json
import os


LOG_FILE = "workflow_history.json"


def log_task(
    workflow: str,
    task: str,
    result: str
):

    history = []

    if os.path.exists(
        LOG_FILE
    ):

        try:

            with open(

                LOG_FILE,

                "r",

                encoding="utf-8"

            ) as f:

                history = json.load(f)

        except:

            history = []

    history.append({

        "workflow": workflow,

        "task": task,

        "result": result
    })

    with open(

        LOG_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            history,

            f,

            indent=4
        )