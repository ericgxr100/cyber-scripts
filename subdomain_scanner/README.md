# Subdomain Scanner

## Description
A Python script to identify active subdomains for a given domain using a provided wordlist.

## Features
- Scans subdomains by appending prefixes from a wordlist.
- Checks for valid responses from each subdomain.

## How to Use
1. Prepare a wordlist file (e.g., `subdomains.txt`).
2. Run the script:
   ```bash
   python subdomain_scanner.py
   ```
3. Provide the target domain and wordlist file when prompted.

## Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)

## Example Output
```plaintext
Scanning subdomains for example.com...

[+] Found: http://blog.example.com
[+] Found: http://shop.example.com
```
