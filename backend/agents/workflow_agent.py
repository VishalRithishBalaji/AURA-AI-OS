import asyncio

from agents.planner_agent import (
    planner_agent
)

from agents.reflection_agent import (
    reflection_agent
)

from agents.async_executor import (
    execute_task
)

from multi_agent.agent_bus import (
    publish_event
)

from multi_agent.collaboration_manager import (
    get_collaboration_context
)

from cognition.cognitive_state import (

    update_status,
    update_step
)

from evolution.self_optimizer import (
    self_optimize
)


MAX_TASKS = 3


INVALID_TASK_PATTERNS = [

    "unexpected issue",
    "try again later",
    "error",
    "unavailable",
    "quota",
    "429",
    "503"
]


# =========================
# TASK VALIDATION
# =========================

def is_valid_task(
    task: str
):

    task = task.lower()

    for pattern in INVALID_TASK_PATTERNS:

        if pattern in task:

            return False

    return len(task.strip()) > 5


# =========================
# WORKFLOW AGENT
# =========================

async def workflow_agent(
    user_input: str
):

    # 📡 START EVENT
    publish_event(

        "WorkflowAgent",

        f"Starting workflow: {user_input}"
    )

    update_status(
        "WORKFLOW_PLANNING"
    )

    # 🤝 SHARED COLLABORATION CONTEXT
    collaboration_context = (
        get_collaboration_context(
            user_input
        )
    )

    # STEP 1 — PLAN
    subtasks = await planner_agent(
        f"""
Task:
{user_input}

Shared Collaboration Context:
{collaboration_context}

Generate concise executable subtasks.
"""
    )

    print("\n🧠 Generated Subtasks:")

    for task in subtasks:

        print(f"- {task}")

    # SAFETY CHECK
    if not subtasks:

        publish_event(

            "WorkflowAgent",

            "Workflow planning failed"
        )

        return """
❌ Workflow Planning Failed
"""

    # FILTER INVALID TASKS
    subtasks = [

        task

        for task in subtasks

        if is_valid_task(task)
    ]

    # LIMIT TASK COUNT
    subtasks = subtasks[:MAX_TASKS]

    # FALLBACK TASKS
    if not subtasks:

        subtasks = [

            "Analyze deployment requirements",

            "Prepare FastAPI deployment",

            "Optimize YOLO inference pipeline"
        ]

    # 📡 TASK EVENTS
    for task in subtasks:

        publish_event(

            "WorkflowAgent",

            f"Planned task: {task}"
        )

    update_status(
        "WORKFLOW_EXECUTION"
    )

    # STEP 2 — PARALLEL EXECUTION
    async_tasks = []

    for task in subtasks:

        update_step(task)

        async_tasks.append(

            execute_task(task)
        )

    results = await asyncio.gather(
        *async_tasks
    )

    # STEP 3 — COMBINE RESULTS
    combined_output = "\n".join(
        results
    )

    publish_event(

        "WorkflowAgent",

        "Workflow execution completed"
    )

    update_status(
        "WORKFLOW_REFLECTION"
    )

    # STEP 4 — REFLECTION
    try:

        reflection = await reflection_agent(
            combined_output
        )

        publish_event(

            "WorkflowAgent",

            "Reflection completed"
        )

    except Exception as e:

        reflection = f"""
Reflection unavailable.

Reason:
{str(e)}
"""

        publish_event(

            "WorkflowAgent",

            "Reflection failed"
        )

    # STEP 5 — RECURSIVE SELF-EVOLUTION
    update_status(
        "SELF_OPTIMIZATION"
    )

    try:

        evolution_report = (
            self_optimize()
        )

        publish_event(

            "WorkflowAgent",

            "Recursive self-improvement completed"
        )

    except Exception as e:

        evolution_report = f"""
Self-improvement unavailable.

Reason:
{str(e)}
"""

        publish_event(

            "WorkflowAgent",

            "Recursive self-improvement failed"
        )

    update_status(
        "WORKFLOW_COMPLETED"
    )

    # STEP 6 — FINAL RESPONSE
    return f"""
# 🚀 Autonomous Workflow Execution

## Shared Collaboration Context
{collaboration_context if collaboration_context else "No shared context available."}

---

{combined_output}

---

# 🪞 Reflection & Improvements

{reflection}

---

# 🧠 Recursive Evolution

{evolution_report}
"""
