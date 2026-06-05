SHARED_MEMORY = []


MAX_SHARED_ITEMS = 50


def add_shared_memory(

    agent: str,
    content: str

):

    global SHARED_MEMORY

    SHARED_MEMORY.append({

        "agent":
            agent,

        "content":
            content
    })

    # LIMIT MEMORY SIZE
    if len(SHARED_MEMORY) > MAX_SHARED_ITEMS:

        SHARED_MEMORY = SHARED_MEMORY[
            -MAX_SHARED_ITEMS:
        ]


def get_shared_memory():

    return SHARED_MEMORY


def search_shared_memory(
    query: str
):

    query = query.lower()

    results = []

    for item in SHARED_MEMORY:

        if query in item[
            "content"
        ].lower():

            results.append(item)

    return results[:10]