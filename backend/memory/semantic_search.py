from memory.vector_store import (
    create_embedding
)

from memory.chroma_memory import (
    identity_collection,
    project_collection,
    technology_collection,
    goal_collection,
    preference_collection
)


collections = [

    identity_collection,
    project_collection,
    technology_collection,
    goal_collection,
    preference_collection
]


def search_memory(
    query: str,
    n_results=2
):

    embedding = create_embedding(
        query
    )

    all_memories = []

    for collection in collections:

        try:

            results = collection.query(
                query_embeddings=[embedding],
                n_results=n_results
            )

            docs = results["documents"][0]

            all_memories.extend(docs)

        except:

            pass

    return all_memories