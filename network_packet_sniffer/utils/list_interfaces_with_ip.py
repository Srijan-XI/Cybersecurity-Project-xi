from scapy.all import get_if_list, get_if_addr

print("Available Interfaces and their IP addresses:")
for iface in get_if_list():
    try:
        ip = get_if_addr(iface)
        print(f"Interface: {iface} | IP: {ip}")
    except Exception as e:
        print(f"Interface: {iface} | No IP assigned")
