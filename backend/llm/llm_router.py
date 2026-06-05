from llm.gemini_client import ask_gemini
from llm.ollama_client import ask_ollama


async def ask_llm(prompt: str):

    try:

        return await ask_ollama(
            prompt
        )

    except Exception as e:

        print(
            f"⚠️ Ollama failed: {e}"
        )

        print(
            "🔄 Falling back to Gemini"
        )

        return await ask_gemini(
            prompt
        )