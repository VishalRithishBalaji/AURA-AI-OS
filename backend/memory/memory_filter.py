IMPORTANT_PATTERNS = [

    "i am",
    "i'm",
    "my project",
    "working on",
    "building",
    "developing",
    "researching",
    "my goal",
    "i use",
    "i prefer",
    "my favorite",
    "i like",
    "interested in",
    "my startup",
    "my company",
    "my career",
    "i study",
    "student",
    "engineer",
    "developer",
]


TECH_KEYWORDS = [

    "ai",
    "ml",
    "deep learning",
    "yolo",
    "cnn",
    "transformer",
    "robotics",
    "cybersecurity",
    "drone",
    "fastapi",
    "nextjs",
    "python",
    "react",
    "llm",
]


def should_store_memory(text: str):

    text_lower = text.lower()

    # VERY SHORT = IGNORE
    if len(text_lower.split()) < 4:

        print("❌ Memory Ignored")

        return False

    # IMPORTANT PATTERNS
    for pattern in IMPORTANT_PATTERNS:

        if pattern in text_lower:

            print(
                "🧠 Important Memory Detected"
            )

            return True

    # TECH CONTEXT
    for keyword in TECH_KEYWORDS:

        if keyword in text_lower:

            print(
                "🧠 Technical Memory Stored"
            )

            return True

    print("❌ Memory Ignored")

    return False