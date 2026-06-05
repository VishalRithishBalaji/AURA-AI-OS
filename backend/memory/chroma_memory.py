import chromadb


client = chromadb.PersistentClient(
    path="./memory_db"
)


identity_collection = (
    client.get_or_create_collection(
        name="identity_memory"
    )
)

project_collection = (
    client.get_or_create_collection(
        name="project_memory"
    )
)

technology_collection = (
    client.get_or_create_collection(
        name="technology_memory"
    )
)

goal_collection = (
    client.get_or_create_collection(
        name="goal_memory"
    )
)

preference_collection = (
    client.get_or_create_collection(
        name="preference_memory"
    )
)