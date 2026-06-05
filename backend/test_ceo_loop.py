import asyncio

from multi_agent.autonomous_ceo_loop import (
    autonomous_ceo_loop
)


result = asyncio.run(

    autonomous_ceo_loop()
)

print(result)