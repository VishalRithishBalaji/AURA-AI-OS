import os


async def project_agent(
    task: str
):

    try:

        total_files = 0
        total_dirs = 0

        extensions = {}

        for root, dirs, files in os.walk("."):

            total_dirs += len(dirs)

            for file in files:

                total_files += 1

                ext = os.path.splitext(file)[1]

                if ext:

                    extensions[ext] = (

                        extensions.get(ext, 0)
                        + 1
                    )

        top_extensions = sorted(

            extensions.items(),

            key=lambda x: x[1],

            reverse=True

        )[:10]

        report = f"""
Project Summary

Directories: {total_dirs}
Files: {total_files}

Top File Types:
"""

        for ext, count in top_extensions:

            report += f"\n{ext}: {count}"

        return report

    except Exception as e:

        return str(e)