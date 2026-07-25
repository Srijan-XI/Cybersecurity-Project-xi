from packet_sniffer.sniffer import start_sniffing
from packet_sniffer.pcap_writer import initialize_capture_file, save_remaining_packets
from config import INTERFACE, PACKET_COUNT

if __name__ == "__main__":
    print("Starting Packet Sniffer...")
    print(f"Using interface: {INTERFACE if INTERFACE is not None else 'all available interfaces'}")
    print(f"Capturing {PACKET_COUNT} packets...")
    
    try:
        initialize_capture_file()
        start_sniffing(interface=INTERFACE, packet_count=PACKET_COUNT)
    except KeyboardInterrupt:
        print("\nStopping packet capture...")
    finally:
        save_remaining_packets()
        print("Packet capture completed.")
