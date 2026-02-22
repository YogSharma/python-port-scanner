# Simple TCP Port Scanner

Small Python script that checks which TCP ports are open on a given host.

Educational project / first steps with network programming in Python.

**Important**  
Only use this script on targets you own or have explicit permission to scan.

## What it does

- Takes a hostname or IP address as argument
- Tries to connect to ports 50–84 (small range – easy to change)
- Shows which ports accept connections (are open)
- Has basic timeout and error handling
- Shows nice starting banner with timestamp

## Requirements

- Python 3 (any recent version)
- No extra packages needed

## How to use

```bash
# Basic usage
python3 scanner.py TARGET

# Examples:
python3 scanner.py scanme.nmap.org
python3 scanner.py 127.0.0.1
python3 scanner.py 192.168.1.254

#Example Output
..................................................
Scanning target 45.33.32.156
Time started: 2025-02-22 14:35:12.345678
..................................................
Port 80 is open

Scan finished.
