import platform
import socket
import psutil
import colorama
from colorama import Fore

colorama.init()

def get_system_info():
    system = platform.system()
    release = platform.release()
    architecture = platform.architecture()[0]
    hostname = socket.gethostname()
    cpu_cores = psutil.cpu_count(logical=False)
    total_memory = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Convert to GB

    return {
        "System": system,
        "Release": release,
        "Architecture": architecture,
        "Hostname": hostname,
        "CPU Cores": cpu_cores,
        "Total Memory": f"{total_memory} GB",
    }

def print_system_info(info):
    for key, value in info.items():
        print(Fore.GREEN + f"{key}: {value}")

    print("""
    .--.
   |o_o |
   |:_/ |
  //   \ \\
 (|     | )
/'\_   _/`\\
\___)=(___/ 
""")

if __name__ == "__main__":
    system_info = get_system_info()
    print_system_info(system_info)
