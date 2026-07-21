from utils.constants import config
from utils.menu import create_menu
from utils.modules import load_all_modules
from utils.owner import OwnerOnlyMiddleware
from utils.pc_manage import delete_screenshot, reboot, screenshot, shutdown
from utils.pc_status import (
    get_hostname,
    get_kernel,
    get_os_name,
    get_system_packages,
    get_uptime,
)
from utils.state import CustomCommand

registered_commands: list[dict] = []

__all__ = [
    "load_all_modules",
    "config",
    "create_menu",
    "get_hostname",
    "get_kernel",
    "get_uptime",
    "get_system_packages",
    "get_os_name",
    "reboot",
    "shutdown",
    "screenshot",
    "delete_screenshot",
    "CustomCommand",
    "OwnerOnlyMiddleware",
    "registered_commands",
]
