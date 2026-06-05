from brain.brain_manager import (
    add_knowledge
)


MIN_RESULT_LENGTH = 150


IMPORTANT_PATTERNS = [

    "fixed",
    "solved",
    "deployment",
    "optimization",
    "solution",
    "working",
    "success",
    "resolved",
    "architecture",
    "implementation",
    "integration",
    "ai model",
    "fastapi",
    "yolov8",
    "drone",
    "system"
]


def should_learn(
    task: str,
    result: str
):

    combined = f"""
{task}
{result}
""".lower()

    # PATTERN MATCH
    for pattern in IMPORTANT_PATTERNS:

        if pattern in combined:

            return True

    # LONG TECHNICAL OUTPUT
    if len(result) > MIN_RESULT_LENGTH:

        return True

    return False


def learn_from_execution(

    task: str,
    result: str

):

    try:

        if not should_learn(

            task,
            result
        ):

            return

        add_knowledge(

            category="workflow_learning",

            problem=task,

            solution=result[:2000]
        )

        print(
            "\n🧠 New Knowledge Learned"
        )

    except Exception as e:

        print(
            f"\nLearning Error: {e}"
        )