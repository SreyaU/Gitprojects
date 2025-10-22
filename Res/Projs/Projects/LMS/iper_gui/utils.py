import platform
import subprocess
import shutil
import sys

def check_iperf():
    """Check if iperf3 is installed; install it if not present."""
    if shutil.which("iperf3"):
        print("iperf3 is already installed.")
        subprocess.run(["iperf3", "--version"], check=False)
        return

    os_type = platform.system()
    print(f"iperf3 not found. Attempting installation on {os_type}...")

    try:
        if os_type == "Linux":
            subprocess.run(["sudo", "apt", "update", "-qq"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "iperf3"], check=True)
        elif os_type == "Darwin":  # macOS
            subprocess.run(["brew", "install", "iperf3"], check=True)
        elif os_type == "Windows":
            if shutil.which("choco"):
                subprocess.run(["choco", "install", "iperf3", "-y"], check=True)
            else:
                print("Chocolatey is not installed. Install it from: https://chocolatey.org/install .Or:\nInstall iperf3 for Windows from: https://iperf.fr/iperf-download.php and Complete SetUp.")
                sys.exit(1)
        else:
            print(f"Unsupported OS: {os_type}")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Installation failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def start_ui():
    """Start iperf GUI once installation """
    subprocess.run['python','gui.py']
