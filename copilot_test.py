import os
import platform
import subprocess

def get_system_uptime():
    system = platform.system()
    if system == "Windows":
        # Use 'net stats srv' to get uptime (works only if server service is running)
        try:
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    return f"System uptime (Windows): {line}"
        except Exception as e:
            return f"Unable to fetch uptime on Windows: {e}"
    elif system == "Linux":
        try:
            with open("/proc/uptime", "r") as f:
                seconds = float(f.readline().split()[0])
                hours = int(seconds // 3600)
                minutes = int((seconds % 3600) // 60)
                return f"System uptime (Linux): {hours} hours, {minutes} minutes"
        except Exception as e:
            return f"Unable to fetch uptime on Linux: {e}"
    elif system == "Darwin":
        try:
            output = subprocess.check_output("uptime", shell=True, text=True)
            return f"System uptime (macOS): {output.strip()}"
        except Exception as e:
            return f"Unable to fetch uptime on macOS: {e}"
    else:
        return "Unsupported operating system for uptime fetch."

if __name__ == "__main__":
    print(get_system_uptime())
