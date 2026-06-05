from agents.project_agent import (
    project_agent
)

from agents.codebase_agent import (
    codebase_agent
)

from agents.task_classifier import (
    classify_task
)

from agents.tool_manager_agent import (
    tool_manager_agent
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

from agents.coding_agent import (
    coding_agent
)

from agents.file_editor_agent import (
    file_editor_agent
)

from agents.deployment_execution_agent import (
    deployment_execution_agent
)

from agents.security_execution_agent import (
    security_execution_agent
)

from departments.research_agent import (
    research_agent
)

from multi_agent.agent_bus import (
    publish_event
)

from agents.planning_execution_agent import (
    planning_execution_agent
)


async def autonomous_executor(
    task: str
):

    try:

        task_type = classify_task(
            task
        )

        publish_event(

            "AutonomousExecutor",

            f"Task Type: {task_type}"
        )

        # =========================
        # PROJECT
        # =========================

        if task_type == "project":

            return await project_agent(
                task
            )

        # =========================
        # CODEBASE
        # =========================

        elif task_type == "codebase":

            return await codebase_agent(
                task
            )

        elif task_type == "planning":

            return await planning_execution_agent(
                task
            )

        # =========================
        # TOOLS
        # =========================

        elif task_type == "tool":

            return await tool_manager_agent(
                task
            )

        # =========================
        # TERMINAL
        # =========================

        elif task_type == "terminal":

            return await terminal_agent(
                task
            )

        # =========================
        # FILE EDITOR
        # =========================

        elif task_type == "file_editor":

            return await file_editor_agent(
                task
            )

        # =========================
        # FILESYSTEM
        # =========================

        elif task_type == "filesystem":

            return await filesystem_agent(
                task
            )

        # =========================
        # BROWSER
        # =========================

        elif task_type == "browser":

            return await browser_control_agent(
                task
            )

        # =========================
        # CODING
        # =========================

        elif task_type == "coding":

            return await coding_agent(
                task
            )

        # =========================
        # RESEARCH
        # =========================

        elif task_type == "research":

            return await research_agent(
                task
            )

        # =========================
        # DEPLOYMENT
        # =========================

        elif task_type == "deployment":

            return await deployment_execution_agent(
                task
            )

        # =========================
        # SECURITY
        # =========================

        elif task_type == "security":

            return await security_execution_agent(
                task
            )

        # =========================
        # GENERAL
        # =========================

        publish_event(

            "AutonomousExecutor",

            "No specialized executor found"
        )

        return f"""
No autonomous execution path found.

Task:
{task}

Task Type:
{task_type}
"""

    except Exception as e:

        publish_event(

            "AutonomousExecutor",

            f"Execution Error: {e}"
        )

        return f"""
Execution Error

Task:
{task}

Error:
{e}
"""