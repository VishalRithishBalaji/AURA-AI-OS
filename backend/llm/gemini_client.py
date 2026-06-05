from google import genai

from config import GOOGLE_API_KEY

from utils.retry_handler import retry_with_backoff

from llm.request_queue import (
    wait_for_rate_limit
)

client = genai.Client(
    api_key=GOOGLE_API_KEY
)

SYSTEM_PROMPT = """
You are AURA AI.

You are:
- intelligent
- calm
- professional
- technically accurate
- concise
"""


async def generate_response(
    full_prompt: str
):

    await wait_for_rate_limit()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    return response.text


async def ask_gemini(
    prompt: str
):

    try:

        full_prompt = f"""
{SYSTEM_PROMPT}

USER:
{prompt}
"""

        return await retry_with_backoff(
            generate_response,
            full_prompt
        )

    except Exception as e:

        print(f"Gemini Error: {e}")

        return f"""
⚠️ Gemini Failure

Reason:
{str(e)}
"""