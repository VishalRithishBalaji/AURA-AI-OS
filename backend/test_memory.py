from memory.project_memory import (
    save_project,
    list_projects
)

save_project(

    "AURA",

    {

        "phase":
        "12.4"
    }
)

print(

    list_projects()
)