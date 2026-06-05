import psutil


async def resource_manager_agent():

    vm = psutil.virtual_memory()

    disk = psutil.disk_usage("/")

    return {

        "memory_total_gb":
        round(
            vm.total / (1024**3),
            2
        ),

        "memory_used_gb":
        round(
            vm.used / (1024**3),
            2
        ),

        "memory_available_gb":
        round(
            vm.available / (1024**3),
            2
        ),

        "disk_total_gb":
        round(
            disk.total / (1024**3),
            2
        ),

        "disk_used_gb":
        round(
            disk.used / (1024**3),
            2
        )
    }