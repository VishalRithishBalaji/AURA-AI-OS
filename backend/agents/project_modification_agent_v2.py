from pathlib import Path

from agents.project_agent import (
    project_agent
)

from agents.codebase_agent import (
    codebase_agent
)


async def project_modification_agent_v2(
    task: str
):

    report = []

    report.append(

        await project_agent(
            "analyze project"
        )
    )

    report.append(

        await codebase_agent(
            "find function"
        )
    )

    if "create dockerfile" in task.lower():

        dockerfile = """
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
"""

        Path(
            "Dockerfile"
        ).write_text(
            dockerfile
        )

        report.append(
            "Dockerfile created."
        )

    return "\n".join(
        report
    )