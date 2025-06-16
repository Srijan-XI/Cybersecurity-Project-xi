import os
os.environ["SCAPY_CACHE"] = "0"  # Disable Scapy cache

from scapy.all import get_if_list

interfaces = get_if_list()
print("Available Network Interfaces:")
for i, iface in enumerate(interfaces):
    print(f"{i + 1}: {iface}")
