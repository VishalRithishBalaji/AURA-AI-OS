from llm.llm_router import ask_llm

from memory.memory_manager import (
    store_memory
)

from memory.semantic_search import (
    search_memory
)

from memory.conversation_memory import (
    add_message,
    get_conversation_context
)

from memory.memory_filter import (
    should_store_memory
)

from memory.memory_summarizer import (
    summarize_memory
)


async def root_agent(user_input: str):

    # SAVE USER MESSAGE
    add_message(
        "USER",
        user_input
    )

    # SHORT-TERM MEMORY
    conversation_context = (
        get_conversation_context()
    )

    # LONG-TERM MEMORY
    try:

        memories = search_memory(
            user_input
        )

        memory_context = "\n".join(
            memories
        )

    except Exception as e:

        print(
            f"Memory Search Error: {e}"
        )

        memory_context = ""

    # FINAL PROMPT
    final_prompt = f"""
Relevant Long-Term Memory:
{memory_context}

Recent Conversation:
{conversation_context}

Current User Message:
{user_input}
"""

    # GENERATE RESPONSE
    response = await ask_llm(
        final_prompt
    )

    # SAVE AI RESPONSE
    add_message(
        "AURA",
        response
    )

    # SMART MEMORY STORAGE
    try:

        if should_store_memory(
            user_input
        ):

            raw_memory = f"""
USER:
{user_input}

AURA:
{response}
"""

            # SUMMARIZE MEMORY
            summary_memory = summarize_memory(
                raw_memory
            )

            print(
                "🧠 Summarized Memory:"
            )

            print(summary_memory)

            # STORE SUMMARY
            store_memory(
                summary_memory
            )

            print(
                "✅ Important Memory Stored"
            )

        else:

            print(
                "❌ Memory Ignored"
            )

    except Exception as e:

        print(
            f"Memory Store Error: {e}"
        )

    return response