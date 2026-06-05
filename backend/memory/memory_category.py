def detect_memory_category(text: str):

    text = text.lower()

    # IDENTITY
    if any(word in text for word in [
        "i am",
        "student",
        "engineer",
        "developer",
        "profession"
    ]):

        return "identity"

    # PROJECTS
    if any(word in text for word in [
        "project",
        "building",
        "developing",
        "working on",
        "research"
    ]):

        return "project"

    # TECHNOLOGIES
    if any(word in text for word in [
        "yolo",
        "fastapi",
        "python",
        "react",
        "cnn",
        "transformer",
        "ai",
        "robotics"
    ]):

        return "technology"

    # GOALS
    if any(word in text for word in [
        "goal",
        "dream",
        "aim",
        "want to",
        "career"
    ]):

        return "goal"

    # PREFERENCES
    if any(word in text for word in [
        "favorite",
        "prefer",
        "like",
        "love",
        "interested in"
    ]):

        return "preference"

    return "general"