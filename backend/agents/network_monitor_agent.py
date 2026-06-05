import psutil


async def network_monitor_agent():

    net = psutil.net_io_counters()

    return {

        "bytes_sent":
        net.bytes_sent,

        "bytes_received":
        net.bytes_recv,

        "packets_sent":
        net.packets_sent,

        "packets_received":
        net.packets_recv
    }