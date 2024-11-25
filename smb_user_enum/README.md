# SMB Enumeration Script

## Description
A Bash script to enumerate SMB shares on a target system, with or without a known domain/workgroup. It uses the `smbclient` tool.

## Features
- Lists available SMB shares on a target.
- Allows specifying a domain/workgroup or leaving it blank.

## How to Use
1. Ensure `smbclient` is installed on your system.
2. Run the script:
   ```bash
   ./smb_enum.sh
   ```
3. Enter the target IP and optional domain/workgroup when prompted.

## Requirements
- Bash
- `smbclient`

## Example Output
```plaintext
Sharename       Type      Comment
IPC$            IPC       IPC Service (Shared Resources)
Documents       Disk      Shared Documents Folder
```
```
