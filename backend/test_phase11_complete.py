import asyncio

from multi_agent.autonomous_ceo_scheduler import (
    autonomous_ceo_scheduler
)


result = asyncio.run(

    autonomous_ceo_scheduler(
        3
    )
)

print(result)