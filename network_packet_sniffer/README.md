# Network Packet Sniffer

A simple yet powerful **Network Packet Sniffer** tool built with **Python** and **Scapy** for capturing, analyzing, and saving network packets to `.pcap` files. Designed to run on Windows systems with proper WinPcap/Npcap support.

---

## 🛠️ Features

- Real-time packet sniffing on a selected network interface.
- Displays protocol-specific details (TCP, UDP, ICMP, etc.).
- Saves captured packets into `.pcap` format for further analysis (using tools like Wireshark).
- Customizable packet count and network interface selection.
- Easily extendable and modular file structure.

---

## 📋 Requirements

Before running this project, ensure the following are installed:

- Python 3.8 or higher
- **Npcap (WinPcap alternative for Windows)**: [Download here](https://nmap.org/npcap/)
- Python Packages:
  - `scapy`
  - `colorama`
  
Install required packages via:

```bash
pip install -r requirements.txt
```
### 📂 Project Structure
```
network_packet_sniffer/
│
├── main.py                      # Entry point to start the sniffer
├── config.py                    # Configuration file (interface and packet count)
├── requirements.txt             # Python package dependencies
│
├── packet_sniffer/
│   ├── __init__.py
│   ├── sniffer.py               # Sniffing logic and packet handling
│   └── packet_handler.py        # Packet decoding and protocol parsing
│
└── utils/
    ├── __init__.py
    └── list_interfaces_with_ip.py  # Utility to list all interfaces with IPs

```
### ⚙️ Configuration (```config.py```)
Update your config.py with the correct interface before running:

# config.py
```
INTERFACE = r'\Device\NPF_{002DA8FB-717X-4XX9-XXXX-XXXX09FEX65B}'  # Replace with your actual interface
PACKET_COUNT = 10  # Number of packets to capture
```
⚠️ Note: Run the following to get your correct network interface:
```
python utils/list_interfaces_with_ip.py
```
## 🚀 How to Run
Clone the Repository:
```
git clone https://github.com/Srijan-XI/Cybersecurity-Project-xi/tree/main/network_packet_sniffer.git
cd network_packet_sniffer
```
## Install dependencies:
```
pip install -r requirements.txt
```
- Check and update the correct network interface in config.py using the utility:
```
python utils/list_interfaces_with_ip.py
```
- Run the Packet Sniffer:
```
python main.py
```