from knowledge_graph.graph_store import (
    load_graph,
    save_graph
)


def create_entity(
    entity_name: str,
    entity_type: str
):

    graph = load_graph()

    graph["entities"][
        entity_name
    ] = {

        "type":
        entity_type
    }

    save_graph(
        graph
    )

    return graph["entities"][
        entity_name
    ]


def list_entities():

    graph = load_graph()

    return graph[
        "entities"
    ]