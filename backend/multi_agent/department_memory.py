department_memory_store = {

    "planner": [],
    "research": [],
    "deployment": [],
    "security": [],
    "memory": []
}


def save_department_memory(
    department: str,
    content: str
):

    if department not in (
        department_memory_store
    ):

        department_memory_store[
            department
        ] = []

    department_memory_store[
        department
    ].append(content)


def get_department_memory(
    department: str
):

    return department_memory_store.get(
        department,
        []
    )[-20:]