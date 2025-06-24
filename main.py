from core.detector import start_sniffing
import sys

def banner():
    print("""
  ███████╗██╗██╗     ███████╗    ████████╗██╗    ██╗██╗███╗   ██╗
  ██╔════╝██║██║     ██╔════╝    ╚══██╔══╝██║    ██║██║████╗  ██║
  █████╗  ██║██║     █████╗         ██║   ██║ █╗ ██║██║██╔██╗ ██║
  ██╔══╝  ██║██║     ██╔══╝         ██║   ██║███╗██║██║██║╚██╗██║
  ██║     ██║███████╗███████╗       ██║   ╚███╔███╔╝██║██║ ╚████║
  ╚═╝     ╚═╝╚══════╝╚══════╝       ╚═╝    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝

        Evil Twin Detector (Windows Edition) – Sai Om Chi Reddy
    """)

def main():
    banner()

    if len(sys.argv) != 2:
        print("\nUsage: python main.py <interface>")
        print("Example: python main.py Wi-Fi")
        sys.exit(1)

    interface = sys.argv[1]
    print(f"\n[*] Scanning on interface: {interface} (limited in Windows)\n")
    start_sniffing(interface)

if __name__ == "__main__":
    main()
