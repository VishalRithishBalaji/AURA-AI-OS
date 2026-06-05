import uuid

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

from memory.memory_category import (
    detect_memory_category
)


def get_collection(category: str):

    collections = {

        "identity":
        identity_collection,

        "project":
        project_collection,

        "technology":
        technology_collection,

        "goal":
        goal_collection,

        "preference":
        preference_collection
    }

    return collections.get(
        category,
        project_collection
    )


def store_memory(text: str):

    embedding = create_embedding(
        text
    )

    category = detect_memory_category(
        text
    )

    collection = get_collection(
        category
    )

    collection.add(
        ids=[str(uuid.uuid4())],
        documents=[text],
        embeddings=[embedding]
    )

    print(
        f"🧠 Stored in category: {category}"
    )