import asyncio

from agents.desktop_manager_agent import (
    desktop_manager_agent
)


async def main():

    print(

        await desktop_manager_agent(
            "open notepad"
        )

    )

    print(

        await desktop_manager_agent(
            "list windows"
        )

    )


asyncio.run(main())