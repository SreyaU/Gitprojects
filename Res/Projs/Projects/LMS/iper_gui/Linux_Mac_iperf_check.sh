
#!/bin/bash

echo "Checking for iperf3..."

if command -v iperf3 &> /dev/null
then
    echo "iperf3 is already installed."
    iperf3 --version
else
    echo "iperf3 not found. Installing..."

    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update && sudo apt install -y iperf3
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install iperf3
    else
        echo "Unsupported OS for this script."
    fi
