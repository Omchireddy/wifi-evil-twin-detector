from scapy.all import sniff, Dot11, Dot11Beacon, rdpcap
from core.utils import is_evil_twin, log_alert

def packet_handler(pkt):
    if pkt.haslayer(Dot11Beacon):
        ssid = pkt[Dot11Elt].info.decode(errors="ignore")
        bssid = pkt[Dot11].addr2

        if is_evil_twin(ssid, bssid):
            msg = f"[ALERT] Evil Twin Detected! SSID: {ssid}, BSSID: {bssid}"
            print(msg)
            log_alert(msg)

def start_sniffing(interface):
    try:
        print("[*] Sniffing packets... Press Ctrl+C to stop.")
        sniff(iface=interface, prn=packet_handler, store=0)
    except Exception as e:
        print(f"[ERROR] Sniffing failed: {e}")
        print("Hint: On Windows, real beacon sniffing is often restricted.")
