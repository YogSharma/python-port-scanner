#!/usr/bin/python3
# ^^^ Shebang line - tells the system to use Python 3 to run this script

import sys
import socket
from datetime import datetime

"""
Simple TCP Port Scanner
----------------------
Scans a target host for open TCP ports in a small range (50–84).
Uses connect() method → most reliable way to detect open ports.

Usage: python3 scanner.py <hostname_or_ip>
Example: python3 scanner.py scanme.nmap.org
         python3 scanner.py 45.33.32.156
"""

# ────────────────────────────────────────────────
#          INPUT VALIDATION & TARGET RESOLUTION
# ────────────────────────────────────────────────
if len(sys.argv) != 2:
    print("Invalid number of arguments.")
    print("Syntax : python3 scanner.py <target>")
    print("Example: python3 scanner.py 192.168.1.1")
    print("         python3 scanner.py example.com")
    sys.exit(1)

try:
    # Convert hostname to IP address (IPv4)
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Error: Hostname could not be resolved.")
    sys.exit(1)

# ────────────────────────────────────────────────
#                 BANNER / START INFO
# ────────────────────────────────────────────────
print("=" * 50)
print(f"      Target IP   : {target}")
print(f"      Started at  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"      Scanning... (ports 50 → 84)")
print("=" * 50)

# ────────────────────────────────────────────────
#                   MAIN SCANNING LOOP
# ────────────────────────────────────────────────
try:
    # Very narrow range used here (mostly for demonstration)
    # Common small ports usually scanned: 21–25, 80, 443, 3306, etc.
    for port in range(50, 85):
        # Create new TCP socket for each port attempt
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set timeout (very important!)
        # Without timeout → script can hang forever on filtered ports
        socket.setdefaulttimeout(1)     # 1 second timeout
        
        # connect_ex() returns 0 on success, error code otherwise
        # This is preferred over connect() because it doesn't raise exception
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[OPEN]  Port {port:4d} is open")
        # Uncomment the next line if you want to see closed ports too
        # else:
        #     print(f"[CLOSED] Port {port:4d}")

        s.close()   # Always close the socket

except KeyboardInterrupt:
    print("\n[!] Scan interrupted by user (Ctrl+C)")
    print("Exiting gracefully...")
    sys.exit(0)

except socket.gaierror:
    print("Error: Hostname could not be resolved.")
    sys.exit(1)

except socket.error as e:
    print(f"Error: Cannot connect to target ({e})")
    sys.exit(1)

# ────────────────────────────────────────────────
#                     FINISHED
# ────────────────────────────────────────────────
print("\n" + "-" * 50)
print("Scan completed.")
print("-" * 50)
