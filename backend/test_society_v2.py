import asyncio

from multi_agent.autonomous_society_v2 import (
    autonomous_society_v2
)


result = asyncio.run(

    autonomous_society_v2(

        "production deployment"
    )
)

print(result)