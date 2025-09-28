from scapy.all import sniff
from .analyzer import analyze_packet
from .pcap_writer import save_packet

def packet_callback(packet):
    try:
        analyze_packet(packet)
        save_packet(packet)
    except Exception as e:
        print(f"Error processing packet: {e}")

def start_sniffing(interface=None, packet_count=10):
    try:
        if interface is None:
            print("No interface specified. Sniffing on all interfaces...")
            sniff(prn=packet_callback, count=packet_count)
        else:
            print(f"Sniffing on interface: {interface} for {packet_count} packets...")
            sniff(iface=interface, prn=packet_callback, count=packet_count)
    except PermissionError:
        print("Error: Permission denied. Run as administrator or with elevated privileges.")
    except Exception as e:
        print(f"Error starting packet capture: {e}")
        print("Try running the list_interfaces.py script to check available interfaces.")
