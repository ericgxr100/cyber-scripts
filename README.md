# Security and Pentesting Tools

This repository contains a collection of scripts developed for various tasks in cybersecurity and penetration testing. Each tool is designed to perform a specific function, from user enumeration to metadata analysis. Below is a detailed description of each included script.

---

## Table of Contents

1. [Metadata Extractor](#metadata-extractor)
2. [Password Bruteforce SSH](#password-bruteforce-ssh)
3. [Port Scanner](#port-scanner)
4. [SMB User Enumerator](#smb-user-enumerator)
5. [Subdomain Scanner](#subdomain-scanner)

---

## Scripts

### 1. Metadata Extractor
**Location:** `metadata_extractor/`  
**Description:**  
This script extracts embedded metadata from files, such as documents, images, and PDFs. Metadata can reveal sensitive information like usernames, software used, and modification dates.  
**Common Use Cases:**  
- Identify hidden details in shared documents.  
- Detect potential attack vectors through metadata.

---

### 2. Password Bruteforce SSH
**Location:** `passwd_bruteforce_ssh/`  
**Description:**  
A tool to perform brute-force attacks on SSH servers using user and password lists. It is ideal for controlled penetration tests in authorized environments.  
**Warning:**  
This script must only be used with explicit permission from the system owner.

---

### 3. Port Scanner
**Location:** `port_scan/`  
**Description:**  
A port scanner designed to identify active services on a target host. It detects open and closed ports and provides valuable insights for security assessments.  
**Features:**  
- Supports scanning custom port ranges.  
- Adjustable speed options for quick or detailed scans.

---

### 4. SMB User Enumerator
**Location:** `smb_user_enum/`  
**Description:**  
A tool to enumerate users and shared resources on SMB servers (file-sharing protocol). This helps identify possible misconfigurations or exposed users.  
**Common Use Cases:**  
- Auditing Windows systems or networks using SMB.

---

### 5. Subdomain Scanner
**Location:** `subdomain_scanner/`  
**Description:**  
A script to discover subdomains associated with a main domain. Useful for mapping the scope of a target during penetration testing.  
**Features:**  
- Supports multiple data sources for discovery.  
- Export options for results.

---

## Requirements
Some scripts require additional tools or libraries. Check the individual README files inside each folder for details on dependencies and configurations.

---

## Disclaimer
These tools are intended for authorized security testing only. Unauthorized use of these tools may violate local or international laws.

---

## Contributions
If you have ideas to improve these tools, feel free to contribute! Open a pull request or create an issue with your suggestions.

---

## Contact
For questions or inquiries, you can reach out via my GitHub profile.
