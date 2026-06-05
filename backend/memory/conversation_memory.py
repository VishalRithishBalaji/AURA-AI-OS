conversation_history = []


def add_message(role: str, content: str):

    conversation_history.append({
        "role": role,
        "content": content
    })

    # KEEP LAST 10 MESSAGES
    if len(conversation_history) > 10:

        conversation_history.pop(0)


def get_conversation_context():

    context = ""

    for msg in conversation_history:

        context += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    return context