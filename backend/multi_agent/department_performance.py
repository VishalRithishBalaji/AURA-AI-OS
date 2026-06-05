department_metrics = {}


def record_performance(
    department: str,
    success: bool
):

    if department not in (
        department_metrics
    ):

        department_metrics[
            department
        ] = {

            "success": 0,

            "failure": 0
        }

    if success:

        department_metrics[
            department
        ]["success"] += 1

    else:

        department_metrics[
            department
        ]["failure"] += 1


def get_performance():

    return department_metrics