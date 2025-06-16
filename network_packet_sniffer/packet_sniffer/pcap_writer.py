from scapy.utils import wrpcap

captured_packets = []

def save_packet(packet):
    global captured_packets
    captured_packets.append(packet)
    if len(captured_packets) >= 10:  # Save after 10 packets
        wrpcap('captured_packets.pcap', captured_packets)
        print("Saved packets to 'captured_packets.pcap'")
