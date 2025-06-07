import logging
import os
import subprocess

from pathlib import Path
from datetime import datetime


def reboot():
    logging.info("Rebooting...")
    os.system("sudo /usr/bin/reboot")


def shutdown():
    logging.info("Shutting down...")
    os.system("sudo /usr/bin/shutdown now")


def screenshot():
    if not os.path.exists("temp"):
        os.mkdir("temp")

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    screenshot_path = Path(os.path.join("temp", f"screenshot-{time}.png"))

    result = subprocess.run([
        "spectacle",
        "-n",
        "-b",
        "-o", str(screenshot_path)
    ], check=True)

    if result.returncode != 0:
        raise Exception("Не удалось сделать скриншот через spectacle")

    return screenshot_path


def delete_screenshot(screenshot_path: Path):
    screenshot_path.unlink(missing_ok=True)
    os.rmdir("temp")
