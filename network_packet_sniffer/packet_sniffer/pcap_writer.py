from pathlib import Path

from scapy.utils import wrpcap

captured_packets = []
pcap_file = Path("captured_packets.pcap")
pcap_initialized = False


def initialize_capture_file():
    global captured_packets, pcap_initialized
    captured_packets = []
    pcap_initialized = False
    if pcap_file.exists():
        pcap_file.unlink()

def save_packet(packet):
    global captured_packets, pcap_initialized
    captured_packets.append(packet)
    if len(captured_packets) >= 10:  # Save after 10 packets
        try:
            wrpcap(str(pcap_file), captured_packets, append=pcap_initialized)
            pcap_initialized = True
            print(f"Saved packets to '{pcap_file}'")
            captured_packets.clear()  # Clear the list after saving
        except Exception as e:
            print(f"Error saving packets to file: {e}")

def save_remaining_packets():
    """Save any remaining packets at the end of capture"""
    global captured_packets, pcap_initialized
    if captured_packets:
        try:
            wrpcap(str(pcap_file), captured_packets, append=pcap_initialized)
            pcap_initialized = True
            print(f"Saved {len(captured_packets)} remaining packets to '{pcap_file}'")
            captured_packets.clear()
        except Exception as e:
            print(f"Error saving remaining packets: {e}")
