import httpx

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


async def ask_ollama(prompt: str):

    print("🚀 Sending request to Ollama")

    async with httpx.AsyncClient(timeout=180) as client:

        response = await client.post(
            OLLAMA_URL,
            json={
                "model": "qwen3:4b",
                "prompt": prompt,
                "stream": False
            }
        )

        print(f"📥 Ollama Status: {response.status_code}")

        response.raise_for_status()

        data = response.json()

        print("✅ Ollama Response Received")

        return data.get("response", "")