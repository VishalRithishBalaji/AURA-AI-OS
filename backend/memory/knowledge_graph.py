knowledge_graph = {}


def add_relation(
    parent: str,
    child: str
):

    if parent not in knowledge_graph:

        knowledge_graph[parent] = []

    if child not in knowledge_graph[parent]:

        knowledge_graph[parent].append(
            child
        )


def get_relations(
    node: str
):

    return knowledge_graph.get(
        node,
        []
    )


def get_graph():

    return knowledge_graph