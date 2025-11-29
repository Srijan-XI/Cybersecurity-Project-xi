# Port Scanner (Like Nmap) 🔍

A simple yet efficient multi-threaded port scanner to scan open ports on remote machines. This tool supports multi-threaded scanning, port range selection, and basic service identification using only Python standard libraries.

## Features ✨

- **Multi-threaded scanning** - Fast parallel port scanning
- **Port range selection** - Scan specific port ranges or individual ports
- **Service identification** - Identifies common services running on open ports
- **Interactive mode** - User-friendly interactive interface
- **Command line interface** - Scriptable command line options
- **Quick scan mode** - Fast scanning of common ports only
- **Security warnings** - Alerts for potentially risky open services
- **Progress tracking** - Real-time scan progress updates
- **Hostname resolution** - Supports both IP addresses and hostnames

## Requirements 📋

- Python 3.6 or higher
- No external dependencies (uses only Python standard libraries)

### Libraries Used:
- `socket` - Network connections
- `threading` - Multi-threading support
- `ipaddress` - IP address validation
- `queue` - Thread-safe queues
- `argparse` - Command line argument parsing
- `time` - Timing and delays
- `signal` - Signal handling (Ctrl+C)

## Installation 🚀

1. Clone or download the project files
2. Ensure Python 3.6+ is installed
3. No additional packages needed!

```bash
# Check Python version
python3 --version

# Navigate to project directory  
cd port_scanner
```

## File Structure 📁

```
port_scanner/
│
├── README.md                  # Project documentation
├── requirements.txt           # Required libraries (none needed)
├── main.py                    # Entry point for the scanner
├── config.py                  # Configuration settings (ports, threads, etc.)
├── demo.py                    # Demo script with examples
├── Workflow.md                # Development workflow documentation
├── scanner/
│   ├── __init__.py            # Makes 'scanner' a package
│   ├── port_scanner.py        # Core scanning logic with PortScanner class
│   ├── service_identifier.py  # Service identification and security info
│   └── utils.py               # Utility functions (validation, hostname resolution)
└── __pycache__/               # Python bytecode cache
```

## Usage 📖

### Interactive Mode
```bash
python main.py
```

### Command Line Mode
```bash
# Basic scan with default ports
python main.py -t 192.168.1.1

# Scan specific port range
python main.py -t google.com -s 80 -e 443

# Quick scan of common ports only
python main.py -t 127.0.0.1 --quick

# Custom thread count
python main.py -t 192.168.1.100 --threads 50
```

### Command Line Options
- `-t, --target` - Target IP address or hostname
- `-s, --start-port` - Start port (default: 1)
- `-e, --end-port` - End port (default: 1024)
- `--threads` - Number of threads (default: 100)
- `-q, --quick` - Quick scan of common ports only
- `--version` - Show version information

## Examples 💡

### Interactive Mode Example:
```
    ╔═══════════════════════════════════════╗
    ║           PORT SCANNER v1.0           ║
    ║      Multi-threaded Port Scanner      ║
    ║         Like Nmap but Simple          ║
    ╚═══════════════════════════════════════╝

🔍 Interactive Mode
========================================
Enter target IP address or hostname: google.com
Resolved google.com to 142.250.185.46
Enter start port (default: 1): 80
Enter end port (default: 1024): 443

📡 Target: 142.250.185.46
🔢 Port Range: 80-443
🧵 Threads: 100

Proceed with scan? (y/n): y
```

### Command Line Example:
```bash
$ python main.py -t 192.168.1.1 -s 20 -e 1000

📡 Target: 192.168.1.1
🔢 Port Range: 20-1000
🧵 Threads: 100

Starting port scan on 192.168.1.1
Scanning ports 20-1000
Using 100 threads

Port 22: Open (SSH)
Port 80: Open (HTTP)
Port 443: Open (HTTPS)
Progress: 100.0% (981/981)

Scan completed in 2.34 seconds
Scanned 981 ports
Found 3 open ports

--- Scan Summary ---
Port 22: Open (SSH)
Port 80: Open (HTTP)
Port 443: Open (HTTPS)
```

## Configuration ⚙️

Edit `config.py` to customize default settings:

```python
# Default port range
DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 1024

# Threading configuration
DEFAULT_THREAD_COUNT = 100

# Timeout settings (in seconds)
SOCKET_TIMEOUT = 1
DEFAULT_END_PORT = 1024
DEFAULT_THREAD_COUNT = 100
