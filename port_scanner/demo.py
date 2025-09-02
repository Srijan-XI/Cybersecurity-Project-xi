#!/usr/bin/env python3
"""
Port Scanner Demo Script
Shows various ways to use the port scanner
"""

from scanner import validate_ip, identify_service

def demo_service_identification():
    """Demo service identification features"""
    print("🔍 Service Identification Demo")
    print("=" * 40)

    common_ports = [21, 22, 23, 25, 53, 80, 135, 139, 443, 445, 993, 3389]

    for port in common_ports:
        service = identify_service(port)
        print(f"Port {port:4d}: {service}")

def demo_ip_validation():
    """Demo IP validation"""
    print("\n🌐 IP Validation Demo")  
    print("=" * 40)

    test_ips = [
        "127.0.0.1",
        "192.168.1.1", 
        "8.8.8.8",
        "::1",
        "invalid_ip",
        "256.256.256.256"
    ]

    for ip in test_ips:
        is_valid = validate_ip(ip)
        status = "✅ Valid" if is_valid else "❌ Invalid"
        print(f"{ip:<20} {status}")

def main():
    """Run all demos"""
    print("🚀 Port Scanner - Feature Demonstrations")
    print("=" * 50)

    demo_service_identification()
    demo_ip_validation() 

    print("\n✨ Demo Complete!")
    print("\nTo run the actual scanner:")
    print("  python3 main.py                    # Interactive mode")
    print("  python3 main.py -t 127.0.0.1       # Command line mode")  
    print("  python3 main.py --help             # Show all options")

if __name__ == "__main__":
    main()
