import platform
import os
import psutil
import socket


def get_system_info():
    print("Operating System:", platform.system())
    print("Machine:", platform.machine())
    print("CPU Cores:", os.cpu_count())


def get_memory_info():
    memory = psutil.virtual_memory()
    print("RAM Usage:", memory.percent, "%")


def get_disk_info():
    disk = psutil.disk_usage("/")
    print("Disk Usage:", disk.percent, "%")


def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Internet: Connected")
    except OSError:
        print("Internet: Not Connected")


get_system_info()
get_memory_info()
get_disk_info()
check_internet()

