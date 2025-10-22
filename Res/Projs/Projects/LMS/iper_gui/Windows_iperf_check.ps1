
Write-Host "Checking for iperf3..."

$iperfPath = Get-Command iperf3.exe -ErrorAction SilentlyContinue

if ($iperfPath) {
    Write-Host "iperf3 is already installed."
    iperf3.exe --version
} else {
    Write-Host "iperf3 not found. Installing via Chocolatey..."
    if (!(Get-Command choco.exe -ErrorAction SilentlyContinue)) {
        Write-Host "Chocolatey not found. Please install Chocolatey first."
    } else {
        choco install iperf3 -y
    }
}
