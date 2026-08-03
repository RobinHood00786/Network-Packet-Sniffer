from scapy.all import sniff, IP, IPv6, TCP, UDP, Ether, ARP, ICMP

packet_count = 0

def packet_callback(packet):
    global packet_count
    packet_count += 1
    print(f"\n{'='*20} Packet {packet_count} {'='*20}")

    if IP in packet:
        print("Protocol : IP")
        print()
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print()

    elif IPv6 in packet:
        print("Protocol : IPv6")
        print()
        print("Source IPv6:", packet[IPv6].src)
        print("Destination IPv6:", packet[IPv6].dst)
        print()

    if TCP in packet:
        print("Protocol : TCP")
        print()
        print("Source Port:", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)
        print()

    if UDP in packet:  
        print("Protocol : UDP")
        print()
        print("Source Port:", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)
        print()

    if Ether in packet:
        print("Protocol : Ethernet")
        print()
        print("Source MAC:", packet[Ether].src)
        print("Destination MAC:", packet[Ether].dst)
        print()

    if ICMP in packet:
        print("Protocol : ICMP")
        print()
        print("ICMP Type:", packet[ICMP].type)
        print("ICMP Code:", packet[ICMP].code)
        print()

    print("Packet Summary:", packet.summary())
    print("\n" + "=""=" * 67 + "\n")

sniff(prn=packet_callback)