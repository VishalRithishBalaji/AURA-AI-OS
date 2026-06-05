def decide_execution_mode(
    task: str
):

    text = task.lower()

    # HEAVY AUTONOMOUS TASKS
    if any(word in text for word in [

        "build",
        "deploy",
        "full system",
        "complete project",
        "autonomous"

    ]):

        return "workflow"

    # BROWSER TASKS
    elif any(word in text for word in [

        "search",
        "browse",
        "google"

    ]):

        return "browser"

    # TOOL TASKS
    elif any(word in text for word in [

        "tool",
        "generate"

    ]):

        return "tool"

    # EXECUTION TASKS
    elif any(word in text for word in [

        "run",
        "execute"

    ]):

        return "execution"

    # CODING
    return "coding"