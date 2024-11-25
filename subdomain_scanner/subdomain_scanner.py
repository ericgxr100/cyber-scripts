import requests

def scan_subdomains(domain, subdomain_list):
    with open(subdomain_list, 'r') as file:
        subdomains = file.readlines()
    
    print(f"Scanning subdomains for {domain}...\n")
    for subdomain in subdomains:
        subdomain = subdomain.strip()
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(f"[+] Found: {url}")
        except requests.ConnectionError:
            pass

if __name__ == "__main__":
    target_domain = input("Enter the target domain: ")
    subdomain_file = input("Enter the subdomain file path: ")
    scan_subdomains(target_domain, subdomain_file)
