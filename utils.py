# Simulated safe SSID/BSSID pairs
trusted_networks = {
    "MyHomeWiFi": "00:11:22:33:44:55",
    "CampusWiFi": "AA:BB:CC:DD:EE:FF"
}

def is_evil_twin(ssid, bssid):
    if ssid in trusted_networks and trusted_networks[ssid].lower() != bssid.lower():
        return True
    return False

def log_alert(message):
    with open("logs/detection_log.txt", "a") as f:
        f.write(message + "\n")
