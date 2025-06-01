import subprocess
import platform

def get_os_name() -> str:
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("PRETTY_NAME="):
                    return line.strip().split("=")[1].strip('"')
    except Exception:
        return platform.system()

    return "Arch Linux"

def get_uptime():
    return subprocess.check_output("uptime -p", shell=True).decode().strip()

def get_kernel():
    return subprocess.check_output("uname -r", shell=True).decode().strip()

def get_hostname():
    return subprocess.check_output("hostname", shell=True).decode().strip()

def get_package_count():
    return subprocess.check_output("pacman -Q | wc -l", shell=True).decode().strip()

def get_update_count():
    return subprocess.check_output("checkupdates | wc -l", shell=True).decode().strip()
