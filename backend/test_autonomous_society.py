import asyncio

from multi_agent.autonomous_society_loop import (
    autonomous_society_loop
)

result = asyncio.run(

    autonomous_society_loop(

        "production deployment"
    )
)

print(result)