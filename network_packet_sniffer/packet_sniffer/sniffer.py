from scapy.all import sniff
from .analyzer import analyze_packet
from .pcap_writer import save_packet

def packet_callback(packet):
    analyze_packet(packet)
    save_packet(packet)

def start_sniffing(interface="eth0", packet_count=10):
    print(f"Sniffing on interface: {interface} for {packet_count} packets...")
    sniff(iface=interface, prn=packet_callback, count=packet_count)
