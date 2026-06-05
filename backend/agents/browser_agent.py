import threading
import asyncio

from browser.playwright_controller import (
    google_search
)

from memory.shared_memory import (
    get_shared_memory_context
)

from multi_agent.agent_bus import (
    publish_event
)

from multi_agent.collaboration_manager import (
    get_collaboration_context
)


# =========================
# THREAD RUNNER
# =========================

def run_browser(
    query: str
):

    asyncio.run(
        google_search(query)
    )


# =========================
# BROWSER AGENT
# =========================

async def browser_agent(
    user_input: str
):

    # 📡 AGENT EVENT
    publish_event(

        "BrowserAgent",

        f"Received task: {user_input}"
    )

    # 🧠 USER MEMORY
    memory_context = (
        get_shared_memory_context(
            user_input
        )
    )

    # 🤝 SHARED AGENT CONTEXT
    collaboration_context = (
        get_collaboration_context(
            user_input
        )
    )

    # CLEAN QUERY
    query = user_input

    for word in [

        "search web",
        "browse",
        "google",
        "internet search"
    ]:

        query = query.replace(
            word,
            ""
        )

    query = query.strip()

    # 🧠 CONTEXTUAL SEARCH
    enhanced_query = query

    if memory_context:

        enhanced_query += f"""

User Context:
{memory_context}
"""

    if collaboration_context:

        enhanced_query += f"""

Agent Collaboration Context:
{collaboration_context}
"""

    # 📡 SEARCH EVENT
    publish_event(

        "BrowserAgent",

        f"Searching web for: {query}"
    )

    # START THREAD
    thread = threading.Thread(

        target=run_browser,

        args=(enhanced_query,),

        daemon=True

    )

    thread.start()

    # 📡 SUCCESS EVENT
    publish_event(

        "BrowserAgent",

        "Chrome browser launched successfully"
    )

    return f"""
# 🌐 Browser Agent Activated

## Query
➡️ {query}

---

## Memory Context
{memory_context if memory_context else "No relevant memory found."}

---

## Collaboration Context
{collaboration_context if collaboration_context else "No shared collaboration context."}

---

✅ Chrome browser launched successfully.
"""