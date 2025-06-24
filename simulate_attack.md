# Evil Twin Simulation on Windows (Test Method)

Since monitor mode is not supported on Windows:
1. Download or create a PCAP file containing fake SSID packets.
2. Modify `detector.py` to read a `.pcap` using:
   ```python
   packets = rdpcap("test.pcap")
   for pkt in packets:
       packet_handler(pkt)
