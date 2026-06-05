import psutil


async def process_manager_agent():

    processes = []

    for proc in psutil.process_iter(

        ["pid", "name"]

    ):

        try:

            processes.append({

                "pid":
                proc.info["pid"],

                "name":
                proc.info["name"]
            })

        except Exception:

            pass

    return processes[:100]