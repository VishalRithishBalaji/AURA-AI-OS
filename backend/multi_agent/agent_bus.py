from multi_agent.shared_memory import (
    add_shared_memory
)


def publish_event(

    agent: str,
    event: str

):

    print(
        f"\n📡 {agent}: {event}"
    )

    add_shared_memory(

        agent,

        event
    )