from brain.knowledge_base import (
    load_knowledge,
    save_knowledge
)


def add_knowledge(

    category: str,
    problem: str,
    solution: str

):

    knowledge = load_knowledge()

    entry = {

        "category":
            category,

        "problem":
            problem,

        "solution":
            solution
    }

    knowledge.append(entry)

    save_knowledge(
        knowledge
    )


def search_knowledge(
    query: str
):

    knowledge = load_knowledge()

    results = []

    query_words = query.lower().split()

    for item in knowledge:

        combined = f"""
{item['category']}
{item['problem']}
{item['solution']}
""".lower()

        score = 0

        for word in query_words:

            if word in combined:

                score += 1

        if score > 0:

            results.append(
                (score, item)
            )

    results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return [

        item[1]

        for item in results[:5]
    ]