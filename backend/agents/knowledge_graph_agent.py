from knowledge_graph.entity_manager import (

    create_entity,

    list_entities
)

from knowledge_graph.relationship_manager import (

    create_relationship,

    list_relationships
)

from knowledge_graph.graph_query import (

    find_entity,

    get_connections
)


async def knowledge_graph_agent(
    task: str
):

    text = task.lower()

    # =========================
    # ENTITY
    # =========================

    if text.startswith(
        "create entity"
    ):

        parts = task.split(
            "|"
        )

        if len(parts) != 3:

            return """
Usage:

create entity|name|type
"""

        return create_entity(

            parts[1].strip(),

            parts[2].strip()
        )

    # =========================
    # RELATIONSHIP
    # =========================

    elif text.startswith(
        "create relationship"
    ):

        parts = task.split(
            "|"
        )

        if len(parts) != 4:

            return """
Usage:

create relationship|source|relation|target
"""

        return create_relationship(

            parts[1].strip(),

            parts[2].strip(),

            parts[3].strip()
        )

    elif text == "list entities":

        return list_entities()

    elif text == "list relationships":

        return list_relationships()

    elif text.startswith(
        "find entity"
    ):

        entity = (

            task.replace(

                "find entity",

                ""

            ).strip()
        )

        return find_entity(
            entity
        )

    elif text.startswith(
        "connections"
    ):

        entity = (

            task.replace(

                "connections",

                ""

            ).strip()
        )

        return get_connections(
            entity
        )

    return """
Knowledge Graph Agent

Commands:

create entity|name|type

create relationship|source|relation|target

list entities

list relationships

find entity <name>

connections <entity>
"""