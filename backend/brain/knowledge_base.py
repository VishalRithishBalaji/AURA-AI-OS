import json
import os


KNOWLEDGE_FILE = (
    "brain/knowledge.json"
)


def load_knowledge():

    os.makedirs(
        "brain",
        exist_ok=True
    )

    if not os.path.exists(
        KNOWLEDGE_FILE
    ):

        return []

    try:

        with open(

            KNOWLEDGE_FILE,

            "r",

            encoding="utf-8"

        ) as f:

            return json.load(f)

    except:

        return []


def save_knowledge(
    knowledge
):

    with open(

        KNOWLEDGE_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            knowledge,

            f,

            indent=4
        )