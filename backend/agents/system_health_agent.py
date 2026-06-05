from agents.system_monitor_agent import (
    system_monitor_agent
)

from agents.resource_manager_agent import (
    resource_manager_agent
)


async def system_health_agent():

    system = await (
        system_monitor_agent()
    )

    resources = await (
        resource_manager_agent()
    )

    cpu = system[
        "cpu_percent"
    ]

    memory = system[
        "memory_percent"
    ]

    disk = system[
        "disk_percent"
    ]

    health = "Healthy"

    recommendations = []

    # =========================
    # CPU
    # =========================

    if cpu > 85:

        health = "Warning"

        recommendations.append(
            "High CPU usage detected."
        )

    # =========================
    # MEMORY
    # =========================

    if memory > 85:

        health = "Warning"

        recommendations.append(
            "High memory usage detected."
        )

    # =========================
    # DISK
    # =========================

    if disk > 90:

        health = "Critical"

        recommendations.append(
            "Disk nearly full."
        )

    if not recommendations:

        recommendations.append(
            "No action required."
        )

    return {

        "health":
        health,

        "cpu_percent":
        cpu,

        "memory_percent":
        memory,

        "disk_percent":
        disk,

        "recommendations":
        recommendations
    }