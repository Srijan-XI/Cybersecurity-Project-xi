# Network Packet Sniffer

A simple yet powerful **Network Packet Sniffer** tool built with **Python** and **Scapy** for capturing, analyzing, and saving network packets to `.pcap` files. Designed to run on Windows systems with proper WinPcap/Npcap support.

---

## 🛠️ Features

- Real-time packet sniffing on a selected network interface or all interfaces
- Displays protocol-specific details (TCP, UDP, IP, etc.)
- Saves captured packets into `.pcap` format for further analysis (using tools like Wireshark)
- Customizable packet count and network interface selection
- Robust error handling and graceful shutdown
- Administrator privilege detection and guidance
- Easily extendable and modular file structure

---

## 📋 Requirements

Before running this project, ensure the following are installed:

- **Python 3.8 or higher**
- **Npcap (WinPcap alternative for Windows)**: [Download here](https://nmap.org/npcap/)
- **Administrator privileges** (required for packet capture)

### Python Dependencies:
All required packages are listed in `requirements.txt`:
- `scapy` - Network packet manipulation
- `colorama` - Colored terminal output
- `requests` - HTTP requests
- `pycryptodome` & `pycryptodomex` - Cryptographic functions
- `pyasn1` & `pyasn1-modules` - ASN.1 parsing
- `dnspython` - DNS operations
- `cryptography` - Cryptographic recipes
- `netifaces` - Network interface information
- `pypcapfile` - PCAP file handling
- `scapy-http` - HTTP protocol support for Scapy

Install all dependencies via:

```bash
pip install -r requirements.txt
```
### 📂 Project Structure
```
network_packet_sniffer/
│
├── main.py                      # Entry point to start the sniffer
├── config.py                    # Configuration file (interface and packet count)
├── list_interfaces.py           # List all available network interfaces
├── requirements.txt             # Python package dependencies
├── README.md                    # Project documentation
│
├── packet_sniffer/
│   ├── __init__.py              # Package initialization
│   ├── sniffer.py               # Main sniffing logic with error handling
│   ├── analyzer.py              # Packet analysis and protocol parsing
│   └── pcap_writer.py           # PCAP file writing functionality
│
└── utils/
    ├── __init__.py              # Package initialization
    └── list_interfaces_with_ip.py  # Utility to list interfaces with IP addresses
```
### ⚙️ Configuration (`config.py`)
Update your `config.py` with the correct interface before running:

```python
# config.py
INTERFACE = r'\Device\NPF_{4216ADDE-FA90-420A-AB07-65BEB98F4B23}'  # Replace with your actual interface
PACKET_COUNT = 10  # Number of packets to capture
```

⚠️ **Important:** Get your correct network interface by running:
```bash
python list_interfaces.py
```
or for interfaces with IP addresses:
```bash
python utils/list_interfaces_with_ip.py
```

**Note:** If you set `INTERFACE = None` in config.py, the sniffer will capture packets on all available interfaces.
## 🚀 How to Run

### 1. Clone the Repository:
```bash
git clone https://github.com/Srijan-XI/Cybersecurity-Project-xi.git
cd Cybersecurity-Project-xi/network_packet_sniffer
```

### 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 3. Check Available Network Interfaces:
```bash
# List all interfaces
python list_interfaces.py

# Or list interfaces with IP addresses
python utils/list_interfaces_with_ip.py
```

### 4. Configure the Interface:
Update `config.py` with your desired interface from the list above.

### 5. Run the Packet Sniffer:
```bash
# Make sure to run as Administrator on Windows or with sudo on Linux
python main.py
```

---

## 🖥️ Operating System Specific Instructions

### 🪟 **Windows Instructions**

#### Prerequisites:
1. **Install Npcap:**
   - Download from: [https://nmap.org/npcap/](https://nmap.org/npcap/)
   - During installation, check "Install Npcap in WinPcap API-compatible Mode"
   - Restart your computer after installation

2. **Install Python:**
   - Download from: [https://python.org/downloads/](https://python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

#### Running on Windows:

1. **Open Command Prompt or PowerShell as Administrator:**
   - Press `Win + X` and select "Windows PowerShell (Admin)" or "Command Prompt (Admin)"
   - Or right-click on PowerShell/Command Prompt and select "Run as administrator"

2. **Navigate to project directory:**
   ```powershell
   cd "C:\path\to\Cybersecurity-Project-xi\network_packet_sniffer"
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Check available interfaces:**
   ```powershell
   python list_interfaces.py
   ```
   Example output:
   ```
   Available Network Interfaces:
   1: \Device\NPF_{4216ADDE-FA90-420A-AB07-65BEB98F4B23}
   2: \Device\NPF_{A8FB-717X-4XX9-XXXX-XXXX09FEX65B}
   ```

5. **Update config.py:**
   ```python
   INTERFACE = r'\Device\NPF_{4216ADDE-FA90-420A-AB07-65BEB98F4B23}'  # Use exact string from step 4
   PACKET_COUNT = 10
   ```

6. **Run the sniffer:**
   ```powershell
   python main.py
   ```

#### Windows Troubleshooting:
- **Error "Access Denied":** Ensure you're running as Administrator
- **Error "No such device":** Check interface name is exactly as listed
- **No packets captured:** Try different interface or set `INTERFACE = None`

---

### 🐧 **Linux Instructions**

#### Prerequisites:
1. **Update system packages:**
   ```bash
   sudo apt update && sudo apt upgrade -y  # Ubuntu/Debian
   # OR
   sudo yum update -y                       # CentOS/RHEL
   # OR
   sudo pacman -Syu                         # Arch Linux
   ```

2. **Install Python and pip:**
   ```bash
   sudo apt install python3 python3-pip   # Ubuntu/Debian
   # OR
   sudo yum install python3 python3-pip   # CentOS/RHEL
   # OR
   sudo pacman -S python python-pip       # Arch Linux
   ```

3. **Install development tools (required for some packages):**
   ```bash
   sudo apt install build-essential libpcap-dev  # Ubuntu/Debian
   # OR
   sudo yum groupinstall "Development Tools"     # CentOS/RHEL
   sudo yum install libpcap-devel
   # OR
   sudo pacman -S base-devel libpcap             # Arch Linux
   ```

#### Running on Linux:

1. **Navigate to project directory:**
   ```bash
   cd /path/to/Cybersecurity-Project-xi/network_packet_sniffer
   ```

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   # OR if you prefer virtual environment (recommended):
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Check available interfaces:**
   ```bash
   python3 list_interfaces.py
   ```
   Example output:
   ```
   Available Network Interfaces:
   1: lo
   2: eth0
   3: wlan0
   4: docker0
   ```

4. **Update config.py:**
   ```python
   INTERFACE = 'eth0'  # or 'wlan0' for WiFi, etc.
   PACKET_COUNT = 10
   ```

5. **Run the sniffer with sudo:**
   ```bash
   sudo python3 main.py
   # OR if using virtual environment:
   sudo ./venv/bin/python main.py
   ```

#### Linux Interface Examples:
- **`lo`** - Loopback interface (localhost traffic)
- **`eth0`** - First Ethernet interface
- **`wlan0`** - First WiFi interface
- **`enp0s3`** - Modern Ethernet naming convention
- **`wlp2s0`** - Modern WiFi naming convention

#### Linux Troubleshooting:
- **Error "Operation not permitted":** Use `sudo`
- **Package installation fails:** Install development tools and libpcap
- **Interface not found:** Use `ip link show` or `ifconfig` to list interfaces
- **No packets on interface:** Check if interface is up: `sudo ip link set eth0 up`

---

### 💡 **Quick Start Commands**

#### Windows (PowerShell as Admin):
```powershell
git clone https://github.com/Srijan-XI/Cybersecurity-Project-xi/tree/main/network_packet_sniffer.git
cd Cybersecurity-Project-xi\network_packet_sniffer
pip install -r requirements.txt
python list_interfaces.py
# Update config.py with correct interface
python main.py
```

#### Linux (Terminal):
```bash
git clone https://github.com/Srijan-XI/Cybersecurity-Project-xi/tree/main/network_packet_sniffer.git
cd Cybersecurity-Project-xi/network_packet_sniffer
pip3 install -r requirements.txt
python3 list_interfaces.py
# Update config.py with correct interface
sudo python3 main.py
```

## 🔧 Advanced Troubleshooting

### 🪟 Windows-Specific Issues:

1. **Permission Denied Error:**
   - **Solution:** Run Command Prompt or PowerShell as Administrator
   - Right-click → "Run as administrator"
   - Alternative: Use `runas` command: `runas /user:Administrator cmd`

2. **Npcap Installation Issues:**
   - **Solution:** Download and install Npcap from [https://nmap.org/npcap/](https://nmap.org/npcap/)
   - Make sure to install with "Install Npcap in WinPcap API-compatible Mode" enabled
   - If issues persist, uninstall and reinstall Npcap
   - Check Windows Defender/Antivirus isn't blocking the installation

3. **Interface Format Issues:**
   - Windows interfaces use format: `\Device\NPF_{GUID}`
   - Copy the exact string from `list_interfaces.py` output
   - Use raw strings: `r'\Device\NPF_{GUID}'`

4. **Firewall Blocking:**
   - Windows Defender Firewall might block packet capture
   - Add Python.exe to firewall exceptions
   - Or temporarily disable firewall for testing

### 🐧 Linux-Specific Issues:

1. **Permission Denied (Linux):**
   - **Solution:** Always use `sudo` for packet capture
   - Alternative: Add user to specific groups:
     ```bash
     sudo usermod -a -G wireshark $USER
     sudo setcap cap_net_raw,cap_net_admin+eip $(which python3)
     ```

2. **Package Installation Failures:**
   - **Solution:** Install development packages:
     ```bash
     # Ubuntu/Debian
     sudo apt install python3-dev libpcap-dev build-essential
     
     # CentOS/RHEL
     sudo yum install python3-devel libpcap-devel gcc
     
     # Arch Linux
     sudo pacman -S python gcc libpcap
     ```

3. **Interface Not Found:**
   - **Solution:** List interfaces with system commands:
     ```bash
     ip link show           # Modern way
     ifconfig -a           # Traditional way
     cat /proc/net/dev     # Alternative method
     ```

4. **Virtual Environment Issues:**
   - If using venv, run with full path:
     ```bash
     sudo /path/to/venv/bin/python main.py
     ```

### 🔄 General Issues:

1. **No Packets Captured:**
   - Try setting `INTERFACE = None` in `config.py` to capture on all interfaces
   - Ensure network activity is present on the selected interface
   - Check if interface is up and has an IP address
   - Test with a busy interface (like your main internet connection)

2. **Python Import Errors:**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version: `python --version` (needs 3.8+)
   - Clear Python cache: `python -Bc "import sys; print(sys.path)"`

3. **PCAP File Issues:**
   - Ensure write permissions in the directory
   - Check available disk space
   - Verify the directory isn't read-only

4. **High CPU Usage:**
   - Reduce packet count in `config.py`
   - Add filters to capture specific traffic only
   - Use a less busy network interface

## 📊 Output Files

- **`captured_packets.pcap`** - Contains captured network packets
- Can be opened with Wireshark for detailed analysis
- File is created in the same directory as `main.py`

## � System Requirements Summary

| Requirement | Windows | Linux |
|-------------|---------|-------|
| **Python Version** | 3.8+ | 3.8+ |
| **Privileges** | Administrator | sudo/root |
| **Packet Capture Library** | Npcap | libpcap (usually pre-installed) |
| **Development Tools** | Not required | build-essential/gcc |
| **Interface Format** | `\Device\NPF_{GUID}` | `eth0`, `wlan0`, etc. |

## 🔍 Example Usage Scenarios

### Scenario 1: Monitor Web Traffic
```python
# In config.py
INTERFACE = 'eth0'  # or your main interface
PACKET_COUNT = 50   # Capture more packets for web browsing

# Run and then browse websites to see HTTP/HTTPS traffic
```

### Scenario 2: Monitor Local Services
```python
# In config.py
INTERFACE = 'lo'    # Loopback interface (Linux) or equivalent
PACKET_COUNT = 20   # Monitor localhost communications
```

### Scenario 3: Monitor All Network Activity
```python
# In config.py
INTERFACE = None    # Capture on all interfaces
PACKET_COUNT = 100  # Capture more for comprehensive monitoring
```

## �🛡️ Security Considerations

- This tool requires administrator/root privileges to capture network packets
- **Legal Compliance:** Only use on networks you own or have explicit written permission to monitor
- **Privacy Laws:** Be aware of local privacy laws and regulations (GDPR, CCPA, etc.)
- **Data Sensitivity:** Captured data may contain sensitive information including:
  - Passwords (if transmitted in plain text)
  - Personal information
  - API keys and tokens
  - Private communications
- **Storage Security:** Secure the generated `.pcap` files appropriately
- **Network Policies:** Check your organization's network monitoring policies before use

## 📚 Additional Resources

- **Wireshark Documentation:** [https://www.wireshark.org/docs/](https://www.wireshark.org/docs/)
- **Scapy Documentation:** [https://scapy.readthedocs.io/](https://scapy.readthedocs.io/)
- **Npcap Installation Guide:** [https://nmap.org/npcap/guide/](https://nmap.org/npcap/guide/)
- **Linux Network Interfaces:** [https://www.tldp.org/LDP/nag2/x-087-2-iface.intro.html](https://www.tldp.org/LDP/nag2/x-087-2-iface.intro.html)

---

**⚠️ Disclaimer:** This tool is for educational and authorized network monitoring purposes only. Users are responsible for complying with all applicable laws and regulations.