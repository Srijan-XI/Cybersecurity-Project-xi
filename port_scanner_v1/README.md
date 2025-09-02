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
├── requirements.txt           # Dependencies (standard library only)
├── main.py                    # Entry point for the scanner
├── config.py                  # Configuration settings
│
└── scanner/
    ├── __init__.py            # Makes 'scanner' a package
    ├── port_scanner.py        # Core scanning logic
    ├── service_identifier.py  # Service identification functions
    └── utils.py               # Utility functions
```

## Usage 💻

### Interactive Mode

Run the scanner without arguments for interactive mode:

```bash
python3 main.py
```

Example session:
```
Enter target IP address or hostname: 192.168.1.1
Enter start port (default: 1): 20
Enter end port (default: 1024): 1024

📡 Target: 192.168.1.1
🔢 Port Range: 20-1024
🧵 Threads: 100

Proceed with scan? (y/n): y

Starting port scan on 192.168.1.1
Scanning ports 20-1024
Using 100 threads

Port 22: Open (SSH)
Port 80: Open (HTTP)
Port 443: Open (HTTPS)
Progress: 100.0% (1005/1005)

Scan completed in 3.45 seconds
Scanned 1005 ports
Found 3 open ports

--- Scan Summary ---
Port 22: Open (SSH)
Port 80: Open (HTTP)  
Port 443: Open (HTTPS)
```

### Command Line Mode

#### Basic Usage
```bash
# Scan default ports on target
python3 main.py -t 192.168.1.1

# Scan specific port range
python3 main.py -t google.com -s 80 -e 443

# Quick scan of common ports only
python3 main.py -t 127.0.0.1 --quick

# Custom thread count
python3 main.py -t 192.168.1.1 -s 1 -e 1000 --threads 200
```

#### Command Line Options
```
-t, --target         Target IP address or hostname
-s, --start-port     Start port (default: 1)
-e, --end-port       End port (default: 1024)  
--threads            Number of threads (default: 100)
-q, --quick          Quick scan common ports only
--version            Show version information
-h, --help           Show help message
```

### Advanced Examples

```bash
# Scan web ports only
python3 main.py -t example.com -s 80 -e 80

# Scan all well-known ports with high thread count
python3 main.py -t 192.168.1.100 -s 1 -e 1023 --threads 500

# Quick scan localhost
python3 main.py -t localhost --quick
```

## Configuration ⚙️

Edit `config.py` to customize default settings:

```python
# Default port range
DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 1024

# Threading configuration  
DEFAULT_THREAD_COUNT = 100

# Timeout settings (seconds)
SOCKET_TIMEOUT = 1
```

## Workflow Explanation 🔄

### 1. User Input Phase
- Get target IP/hostname from user
- Get port range (start and end ports)
- Validate all inputs

### 2. Input Validation
- **IP Validation**: Uses `ipaddress` library to validate IPv4/IPv6
- **Hostname Resolution**: Resolves hostnames to IP addresses  
- **Port Range Validation**: Ensures ports are 1-65535 and start ≤ end

### 3. Scanning Process
- Creates thread pool with configurable number of workers
- Each thread scans ports from a shared queue
- Uses socket connections to test port accessibility
- Collects results in thread-safe manner

### 4. Service Identification  
- Maps port numbers to known services (HTTP, SSH, FTP, etc.)
- Provides security warnings for risky services
- Returns "Unknown Service" for unrecognized ports

### 5. Result Display
- Shows real-time progress updates
- Displays scan summary with open ports and services
- Provides security alerts where applicable

## Service Detection 🔍

The scanner identifies 40+ common services including:

| Port | Service | Description |
|------|---------|-------------|
| 21   | FTP     | File Transfer Protocol |
| 22   | SSH     | Secure Shell |
| 23   | Telnet  | Unencrypted remote login |
| 25   | SMTP    | Email transmission |
| 53   | DNS     | Domain Name System |
| 80   | HTTP    | Web traffic |
| 443  | HTTPS   | Secure web traffic |
| 3389 | RDP     | Remote Desktop Protocol |

## Security Features 🔒

- **Security Warnings**: Identifies potentially risky open services
- **Safe Timeouts**: Prevents hanging connections
- **Graceful Interruption**: Handles Ctrl+C safely
- **Input Validation**: Prevents invalid targets and ranges

## Performance 🚀

- **Multi-threading**: Configurable thread count (default: 100)
- **Efficient Scanning**: Typically scans 1000+ ports in under 5 seconds
- **Memory Efficient**: Minimal memory footprint
- **Progress Tracking**: Real-time scan progress

## Limitations ⚠️

- TCP ports only (no UDP scanning)
- Basic service identification (no deep packet inspection)
- No stealth scanning options
- Requires network connectivity to target

## Examples 📝

### Scan Local Machine
```bash
python3 main.py -t 127.0.0.1 -s 1 -e 100
```

### Scan Remote Server  
```bash
python3 main.py -t example.com --quick
```

### Custom Port Range
```bash
python3 main.py -t 192.168.1.1 -s 8000 -e 9000
```

## Troubleshooting 🔧

### Common Issues

1. **Permission Denied**: Some systems require elevated privileges for certain ports
2. **Firewall Blocking**: Firewalls may block scan attempts
3. **Network Timeout**: Increase timeout in config.py for slow networks
4. **Too Many Threads**: Reduce thread count if experiencing connection issues

### Performance Tips

- Use fewer threads (50-200) for better stability
- Scan smaller port ranges for faster results  
- Use quick scan mode for common ports only
- Close other network applications during scanning

## Contributing 🤝

Feel free to contribute improvements:
1. Fork the repository
2. Create feature branch
3. Add tests for new functionality
4. Submit pull request

## License 📄

This project is open source. Feel free to use and modify as needed.

## Disclaimer ⚖️

This tool is for educational and legitimate security testing purposes only. Always ensure you have permission to scan target systems. Unauthorized port scanning may be illegal in your jurisdiction.

---

**Happy Scanning! 🎯**
