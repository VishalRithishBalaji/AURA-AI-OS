from knowledge_graph.graph_store import (
    load_graph,
    save_graph
)


def create_relationship(

    source: str,

    relation: str,

    target: str

):

    graph = load_graph()

    graph[
        "relationships"
    ].append({

        "source":
        source,

        "relation":
        relation,

        "target":
        target
    })

    save_graph(
        graph
    )

    return "Relationship Created"


def list_relationships():

    graph = load_graph()

    return graph[
        "relationships"
    ]