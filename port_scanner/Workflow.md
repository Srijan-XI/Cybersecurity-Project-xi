# 🚀 Port Scanner — Workflow Explanation
## 1. User Input Phase:
The user runs the tool via:
```
python -m port_scanner.main
```
Prompted to enter:
```
Target IP Address (example: 192.168.1.1 or 127.0.0.1)

Start Port (default: 1)

End Port (default: 1024)
```

## 2. Input Validation (Using ```utils.py```):
IP Address Validation:

Checks if the provided IP is a valid IPv4/IPv6 address using Python’s ipaddress library.

If invalid → program prints an error and exits.

Port Range Validation:

Confirms port range is between 1 and 65535 and that start port ≤ end port.

If invalid → program prints an error and exits.

## 3. Scanning Process (Using ```port_scanner.py```):
- For every port in the range:

    - A new thread is created to scan that specific port to ensure faster, parallel processing.

    - Each thread:

        - Tries to connect to the port using ```socket```.

        - If the connection succeeds (return code 0), the port is considered open.

## 4. Service Identification (Using ```service_identifier.py```):
- If a port is open:

  - The scanner checks if this port number corresponds to a known service (HTTP, FTP, SSH, etc.).

  - If found, service name is attached.

  - Otherwise, returns "Unknown Service".

## 5. Result Collection:
- All open ports along with identified services are appended to a result list.

- Threads are carefully managed:

  - Max number of threads controlled via DEFAULT_THREAD_COUNT (from config.py).

## 6. Display Output:
- After scanning completes:

   - A neat summary table of all open ports and their respective services is printed.

### Example:
```
--- Scan Summary ---
Port 22: Open (SSH)
Port 80: Open (HTTP)
Port 443: Open (HTTPS)
```

## ⚙️ Technologies Used:

Python Standard Libraries Only:

```socket, threading, ipaddress, sys, os```