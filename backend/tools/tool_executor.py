import subprocess
import tempfile
import os
import textwrap


def execute_python(code: str):

    try:

        # CLEAN INDENTATION
        code = textwrap.dedent(
            code
        ).strip()

        with tempfile.NamedTemporaryFile(

            delete=False,
            suffix=".py",
            mode="w",
            encoding="utf-8"

        ) as f:

            f.write(code)

            temp_path = f.name

        result = subprocess.run(

            ["python", temp_path],

            capture_output=True,

            text=True,

            timeout=20

        )

        os.remove(temp_path)

        return f"""
STDOUT:
{result.stdout}

STDERR:
{result.stderr}
"""

    except Exception as e:

        return str(e)


def execute_terminal(command: str):

    try:

        result = subprocess.run(

            command,

            shell=True,

            capture_output=True,

            text=True,

            timeout=30

        )

        return f"""
STDOUT:
{result.stdout}

STDERR:
{result.stderr}
"""

    except Exception as e:

        return str(e)