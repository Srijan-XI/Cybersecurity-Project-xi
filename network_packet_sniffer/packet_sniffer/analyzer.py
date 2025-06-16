from scapy.layers.inet import IP, TCP, UDP

def analyze_packet(packet):
    print("\n=== Packet Captured ===")
    
    if IP in packet:
        ip_layer = packet[IP]
        print(f"From: {ip_layer.src} -> To: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print("Protocol: TCP")
            print(f"Source Port: {tcp_layer.sport} -> Destination Port: {tcp_layer.dport}")
        
        elif UDP in packet:
            udp_layer = packet[UDP]
            print("Protocol: UDP")
            print(f"Source Port: {udp_layer.sport} -> Destination Port: {udp_layer.dport}")
    else:
        print("Non-IP Packet")
