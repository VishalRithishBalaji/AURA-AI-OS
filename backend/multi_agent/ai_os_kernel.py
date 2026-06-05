from multi_agent.autonomous_runtime import (
    start_runtime
)

from multi_agent.system_governor import (
    initialize_governor
)


async def boot_ai_os():

    governor = initialize_governor()

    runtime = await start_runtime()

    return {

        "kernel": "AURA AI OS",

        "status": "running",

        "governor": governor,

        "runtime": runtime
    }