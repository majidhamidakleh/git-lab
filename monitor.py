import platform
import os
import psutil
import socket


def get_system_info():
    print("Operating System:", platform.system())
    print("Machine:", platform.machine())
    print("CPU Cores:", os.cpu_count())

def get_cpu_info():
    cpu = psutil.cpu_percent(interval=1)
    print("CPU Usage:", cpu, "%")

    if cpu >= 80:
        print("CPU Status: WARNING")
        return False
    else:
        print("CPU Status: OK")
        return True


def get_memory_info():
    memory = psutil.virtual_memory()
    print("RAM Usage:", memory.percent, "%")

    if memory.percent >= 80:
        print("RAM Status: WARNING")
    else:
        print("RAM Status: OK")
        return True


def get_disk_info():
    disk = psutil.disk_usage("/")
    print("Disk Usage:", disk.percent, "%")

    if disk.percent >= 80:
        print("Disk Status: WARNING")
    else:
        print("Disk Status: OK")
        return True

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Internet: Connected")
        print("Internet Status: OK")
        return True
    except OSError:
        print("Internet: Not Connected")
        print("Internet Status: WARNING")
        return False

get_system_info()

cpu_ok = get_cpu_info()
ram_ok = get_memory_info()
disk_ok = get_disk_info()
internet_ok = check_internet()

print()
print("SYSTEM MONITOR")
print("----------------")

if cpu_ok and ram_ok and disk_ok and internet_ok:
    print("System Status: HEALTHY")
else:
    print("System Status: WARNING")




