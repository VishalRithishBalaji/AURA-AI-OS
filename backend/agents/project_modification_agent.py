from agents.project_agent import (
    project_agent
)

from agents.codebase_agent import (
    codebase_agent
)

from agents.code_generation_agent import (
    code_generation_agent
)

from agents.multi_file_editor_agent import (
    multi_file_editor_agent
)


async def project_modification_agent(
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

    report.append(

        await code_generation_agent(
            task
        )
    )

    report.append(

        await multi_file_editor_agent(
            task
        )
    )

    return "\n\n".join(
        report
    )