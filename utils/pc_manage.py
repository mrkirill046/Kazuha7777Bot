import logging
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path


def reboot() -> None:
    logging.info("Rebooting...")
    subprocess.run(["systemctl", "reboot"])


def shutdown() -> None:
    logging.info("Shutting down...")
    subprocess.run(["systemctl", "poweroff"])


def screenshot() -> Path:
    os.makedirs("temp", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    screenshot_path = Path("temp") / f"screenshot-{timestamp}.png"

    result = subprocess.run(
        ["niri", "msg", "action", "screenshot-screen", "--path", str(screenshot_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(f"niri screenshot error: {result.stderr.strip()}")

    for _ in range(20):
        if screenshot_path.exists():
            return screenshot_path
        time.sleep(0.1)

    raise RuntimeError("Screenshot file was not created")


def delete_screenshot(screenshot_path: Path) -> None:
    screenshot_path.unlink(missing_ok=True)

    try:
        os.rmdir("temp")
    except OSError:
        pass
