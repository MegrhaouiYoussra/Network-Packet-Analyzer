# packet_analyzer.py

from scapy.all import sniff, IP, TCP, UDP, ICMP


def analyze_packet(packet):
    """
    Analyze a captured packet and print useful information.
    """

    if not packet.haslayer(IP):
        return

    ip_layer = packet[IP]
    src_ip = ip_layer.src
    dst_ip = ip_layer.dst
    packet_length = len(packet)

    print("=" * 70)
    print(f"Source IP      : {src_ip}")
    print(f"Destination IP : {dst_ip}")
    print(f"Packet Length  : {packet_length} bytes")

    if packet.haslayer(TCP):
        tcp_layer = packet[TCP]
        print("Protocol       : TCP")
        print(f"Source Port    : {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")
        print(f"Flags          : {tcp_layer.flags}")

    elif packet.haslayer(UDP):
        udp_layer = packet[UDP]
        print("Protocol       : UDP")
        print(f"Source Port    : {udp_layer.sport}")
        print(f"Destination Port: {udp_layer.dport}")

    elif packet.haslayer(ICMP):
        icmp_layer = packet[ICMP]
        print("Protocol       : ICMP")
        print(f"Type           : {icmp_layer.type}")
        print(f"Code           : {icmp_layer.code}")

    else:
        print(f"Protocol       : Other (IP proto={ip_layer.proto})")


def main():
    print("Starting Network Packet Analyzer...")
    print("Capturing packets in real time. Press Ctrl+C to stop.\n")

    sniff(prn=analyze_packet, store=False)


if __name__ == "__main__":
    main()
