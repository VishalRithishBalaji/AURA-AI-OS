from agents.tool_manager_agent import (
    tool_manager_agent
)

from agents.computer_control_agent import (
    computer_control_agent
)

from agents.terminal_agent import (
    terminal_agent
)

from agents.filesystem_agent import (
    filesystem_agent
)

from agents.browser_control_agent import (
    browser_control_agent
)
from agents.root_agent import (
    root_agent
)

from agents.browser_agent import (
    browser_agent
)

from agents.planner_agent import (
    planner_agent
)

from agents.coding_agent import (
    coding_agent
)

from agents.workflow_agent import (
    workflow_agent
)

from agents.execution_agent import (
    execution_agent
)

from agents.tool_creator_agent import (
    tool_creator_agent
)

from agents.self_improvement_agent import (
    self_improvement_agent
)

from agents.knowledge_agent import (
    knowledge_agent
)

from agents.cognitive_agent import (
    cognitive_agent
)

from agents.shared_memory_agent import (
    shared_memory_agent
)

from agents.evolution_agent import (
    evolution_agent
)

from multi_agent.agent_bus import (
    publish_event
)

from cognition.cognitive_state import (
    update_status
)

from departments.ceo_agent import (
    ceo_agent
)

from agents.ai_os_agent import (
    ai_os_agent
)

from agents.system_awareness_agent import (
    system_awareness_agent
)

from agents.desktop_control_agent import (
    desktop_control_agent
)

from agents.memory_recall_agent import (
    memory_recall_agent
)

from agents.memory_store_agent import (
    memory_store_agent
)

from agents.workspace_agent import (
    workspace_agent
)

from agents.project_os_agent import (
    project_os_agent
)

from agents.project_execution_agent import (
    project_execution_agent
)

from agents.knowledge_graph_agent import (
    knowledge_graph_agent
)

from agents.meta_learning_agent import (
    meta_learning_agent
)

from agents.autonomous_runtime_agent import (
    autonomous_runtime_agent
)

async def route_task(
    user_input: str
):

    text = user_input.lower()

    # 📡 LOG USER REQUEST
    publish_event(

        "Orchestrator",

        f"Routing request: {user_input}"
    )

    update_status(
        "ROUTING"
    )

    if any(word in user_input.lower() for word in [

        "boot ai os",
        "start ai os",
        "kernel status",
        "ai os status"

    ]):

        print(
            "\n📡 Orchestrator: Routing to AIOSAgent"
        )

        return await ai_os_agent(
            user_input
        )


    elif any(word in user_input.lower() for word in [

        "start runtime",
        "stop runtime",
        "runtime status",
        "run cycle",
        "scheduled goals"

    ]):

        print(
            "\n📡 Orchestrator: Routing to AutonomousRuntimeAgent"
        )

        return await (
            autonomous_runtime_agent(
                user_input
            )
        )

    elif any(word in user_input.lower() for word in [

        "optimize agents",
        "run evolution",
        "meta learning",
        "improvement strategies",
        "strategies "

    ]):

        print(
            "\n📡 Orchestrator: Routing to MetaLearningAgent"
        )

        return await (
            meta_learning_agent(
                user_input
            )
        )

    elif any(word in user_input.lower() for word in [

        "create entity",
        "create relationship",
        "list entities",
        "list relationships",
        "find entity",
        "connections"

    ]):

        print(
            "\n📡 Orchestrator: Routing to KnowledgeGraphAgent"
        )

        return await (
            knowledge_graph_agent(
                user_input
            )
        )

    elif any(word in user_input.lower() for word in [

        "execute project",
        "execute milestones",
        "project health",
        "generate roadmap"

    ]):

        print(
            "\n📡 Orchestrator: Routing to ProjectExecutionAgent"
        )

        return await (
            project_execution_agent(
                user_input
            )
        )

    elif any(word in user_input.lower() for word in [

        "create project",
        "list projects",
        "add milestone",
        "complete milestone",
        "project dashboard",
        "schedule project",
        "project schedule"

    ]):

        print(
            "\n📡 Orchestrator: Routing to ProjectOSAgent"
        )

        return await (
            project_os_agent(
                user_input
            )
        )

    # =========================
    # WORKSPACE
    # =========================

    elif any(word in user_input.lower() for word in [

        "activate project",

        "workspace projects",

        "workspace status",

        "resume workspace"

    ]):

        print(
            "\n📡 Orchestrator: Routing to WorkspaceAgent"
        )

        return await (
            workspace_agent(
                user_input
            )
        )

    # =========================
    # MEMORY STORAGE
    # =========================

    elif user_input.lower().startswith(
        "remember"
    ):

        print(
            "\n📡 Orchestrator: Routing to MemoryStoreAgent"
        )

        return await (
            memory_store_agent(
                user_input
            )
        )

    # =========================
    # MEMORY RECALL
    # =========================

    elif any(word in user_input.lower() for word in [

        "all memory",
        "projects",
        "workflows"

    ]):

        print(
            "\n📡 Orchestrator: Routing to MemoryRecallAgent"
        )

        return await (
            memory_recall_agent(
                user_input
            )
        )

    # =========================
    # DESKTOP CONTROL
    # =========================

    elif any(word in user_input.lower() for word in [

        # App State

        "application state",
        "desktop state",
        "active window",

        # Workflows

        "open notepad",
        "open chrome",
        "open vscode",

        # Focus

        "focus",
        "focus window",
        "focus chrome",
        "focus vscode",
        "focus notepad",

        # Windows

        "list windows",
        "window list",

        # Input

        "type ",
        "press ",
        "click "


    ]):

        print(
            "\n📡 Orchestrator: Routing to DesktopControlAgent"
        )

        return await (
            desktop_control_agent(
                user_input
            )
        )

    # =========================
    # AI OS SYSTEM AWARENESS
    # =========================

    elif any(word in user_input.lower() for word in[
        "system status",
        "system health",
        "machine status",

        "cpu",
        "cpu usage",

        "memory",
        "memory usage",

        "running processes",
        "top processes",

        "running services",

        "network status",

        "kill process"
    ]):

        print(
            "\n📡 Orchestrator: Routing to SystemAwarenessAgent"
        )

        return await (
            system_awareness_agent(
                user_input
            )
        )

    # =========================
    # 🧠 COGNITIVE TASKS
    # =========================

    elif any(word in text for word in [

        "autonomously",
        "analyze deeply",
        "think step-by-step",
        "complete autonomously",
        "reason about",
        "think carefully",
        "self analyze"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to CognitiveAgent"
        )

        update_status(
            "COGNITIVE_REASONING"
        )

        return await cognitive_agent(
            user_input
        )

    # =========================
    # 🧠 EVOLUTION TASKS
    # =========================

    elif any(word in text for word in [

        "evolve yourself",
        "self optimize",
        "recursive improvement",
        "improve architecture",
        "analyze failures"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to EvolutionAgent"
        )

        update_status(
            "SELF_EVOLUTION"
        )

        return await evolution_agent()
    
    # =========================
    # 🌍 BROWSER CONTROL
    # =========================

    elif any(word in text for word in [

        "open website",
        "navigate website",
        "browser control"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to BrowserControlAgent"
        )

        update_status(
            "BROWSER_CONTROL"
        )

        return await browser_control_agent(
            user_input
        )

    # =========================
    # 🌐 BROWSER TASKS
    # =========================

    elif any(word in text for word in [

        "search",
        "browse",
        "google",

    ]):

        publish_event(

            "Orchestrator",

            "Routing to BrowserAgent"
        )

        update_status(
            "BROWSER_EXECUTION"
        )

        return await browser_agent(
            user_input
        )

    # =========================
    # ⚙️ EXECUTION TASKS
    # =========================

    elif any(word in text for word in [

        "run python",
        "run terminal",
        "execute code",
        "execute script"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to ExecutionAgent"
        )

        update_status(
            "EXECUTION_RUNTIME"
        )

        return await execution_agent(
            user_input
        )



    # =========================
    # 🛠 TOOL GENERATION TASKS
    # =========================

    elif any(word in text for word in [

        "create tool",
        "create a tool",
        "generate tool",
        "build tool"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to ToolCreatorAgent"
        )

        update_status(
            "TOOL_GENERATION"
        )

        return await tool_creator_agent(
            user_input
        )

    # =========================
    # 🧠 SELF IMPROVEMENT TASKS
    # =========================

    elif any(word in text for word in [

        "analyze yourself",
        "improve yourself",
        "performance report",
        "self improvement"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to SelfImprovementAgent"
        )

        update_status(
            "SELF_ANALYSIS"
        )

        return await self_improvement_agent()

    # =========================
    # 🧠 KNOWLEDGE TASKS
    # =========================

    elif any(word in text for word in [

        "what have you learned",
        "knowledge base",
        "learned solutions",
        "past solutions",
        "what do you know",
        "show memories"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to KnowledgeAgent"
        )

        update_status(
            "KNOWLEDGE_RETRIEVAL"
        )

        return await knowledge_agent(
            user_input
        )

    # =========================
    # 🧠 SHARED MEMORY TASKS
    # =========================

    elif any(word in text for word in [

        "shared memory",
        "agent memory",
        "collaboration memory"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to SharedMemoryAgent"
        )

        update_status(
            "SHARED_MEMORY_ACCESS"
        )

        return await shared_memory_agent()


    # =========================
    # 🔧 TOOL MANAGER
    # =========================

    elif any(word in text for word in [

        "clone repository",
        "github repository",
        "github workflow",
        "github actions",

        "docker deployment",
        "docker image",
        "containerize",

        "browser plugin",
        "tool registry"

    ]):
        publish_event(

            "Orchestrator",

            "Routing to ToolManagerAgent"
        )

        update_status(
            "TOOL_EXECUTION"
        )

        return await tool_manager_agent(
            user_input
        )
    

    # =========================
    # 📁 FILESYSTEM TASKS
    # =========================

    elif any(word in text for word in [

        "list files",
        "show files",
        "list folders",
        "current directory"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to FilesystemAgent"
        )

        update_status(
            "FILESYSTEM_ACCESS"
        )

        return await filesystem_agent(
            user_input
        )
    
    # =========================
    # 💻 TERMINAL TASKS
    # =========================

    elif any(word in text for word in [

        "git status",
        "git pull",
        "git push",
        "pip install",
        "terminal command",
        "powershell command"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to TerminalAgent"
        )

        update_status(
            "TERMINAL_EXECUTION"
        )

        return await terminal_agent(
            user_input
        )
    

    # =========================
    # 🖥 COMPUTER CONTROL
    # =========================

    elif any(word in text for word in [

        # Desktop
        "open vscode",
        "open chrome",
        "open explorer",
        "open github",
        "open chatgpt",
        "open downloads",
        "open desktop",

        # Files
        "create file",
        "read file",

        # Processes
        "running processes",
        "kill uvicorn",

        # Project
        "analyze project",
        "project summary",
        "project structure",
        "refactor project",

        # Codebase
        "find function",
        "find class",
        "find todo",

        # Generation
        "create api module",
        "generate fastapi route",

        # Workflows
        "docker workflow",
        "deployment workflow",
        "testing workflow",
        "refactor workflow",
        "dynamic workflow",

        "modify project v2",
        "vision analysis",
        "analyze screen",
        "take screenshot",
        "click center",
        "scroll down"


        # Screen
        "analyze screenshot",
        "screen understanding",
        "inspect screen",

        "press enter",
        "ctrl s",
        "type text",
        "scroll down",
        "scroll up",
        "take screenshot"

        
    ]):

        publish_event(

            "Orchestrator",

            "Routing to ComputerControlAgent"
        )

        update_status(
            "COMPUTER_CONTROL"
        )

        return await computer_control_agent(
            user_input
        )


    # =========================
    # 💻 CODING + DEBUG TASKS
    # HIGH PRIORITY
    # =========================

    elif any(word in text for word in [

        "code",
        "bug",
        "error",
        "fastapi",
        "react",
        "nextjs",
        "api",
        "python",
        "debug",
        "fix",
        "implement",
        "function",
        "deployment issue",
        "uvicorn",
        "gunicorn",
        "nginx"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to CodingAgent"
        )

        update_status(
            "CODING_EXECUTION"
        )

        return await coding_agent(
            user_input
        )

    # =========================
    # 🚀 WORKFLOW TASKS
    # LOWER PRIORITY
    # =========================

    elif any(word in text for word in [

        "build full system",
        "complete project",
        "full infrastructure",
        "full architecture",
        "autonomous workflow",
        "multi-step execution",
        "deploy entire project",
        "complete setup",
        "end-to-end system"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to WorkflowAgent"
        )

        update_status(
            "WORKFLOW_EXECUTION"
        )

        return await workflow_agent(
            user_input
        )


    # =========================
    # 🏢 PHASE 10 CEO AGENT
    # =========================

    elif any(word in text for word in [

        "production deployment",
        "enterprise deployment",
        "enterprise architecture",
        "system architecture",
        "multi agent",
        "multi-agent",
        "department collaboration",
        "organization strategy",
        "company strategy",
        "deployment strategy",
        "security strategy",
        "long term strategy",
        "prepare aura for production",
        "prepare aura for deployment",
        "build enterprise system",
        "ceo task",
        "society task"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to CEOAgent"
        )

        update_status(
            "MULTI_AGENT_SOCIETY"
        )

        return await ceo_agent(
            user_input
        )

    # =========================
    # 🗺 PLANNING TASKS
    # =========================

    elif any(word in text for word in [

        "plan",
        "roadmap",
        "steps",
        "architecture",
        "strategy"

    ]):

        publish_event(

            "Orchestrator",

            "Routing to PlannerAgent"
        )

        update_status(
            "PLANNING"
        )

        tasks = await planner_agent(
            user_input
        )

        return "\n".join([

            f"• {task}"

            for task in tasks

        ])

    # =========================
    # 🧠 DEFAULT ROOT AGENT
    # =========================

    else:

        publish_event(

            "Orchestrator",

            "Routing to RootAgent"
        )

        update_status(
            "GENERAL_CONVERSATION"
        )

        return await root_agent(
            user_input
        )
