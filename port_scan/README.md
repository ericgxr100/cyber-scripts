# Port Scanner

## Description
A Python-based port scanner that identifies open ports on a given target IP. The script uses multithreading to improve scanning speed.

## Features
- Scans all 65,535 TCP ports.
- Uses multithreading for faster scans.
- Provides a simple and interactive input mechanism.

## How to Use
1. Run the script:
   ```bash
   python port_scanner.py
   ```
2. Enter the target IP address when prompted.
3. The script will output a list of open ports.

## Requirements
- Python 3.x
- `concurrent.futures` (comes pre-installed with Python 3.x)

## Example Output
   ```plaintext
Scanning 192.168.1.1...

[+] Port 22 is open.
[+] Port 80 is open.
[+] Port 443 is open.
   ```


