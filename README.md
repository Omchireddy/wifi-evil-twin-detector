# 🕵️‍♂️ Evil Twin Wi-Fi Detector (Windows Edition)

## 📌 Description

**Evil Twin Wi-Fi Detector** is a lightweight command-line tool designed to detect potential Evil Twin attacks on Wi-Fi networks. It scans for duplicate SSIDs with different BSSIDs on the selected interface, which is a common indicator of rogue access points attempting to impersonate legitimate Wi-Fi hotspots.

---

## 🛠️ Features

- ✅ Terminal-based interface with ASCII banner.
- ✅ Detects duplicate SSIDs across different MAC addresses.
- ✅ Custom interface selection for Windows users.
- ✅ Modular structure (`core/`, `logs/`, `tests/`).
- ✅ Easy to extend and test.

---

## 📁 Project Structure
    wifi_evil_twin_detector/
    │
    ├── core/ # Main detection logic (start_sniffing)
    ├── logs/ # Stores scan logs
    ├── tests/ # Future unit/integration tests
    ├── .venv/ # Python virtual environment
    ├── main.py # Main execution script
    ├── requirements.txt # Python dependencies
    └── README.md # Project documentation
## ✅ 2. Create virtual environment
    python -m venv .venv
    .venv\Scripts\activate   # For Windows
## ✅ 3. Install dependencies
    pip install -r requirements.txt
## ✅ 4. Run the tool
    python main.py <your_wifi_interface>
## 🧪 Example Output
    [*] Scanning on interface: Wi-Fi (limited in Windows)

    [!] Detected SSID: "Free_Public_WiFi"
      ├── BSSID 1: 00:11:22:33:44:55 (Signal: -40dBm)
      └── BSSID 2: AA:BB:CC:DD:EE:FF (Signal: -30dBm) ❗ Potential Evil Twin
## 🛡️ Important Notes
- 🪟 Windows Wi-Fi APIs are limited; sniffing is basic unless run with advanced permissions or external tools.
- 🧪 Best tested on Kali Linux with scapy or airodump-ng for deeper monitoring (planned in v2.0).
## 📈 Future Improvements
- Linux Support with scapy-based packet sniffing.
- Real-time monitoring dashboard using Flask or Tkinter.
- Auto-log analysis of known safe vs rogue APs.
- Machine learning module for anomaly detection.
- Integration with alerting systems (email, Telegram bot, etc.).
- GUI version for more user-friendly detection.
- GUI version for more user-friendly detection.
## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.




