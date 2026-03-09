from packet_sniffer.sniffer import start_sniffing
from packet_sniffer.pcap_writer import save_remaining_packets
from config import INTERFACE, PACKET_COUNT

if __name__ == "__main__":
    print("Starting Packet Sniffer...")
    print(f"Using interface: {INTERFACE}")
    print(f"Capturing {PACKET_COUNT} packets...")
    
    try:
        start_sniffing(interface=INTERFACE, packet_count=PACKET_COUNT)
    except KeyboardInterrupt:
        print("\nStopping packet capture...")
    finally:
        save_remaining_packets()
        print("Packet capture completed.")
