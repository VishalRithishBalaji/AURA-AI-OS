import json
import os


LOG_FILE = "workflow_history.json"


def get_successful_patterns():

    if not os.path.exists(
        LOG_FILE
    ):

        return []

    try:

        with open(

            LOG_FILE,

            "r",

            encoding="utf-8"

        ) as f:

            history = json.load(f)

        return history[-20:]

    except:

        return []