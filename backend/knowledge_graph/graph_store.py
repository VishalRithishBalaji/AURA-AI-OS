from memory.persistent_memory import (
    remember,
    recall
)

GRAPH_KEY = "knowledge_graph"


def load_graph():

    graph = recall(
        GRAPH_KEY
    )

    if not graph:

        graph = {

            "entities": {},

            "relationships": []
        }

        remember(

            GRAPH_KEY,

            graph
        )

    return graph


def save_graph(
    graph: dict
):

    remember(

        GRAPH_KEY,

        graph
    )