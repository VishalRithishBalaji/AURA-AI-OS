
import asyncio
import re


MAX_RETRIES = 3

MAX_WAIT_SECONDS = 30


async def retry_with_backoff(
    func,
    *args,
    **kwargs
):

    for attempt in range(MAX_RETRIES):

        try:

            return await func(
                *args,
                **kwargs
            )

        except Exception as e:

            error = str(e)

            print(
                f"\n⚠️ Retry {attempt + 1} Failed:"
            )

            print(error)

            # =========================
            # QUOTA EXHAUSTED
            # =========================

            if (
                "429" in error
                or "RESOURCE_EXHAUSTED" in error
            ):

                retry_seconds = 5

                # EXTRACT RETRY DELAY
                match = re.search(

                    r"retry in ([0-9.]+)(ms|s)?",

                    error.lower()
                )

                if match:

                    value = float(
                        match.group(1)
                    )

                    unit = match.group(2)

                    # MILLISECONDS
                    if unit == "ms":

                        retry_seconds = max(
                            value / 1000,
                            1
                        )

                    # SECONDS
                    else:

                        retry_seconds = max(
                            value,
                            1
                        )

                # SAFETY LIMIT
                retry_seconds = min(

                    retry_seconds,

                    MAX_WAIT_SECONDS
                )

                print(
                    f"\n⏳ Waiting {retry_seconds:.1f}s for API cooldown..."
                )

                await asyncio.sleep(
                    retry_seconds
                )

            # =========================
            # SERVER OVERLOAD
            # =========================

            elif (
                "503" in error
                or "UNAVAILABLE" in error
            ):

                wait_time = min(

                    2 * (attempt + 1),

                    10
                )

                print(
                    f"\n⏳ Retrying in {wait_time}s..."
                )

                await asyncio.sleep(
                    wait_time
                )

            # =========================
            # UNKNOWN ERRORS
            # =========================

            else:

                wait_time = min(

                    attempt + 1,

                    5
                )

                print(
                    f"\n⏳ Unknown error. Retrying in {wait_time}s..."
                )

                await asyncio.sleep(
                    wait_time
                )

    # =========================
    # FINAL FAILURE RESPONSE
    # =========================

    return """
⚠️ Gemini API quota exceeded.

Possible fixes:
- Wait for cooldown
- Upgrade Gemini API plan
- Use another API key
- Switch to local LLM fallback

Recommended local models:
- Ollama
- LM Studio
- DeepSeek
- Mistral
"""
