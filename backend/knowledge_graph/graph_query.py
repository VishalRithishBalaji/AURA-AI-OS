from knowledge_graph.graph_store import (
    load_graph
)


def find_entity(
    name: str
):

    graph = load_graph()

    return graph[
        "entities"
    ].get(
        name
    )


def get_connections(
    entity: str
):

    graph = load_graph()

    connections = []

    for rel in graph[
        "relationships"
    ]:

        if (

            rel["source"]
            == entity

            or

            rel["target"]
            == entity

        ):

            connections.append(
                rel
            )

    return connections