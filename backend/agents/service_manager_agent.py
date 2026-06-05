import psutil


async def service_manager_agent():

    services = []

    for proc in psutil.process_iter(

        ["name"]

    ):

        try:

            name = proc.info["name"]

            if name:

                services.append(
                    name
                )

        except Exception:

            pass

    return sorted(

        list(
            set(
                services
            )
        )

    )[:100]