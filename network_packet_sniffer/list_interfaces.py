import os
os.environ["SCAPY_CACHE"] = "0"  # Disable Scapy cache

from scapy.all import get_if_list

try:
    interfaces = get_if_list()
    print("Available Network Interfaces:")
    for i, iface in enumerate(interfaces):
        print(f"{i + 1}: {iface}")
    
    print("\nNote: Use the interface name exactly as shown above in your config.py file.")
    print("For Windows, interfaces typically start with '\\Device\\NPF_'")
    
except Exception as e:
    print(f"Error listing interfaces: {e}")
    print("Make sure you have Npcap installed and are running with administrator privileges.")
