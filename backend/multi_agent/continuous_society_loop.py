import asyncio

from departments.autonomous_ceo_agent import (
    autonomous_ceo_agent
)


async def continuous_society_loop():

    cycles = []

    for _ in range(3):

        report = await (
            autonomous_ceo_agent()
        )

        cycles.append(
            report
        )

        await asyncio.sleep(
            1
        )

    return "\n".join(
        cycles
    )