# Port Scanner (Like Nmap)

## Description
A simple yet efficient port scanner to scan open ports on remote machines. Supports multi-threaded scanning, port range selection, and basic service identification.

## Features
- Multi-threaded scanning
- Port range selection
- Service identification based on common ports

## Requirements
- Python 3.x

Libraries used:
- socket
- threading
- ipaddress

## File Structure

```
port_scanner/
│
├── README.md                  # Project overview and usage instructions
├── requirements.txt           # Required libraries
├── main.py                    # Entry point for the scanner
├── scanner/
│   ├── __init__.py            # Makes 'scanner' a package
│   ├── port_scanner.py        # Core scanning logic
│   ├── service_identifier.py  # Service identification functions
│   └── utils.py               # Utility functions (IP validation, port range checks, etc.)
└── config.py                  # Configuration settings (default port range, thread count, etc.)
```
## Example
```
Enter target IP: 192.168.1.1
Enter start port: 20
Enter end port: 1024
Scanning...
Port 22: Open (SSH)
Port 80: Open (HTTP)
```

---

## 🔧 **Implementation**

### **config.py**
```python
DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 1024
DEFAULT_THREAD_COUNT = 100
