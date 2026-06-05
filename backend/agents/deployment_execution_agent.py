import os

from agents.file_editor_agent import (
    file_editor_agent
)


async def deployment_execution_agent(
    task: str
):

    text = task.lower()

    # =========================
    # DOCKERFILE
    # =========================

    if "dockerfile" in text:

        return await file_editor_agent(
            "create Dockerfile"
        )

    # =========================
    # DOCKER COMPOSE
    # =========================

    elif (

        "docker-compose" in text

        or

        "docker compose" in text

    ):

        content = """
version: '3.9'

services:

  aura:

    build: .

    container_name: aura

    restart: unless-stopped

    ports:

      - "8000:8000"
"""

        with open(

            "docker-compose.yml",

            "w",

            encoding="utf-8"

        ) as f:

            f.write(content)

        return """
docker-compose.yml created.
"""

    # =========================
    # MONITORING
    # =========================

    elif (

        "monitoring" in text

        or

        "prometheus" in text

        or

        "grafana" in text

    ):

        monitoring = """
# Monitoring Stack

Prometheus
Grafana
Health Checks

Metrics:

- CPU
- Memory
- API Latency
- Error Rate
"""

        with open(

            "monitoring.md",

            "w",

            encoding="utf-8"

        ) as f:

            f.write(
                monitoring
            )

        return """
Monitoring plan created.
"""

    # =========================
    # HEALTH CHECKS
    # =========================

    elif "health check" in text:

        healthcheck = """
HEALTH CHECKS

GET /health

Expected:

{
  "status": "ok"
}
"""

        with open(

            "health_checks.md",

            "w",

            encoding="utf-8"

        ) as f:

            f.write(
                healthcheck
            )

        return """
Health check specification created.
"""

    # =========================
    # DEPLOYMENT PLAN
    # =========================

    elif "deployment" in text:

        return """
Deployment Plan

1. Create Dockerfile
2. Create docker-compose.yml
3. Configure Monitoring
4. Configure Health Checks
5. Build Container
6. Start Services
"""

    return """
Deployment task not recognized.
"""