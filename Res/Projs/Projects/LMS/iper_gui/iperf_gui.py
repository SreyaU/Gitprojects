''''This script is used to create iperf GUI version

#--------------
# Logic Flow
#--------------
# OS specific operations
# 1) Check iperf installed/not
# 2) Install if not already installed
# 3) confirm installation and version
# 4) take iperf command - create a gui for entering command
# 5) Create UI Jperf clone using tk
# 6) create graphical interface with matplotlib
# 7) create timestamped files on rerun again.

'''
import platform
import utils

#Check OS type
os_name = platform.system()
print(f"Operating System: {os_name}")

if os_name == "Windows":
    print("Running on Windows")
elif os_name == "Linux":
    print("Running on Linux")
elif os_name == "Darwin":
    print("Running on macOS")
else:
    print("Unknown OS")

#Steps 1-3
utils.check_iperf()

#Steps 4-5
utils.start_ui()






