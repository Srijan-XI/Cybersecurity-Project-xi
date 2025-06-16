from .scanner.utils import validate_ip, validate_port_range
from .scanner.port_scanner import run_scanner
from .config import DEFAULT_START_PORT, DEFAULT_END_PORT, DEFAULT_THREAD_COUNT

def main():
    ip = input("Enter target IP: ").strip()
    if not validate_ip(ip):
        print("Invalid IP address.")
        return

    try:
        start_port = int(input(f"Enter start port [{DEFAULT_START_PORT}]: ") or DEFAULT_START_PORT)
        end_port = int(input(f"Enter end port [{DEFAULT_END_PORT}]: ") or DEFAULT_END_PORT)
    except ValueError:
        print("Port must be an integer.")
        return

    if not validate_port_range(start_port, end_port):
        print("Invalid port range.")
        return

    print(f"Scanning {ip} from port {start_port} to {end_port}...\n")
    results = run_scanner(ip, start_port, end_port, DEFAULT_THREAD_COUNT)

    print("\n--- Scan Summary ---")
    for port, service in results:
        print(f"Port {port}: Open ({service})")

if __name__ == "__main__":
    main()
