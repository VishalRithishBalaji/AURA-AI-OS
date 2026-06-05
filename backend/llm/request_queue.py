import asyncio
import time

LAST_REQUEST_TIME = 0

MIN_REQUEST_INTERVAL = 5

LLM_SEMAPHORE = asyncio.Semaphore(1)


async def wait_for_rate_limit():

    global LAST_REQUEST_TIME

    async with LLM_SEMAPHORE:

        now = time.time()

        elapsed = now - LAST_REQUEST_TIME

        if elapsed < MIN_REQUEST_INTERVAL:

            wait_time = (
                MIN_REQUEST_INTERVAL
                - elapsed
            )

            print(
                f"⏳ Waiting {wait_time:.1f}s"
            )

            await asyncio.sleep(
                wait_time
            )

        LAST_REQUEST_TIME = time.time()