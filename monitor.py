import platform
import os
import psutil
import socket
from datetime import datetime
import logging

logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)



def get_system_info():
    print("Operating System:", platform.system())
    print("Machine:", platform.machine())
    print("CPU Cores:", os.cpu_count())

def get_cpu_info():
    cpu = psutil.cpu_percent(interval=1)
    print("CPU Usage:", cpu, "%")

    if cpu >= 80:
        print("CPU Status: WARNING")
        return False, cpu

    else:
        print("CPU Status: OK")
        return True, cpu


def get_memory_info():
    memory = psutil.virtual_memory()
    print("RAM Usage:", memory.percent, "%")

    if memory.percent >= 80:
        print("RAM Status: WARNING")
        return False, memory.percent
    else:
        print("RAM Status: OK")
        return True, memory.percent


def get_disk_info():
    disk = psutil.disk_usage("/")
    print("Disk Usage:", disk.percent, "%")

    if disk.percent >= 80:
        print("Disk Status: WARNING")
        return False, disk.percent
    else:
        print("Disk Status: OK")
        return True, disk.percent

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

print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


logging.info("System monitoring started")

get_system_info()

cpu_ok, cpu_usage = get_cpu_info()

ram_ok, ram_usage = get_memory_info()
disk_ok, disk_usage = get_disk_info()
internet_ok = check_internet()

print()
print("SYSTEM MONITOR")
print("----------------")

if cpu_ok and ram_ok and disk_ok and internet_ok:
    print("System Status: HEALTHY")
else:
    print("System Status: WARNING")

logging.info(f"CPU Usage: {cpu_usage}%")
logging.info(f"RAM Usage: {ram_usage}%")
logging.info(f"Disk Usage: {disk_usage}%")

if internet_ok:
    logging.info("Internet: Connected")
else:
    logging.warning("Internet: Not Connected")

if cpu_ok and ram_ok and disk_ok and internet_ok:
    logging.info("System status: HEALTHY")
else:
    logging.warning("System status: WARNING")




