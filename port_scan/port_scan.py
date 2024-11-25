import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip, port))
            print(f"[+] Port {port} is open.")
    except:
        pass

def main():
    ip = input("Enter the IP address to scan: ")
    ports = range(1, 65536) 
    print(f"Scanning {ip}...\n")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, ip, port)

if __name__ == "__main__":
    main()
