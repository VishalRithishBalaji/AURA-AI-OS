from pathlib import Path


async def file_editor_agent(
    task: str
):

    text = task.lower()

    try:

        # CREATE FILE

        if "create file" in text:

            parts = task.split()

            filename = parts[-1]

            Path(filename).touch()

            return f"""
File created:

{filename}
"""
        elif "create dockerfile" in text:

            dockerfile = """
        FROM python:3.11

        WORKDIR /app

        COPY . .

        RUN pip install -r requirements.txt

        CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
        """

            with open(

                "Dockerfile",

                "w",

                encoding="utf-8"

            ) as f:

                f.write(dockerfile)

            return """
        Dockerfile created.
        """

        elif "append file" in text:

            parts = task.split("|")

            filename = parts[1].strip()

            content = parts[2]

            with open(

                filename,

                "a",

                encoding="utf-8"

            ) as f:

                f.write(content)

            return f"""
        Content appended:

        {filename}
        """

        elif "write file" in text:

            parts = task.split("|")

            filename = parts[1].strip()

            content = parts[2]

            with open(

                filename,

                "w",

                encoding="utf-8"

            ) as f:

                f.write(content)

            return f"""
        File written:

        {filename}
        """

        elif "replace text" in text:

            parts = task.split("|")

            filename = parts[1].strip()

            old_text = parts[2]

            new_text = parts[3]

            with open(

                filename,

                "r",

                encoding="utf-8"

            ) as f:

                content = f.read()

            content = content.replace(

                old_text,

                new_text
            )

            with open(

                filename,

                "w",

                encoding="utf-8"

            ) as f:

                f.write(content)

            return f"""
        Text replaced:

        {filename}
        """

        # READ FILE

        elif "read file" in text:

            filename = task.replace(
                "read file",
                ""
            ).strip()

            with open(

                filename,

                "r",

                encoding="utf-8"

            ) as f:

                return f.read()

        return """
File Editor Agent:
No supported operation detected.
"""

    except Exception as e:

        return f"""
File Editor Error:

{str(e)}
"""