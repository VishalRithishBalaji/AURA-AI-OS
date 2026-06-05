session_memory = {}


def remember_session(
    key: str,
    value
):

    session_memory[
        key
    ] = value


def recall_session(
    key: str
):

    return session_memory.get(
        key
    )


def get_session():

    return session_memory