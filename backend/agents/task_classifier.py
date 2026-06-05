def classify_task(
    task: str
):

    text = task.lower()

    # =========================
    # PROJECT
    # =========================

    if any(word in text for word in [

        "analyze project",
        "project summary",
        "project structure",
        "verify deployment structure"

    ]):

        return "project"

    # =========================
    # RESEARCH / DOCUMENTATION
    # =========================

    elif any(word in text for word in [

        "research",
        "investigate",
        "study",
        "compare",
        "evaluate",

        "documentation",
        "document",
        "deployment documentation",
        "generate deployment documentation",
        "write documentation"

    ]):

        return "research"

    # =========================
    # SECURITY
    # =========================

    elif any(word in text for word in [

        "security audit",
        "security scan",
        "credential scan",
        "vulnerability",
        "audit deployment"

    ]):

        return "security"

    # =========================
    # DEPLOYMENT
    # =========================

    elif any(word in text for word in [

        "docker-compose",
        "docker compose",
        "deployment plan",
        "deployment",
        "monitoring",
        "setup monitoring",
        "prometheus",
        "grafana"

    ]):

        return "deployment"

    # =========================
    # FILE EDITOR
    # =========================

    elif any(word in text for word in [

        "create dockerfile",
        "create file",
        "read file",
        "write file",
        "append file",
        "replace text"

    ]):

        return "file_editor"

    # =========================
    # CODEBASE
    # =========================

    elif any(word in text for word in [

        "find function",
        "find class",
        "find todo"

    ]):

        return "codebase"

    # =========================
    # FILESYSTEM
    # =========================

    elif any(word in text for word in [

        "list files",
        "list folders",
        "current directory",
        "filesystem"

    ]):

        return "filesystem"

    # =========================
    # TOOL MANAGER
    # =========================

    elif any(word in text for word in [

        "clone repository",
        "github repository",
        "github workflow",
        "github actions",
        "docker deployment",
        "containerize",
        "plugin",
        "tool registry"

    ]):

        return "tool"

    # =========================
    # TERMINAL
    # =========================

    elif any(word in text for word in [

        "git",
        "pip",
        "powershell",
        "terminal",
        "cmd",
        "install",
        "execute",
        "run script",
        "command",
        "pytest",
        "build"

    ]):

        return "terminal"

    # =========================
    # BROWSER
    # =========================

    elif any(word in text for word in [

        "website",
        "browser",
        "google",
        "search web",
        "browse",
        "internet"

    ]):

        return "browser"

    # =========================
    # CODING
    # =========================

    elif any(word in text for word in [

        "generate fastapi route",
        "generate code",
        "fix bug",
        "debug code"

    ]):

        return "coding"

    elif any(word in text for word in [

        "planning",
        "delegation",
        "workflow optimization"

    ]):

        return "planning"

    # =========================
    # DEFAULT
    # =========================

    return "general"