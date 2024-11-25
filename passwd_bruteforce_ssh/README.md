# SSH Bruteforce Script

## Description
A Python script to perform brute force attacks against SSH services using a username and a password list.

## Features
- Automates testing of multiple passwords for a given username.
- Outputs valid credentials if found.

## How to Use
1. Prepare a password list file (e.g., `passwords.txt`).
2. Run the script:
   ```bash
   python ssh_bruteforce.py
   ```
3. Provide the target IP, username, and password file when prompted.

## Requirements
- Python 3.x
- `paramiko` library (install with `pip install paramiko`)

## Example Output
```plaintext
Target IP: 192.168.1.10
Username: admin
Password file: passwords.txt

[-] Failed: admin:password123
[+] Found credentials: admin:securepass!
```
