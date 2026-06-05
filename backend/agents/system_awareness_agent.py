from agents.system_monitor_agent import (
    system_monitor_agent
)

from agents.resource_manager_agent import (
    resource_manager_agent
)

from agents.process_manager_agent import (
    process_manager_agent
)

from agents.service_manager_agent import (
    service_manager_agent
)

from agents.system_health_agent import (
    system_health_agent
)

from agents.network_monitor_agent import (
    network_monitor_agent
)

from agents.process_control_agent import (
    process_control_agent
)


async def system_awareness_agent(
    task: str
):

    text = task.lower()

    # =========================
    # SYSTEM HEALTH
    # =========================

    if "system health" in text:

        return await (
            system_health_agent()
        )

    # =========================
    # NETWORK STATUS
    # =========================

    elif "network status" in text:

        return await (
            network_monitor_agent()
        )

    # =========================
    # PROCESS CONTROL
    # =========================

    elif "top processes" in text:

        return await (
            process_control_agent(
                task
            )
        )

    elif "kill process" in text:

        return await (
            process_control_agent(
                task
            )
        )

    # =========================
    # SYSTEM STATUS
    # =========================

    elif any(word in text for word in [

        "system status",
        "machine status"

    ]):

        system = await (
            system_monitor_agent()
        )

        resources = await (
            resource_manager_agent()
        )

        return {

            "cpu_percent":
            system["cpu_percent"],

            "memory_percent":
            system["memory_percent"],

            "disk_percent":
            system["disk_percent"],

            "memory_used_gb":
            resources["memory_used_gb"],

            "memory_available_gb":
            resources["memory_available_gb"],

            "disk_used_gb":
            resources["disk_used_gb"]
        }

    # =========================
    # CPU
    # =========================

    elif "cpu" in text:

        system = await (
            system_monitor_agent()
        )

        return {

            "cpu_percent":
            system["cpu_percent"]
        }

    # =========================
    # MEMORY
    # =========================

    elif any(word in text for word in [

        "memory",
        "memory usage",
        "ram"

    ]):

        return await (
            resource_manager_agent()
        )

    # =========================
    # PROCESSES
    # =========================

    elif any(word in text for word in [

        "running processes",
        "process list",
        "processes"

    ]):

        processes = await (
            process_manager_agent()
        )

        return {

            "count":
            len(
                processes
            ),

            "processes":
            processes[:25]
        }

    # =========================
    # SERVICES
    # =========================

    elif any(word in text for word in [

        "running services",
        "services"

    ]):

        services = await (
            service_manager_agent()
        )

        return {

            "count":
            len(
                services
            ),

            "services":
            services[:25]
        }

    # =========================
    # HELP
    # =========================

    return """
System Awareness Agent

Available Commands:

- system status
- system health
- network status
- cpu usage
- memory usage
- running processes
- top processes
- running services
- kill process <name>
"""