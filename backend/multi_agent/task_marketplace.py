task_pool = []


def create_task(
    department: str,
    task: str
):

    task_data = {

        "department": department,

        "task": task,

        "status": "open"
    }

    task_pool.append(
        task_data
    )

    return task_data


def claim_tasks(
    department: str
):

    claimed = []

    for task in task_pool:

        if (

            task["department"]

            ==

            department

            and

            task["status"]

            ==

            "open"

        ):

            task["status"] = (
                "claimed"
            )

            claimed.append(
                task
            )

    return claimed


def get_task_pool():

    return task_pool