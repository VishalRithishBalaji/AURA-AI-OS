import asyncio

from multi_agent.ai_os_kernel import (
    boot_ai_os
)


result = asyncio.run(

    boot_ai_os()
)

print(

    "\nAI OS BOOT REPORT\n"
)

print(result)