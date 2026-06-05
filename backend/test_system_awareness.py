import asyncio

from agents.system_monitor_agent import (
    system_monitor_agent
)

from agents.process_manager_agent import (
    process_manager_agent
)

from agents.resource_manager_agent import (
    resource_manager_agent
)

from agents.service_manager_agent import (
    service_manager_agent
)


async def main():

    print("\nSYSTEM\n")
    print(
        await system_monitor_agent()
    )

    print("\nRESOURCES\n")
    print(
        await resource_manager_agent()
    )

    print("\nPROCESSES\n")
    print(
        len(
            await process_manager_agent()
        )
    )

    print("\nSERVICES\n")
    print(
        len(
            await service_manager_agent()
        )
    )


asyncio.run(main())