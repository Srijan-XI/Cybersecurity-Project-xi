from scapy.utils import wrpcap
import os

captured_packets = []

def save_packet(packet):
    global captured_packets
    captured_packets.append(packet)
    if len(captured_packets) >= 10:  # Save after 10 packets
        try:
            wrpcap('captured_packets.pcap', captured_packets)
            print("Saved packets to 'captured_packets.pcap'")
            captured_packets.clear()  # Clear the list after saving
        except Exception as e:
            print(f"Error saving packets to file: {e}")

def save_remaining_packets():
    """Save any remaining packets at the end of capture"""
    global captured_packets
    if captured_packets:
        try:
            wrpcap('captured_packets.pcap', captured_packets)
            print(f"Saved {len(captured_packets)} remaining packets to 'captured_packets.pcap'")
            captured_packets.clear()
        except Exception as e:
            print(f"Error saving remaining packets: {e}")
