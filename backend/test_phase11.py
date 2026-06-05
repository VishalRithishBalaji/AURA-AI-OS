import asyncio

from departments.autonomous_ceo_agent import (
    autonomous_ceo_agent
)


result = asyncio.run(

    autonomous_ceo_agent()
)

print(result)