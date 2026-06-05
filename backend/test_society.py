import asyncio

from multi_agent.task_marketplace import (
    create_task
)

from multi_agent.society_scheduler import (
    run_society_cycle
)


create_task(

    "deployment",

    "create Dockerfile"
)

print(

    asyncio.run(
        run_society_cycle()
    )
)