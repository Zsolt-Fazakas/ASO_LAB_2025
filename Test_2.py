from scapy.all import ARP, Ether, srp

def scan_vlan(network):
    print(f"🔍 Scanning VLAN {network}...\n")

    # Creăm un request ARP pentru toate IP-urile din rețea
    arp_request = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address
    packet = ether / arp_request

    # Trimitem pachetul și capturăm răspunsurile
    answered, _ = srp(packet, timeout=2, verbose=False)

    print("✅ Mașini active în VLAN:")
    for sent, received in answered:
        print(f"➡ IP: {received.psrc} - MAC: {received.hwsrc}")

# Specificăm rețeaua VLAN (de exemplu, 10.8.11.0/24)
scan_vlan("10.8.11.0/24")
