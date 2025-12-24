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
    os.makedirs("temp", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    screenshot_path = Path("temp") / f"screenshot-{timestamp}.png"

    grimblast_path = Path("/usr/bin/grimblast")

    if not grimblast_path.exists():
        raise FileNotFoundError(f"grimblast not found at: {grimblast_path}")

    result = subprocess.run([
        str(grimblast_path),
        "copysave",
        "output",
        str(screenshot_path)
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"grimblast error: {result.stderr.strip()}")

    if not screenshot_path.exists():
        raise RuntimeError("grimblast did not create the screenshot file")

    return screenshot_path


def delete_screenshot(screenshot_path: Path):
    screenshot_path.unlink(missing_ok=True)

    try:
        os.rmdir("temp")
    except OSError:
        pass
