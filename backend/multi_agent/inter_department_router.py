from multi_agent.department_bus import (
    publish_department_message
)


def route_department_message(
    sender: str,
    receiver: str,
    message: str
):

    publish_department_message(

        sender,

        f"[TO:{receiver}] {message}"
    )

    return f"""
Message Routed

From:
{sender}

To:
{receiver}
"""