from agents.desktop_agent import (
    desktop_agent
)

from agents.workflow_execution_agent import (
    workflow_execution_agent
)

from agents.project_modification_agent import (
    project_modification_agent
)

from agents.autonomous_task_agent import (
    autonomous_task_agent
)

from agents.screen_vision_agent import (
    screen_vision_agent
)

from agents.project_agent import (
    project_agent
)

from agents.codebase_agent import (
    codebase_agent
)

from agents.desktop_automation_agent import (
    desktop_automation_agent
)

from agents.file_editor_agent import (
    file_editor_agent
)

from agents.project_refactor_agent import (
    project_refactor_agent
)

from agents.multi_file_editor_agent import (
    multi_file_editor_agent
)

from agents.code_generation_agent import (
    code_generation_agent
)

from agents.screen_understanding_agent import (
    screen_understanding_agent
)

from agents.task_agent import (
    task_agent
)

from agents.filesystem_agent import (
    filesystem_agent
)

from agents.terminal_agent import (
    terminal_agent
)

from agents.dynamic_workflow_agent import (
    dynamic_workflow_agent
)

from agents.project_modification_agent_v2 import (
    project_modification_agent_v2
)

from agents.vision_analysis_agent import (
    vision_analysis_agent
)

from agents.desktop_action_agent import (
    desktop_action_agent
)

async def computer_control_agent(
    task: str
):

    text = task.lower()

    # =========================
    # DESKTOP
    # =========================

    if any(word in text for word in [

        "open vscode",
        "open chrome",
        "open explorer"

    ]):

        return await desktop_agent(task)

    # =========================
    # DESKTOP AUTOMATION
    # =========================

    elif any(word in text for word in [

        "open github",
        "open chatgpt",
        "open downloads",
        "open desktop"

    ]):

        return await desktop_automation_agent(task)

    # =========================
    # FILE EDITOR
    # =========================

    elif any(word in text for word in [

        "create file",
        "read file"

    ]):

        return await file_editor_agent(task)

    # =========================
    # PROCESS CONTROL
    # =========================

    elif any(word in text for word in [

        "running processes",
        "kill uvicorn"

    ]):

        return await task_agent(task)

    # =========================
    # FILESYSTEM
    # =========================

    elif any(word in text for word in [

        "list files",
        "list folders",
        "current directory"

    ]):

        return await filesystem_agent(task)

    # =========================
    # PROJECT ANALYSIS
    # =========================

    elif any(word in text for word in [

        "project summary",
        "analyze project",
        "project structure"

    ]):

        return await project_agent(task)

    # =========================
    # CODEBASE ANALYSIS
    # =========================

    elif any(word in text for word in [

        "find todo",
        "find class",
        "find function"

    ]):

        return await codebase_agent(task)

    # =========================
    # PROJECT REFACTORING
    # =========================

    elif "refactor project" in text:

        return await project_refactor_agent(task)

    # =========================
    # PROJECT MODIFICATION
    # =========================

    elif "modify project" in text:

        return await project_modification_agent(task)

    # =========================
    # MULTI FILE EDITING
    # =========================

    elif "create api module" in text:

        return await multi_file_editor_agent(task)

    # =========================
    # CODE GENERATION
    # =========================

    elif "generate fastapi route" in text:

        return await code_generation_agent(task)

    # =========================
    # AUTONOMOUS WORKFLOWS
    # =========================

    elif any(word in text for word in [

        "docker workflow",
        "deployment workflow",
        "testing workflow",
        "refactor workflow"

    ]):

        return await autonomous_task_agent(task)

    # =========================
    # SCREEN ANALYSIS
    # =========================

    elif any(word in text for word in [

        "analyze screenshot",
        "screen understanding",
        "screen vision",
        "inspect screen"

    ]):

        return await screen_vision_agent(task)

    elif "dynamic workflow" in text:

        return await dynamic_workflow_agent(
            task
        )

    elif "modify project v2" in text:

        return await project_modification_agent_v2(
            task
        )

    elif any(word in text for word in [

        "vision analysis",
        "analyze screen"

    ]):

        return await vision_analysis_agent(
            task
        )

    elif any(word in text for word in [

        "click center",
        "scroll down",
        "take screenshot",
        "press enter",
        "ctrl s",
        "type text",
        "scroll down",
        "scroll up",
        "take screenshot"

    ]):

        return await desktop_action_agent(
            task
        )

    # =========================
    # TERMINAL FALLBACK
    # =========================

    return await terminal_agent(task)
