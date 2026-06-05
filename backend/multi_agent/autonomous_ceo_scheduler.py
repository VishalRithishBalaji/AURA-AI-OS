import asyncio

from multi_agent.autonomous_ceo_loop import (
    autonomous_ceo_loop
)


async def autonomous_ceo_scheduler(
    cycles: int = 3
):

    reports = []

    for _ in range(cycles):

        result = await (
            autonomous_ceo_loop()
        )

        reports.append(
            result
        )

        await asyncio.sleep(
            1
        )

    return "\n".join(
        reports
    )