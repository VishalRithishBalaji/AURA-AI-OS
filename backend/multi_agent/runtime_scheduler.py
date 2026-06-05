import asyncio

from multi_agent.autonomous_ceo_loop import (
    autonomous_ceo_loop
)

from multi_agent.autonomous_runtime import (
    increment_cycle
)


async def run_scheduler(
    cycles: int = 3
):

    reports = []

    for _ in range(cycles):

        report = await (
            autonomous_ceo_loop()
        )

        reports.append(
            report
        )

        increment_cycle()

        await asyncio.sleep(1)

    return reports