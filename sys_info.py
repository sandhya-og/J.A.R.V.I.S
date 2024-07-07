import psutil
import platform
import time
from datetime import datetime
from plyer import notification

def System_Information():
    
    def get_size(bytes, suffix="B"):
        factor = 1024
        
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    print( "\n", "=" * 40, "System Information", "=" * 40, "\n")
    
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"IP-Address: {psutil.net_if_addrs()['Wi-Fi'][1].address}")
    print(f"mac-address: {psutil.net_if_addrs()['Wi-Fi'][0].address}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    
    # Boot Time
    print("\n", "=" * 40, "Boot Time", "=" * 40, "\n")
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    
    #CPU information
    print("\n", "=" * 40, "CPU Info", "=" * 40, "\n")
    
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    
    # Memory Information
    print("\n", "=" * 40, "Memory Information", "=" * 40, "\n")
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("\n", "=" * 20, "SWAP", "=" * 20, "\n")
    
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")
    
    # Disk Information
    print("\n", "=" * 40, "Disk Information", "=" * 40, "\n")
    print("Partitions and Usage:")
    
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"\n=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
        
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"\nTotal read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}\n")
    
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"\nTotal Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}\n")
    
    return 0

def battery():
    battery = psutil.sensors_battery()
    while True:
        percent = battery.percent
        notification.notify (
            title='Battery Percentage',
            message=str(percent) + '% Battery remaining',
            timeout=10
        )
        time.sleep(10)
        break