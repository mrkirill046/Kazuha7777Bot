import subprocess


def _run_command(command: str) -> str:
    try:
        return subprocess.check_output(
            command, shell=True, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "N/A"


def get_os_name() -> str:
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("PRETTY_NAME="):
                    full = line.strip().split("=", 1)[1].strip('"')
                    parts = full.split()

                    if len(parts) >= 2:
                        return (
                            f"{parts[0]} {parts[1]} {' '.join(parts[2:])}"
                            if len(parts) > 2
                            else f"{parts[0]} {parts[1]}"
                        )

                    return full
    except Exception:
        pass

    return "NixOS"


def get_uptime() -> str:
    try:
        with open("/proc/uptime") as f:
            seconds = int(float(f.read().split()[0]))

        days, remainder = divmod(seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, _ = divmod(remainder, 60)

        parts = []

        if days:
            parts.append(f"{days}d")
        if hours:
            parts.append(f"{hours}h")

        parts.append(f"{minutes}m")

        return " ".join(parts)
    except Exception:
        return "N/A"


def get_kernel() -> str:
    return _run_command("uname -r")


def get_hostname() -> str:
    return _run_command("hostname")


def get_system_packages() -> str:
    count = _run_command("nix-store -q --requisites /run/current-system/sw | wc -l")
    return count
