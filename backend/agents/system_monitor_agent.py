import psutil


async def system_monitor_agent():

    return {

        "cpu_percent":
        psutil.cpu_percent(interval=1),

        "memory_percent":
        psutil.virtual_memory().percent,

        "disk_percent":
        psutil.disk_usage("/").percent,

        "boot_time":
        psutil.boot_time()
    }