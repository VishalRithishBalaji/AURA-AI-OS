import json
import os


MEMORY_FILE = "memory_store.json"


def load_memory():

    if not os.path.exists(
        MEMORY_FILE
    ):

        return {}

    try:

        with open(

            MEMORY_FILE,

            "r",

            encoding="utf-8"

        ) as f:

            return json.load(
                f
            )

    except Exception:

        return {}


def save_memory(
    data: dict
):

    with open(

        MEMORY_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            data,

            f,

            indent=2
        )


def remember(
    key: str,
    value
):

    memory = load_memory()

    memory[key] = value

    save_memory(
        memory
    )


def recall(
    key: str
):

    memory = load_memory()

    return memory.get(
        key
    )


def get_all_memory():

    return load_memory()