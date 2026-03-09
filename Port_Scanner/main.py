#!/usr/bin/env python3
"""
Port Scanner - Main Entry Point

A simple yet efficient port scanner to scan open ports on remote machines.
Supports multi-threaded scanning, port range selection, and basic service identification.
"""

import sys
import os
import argparse
import signal

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scanner import PortScanner, quick_scan, validate_ip, validate_port_range
from scanner.utils import get_user_input, resolve_hostname
from config import DEFAULT_START_PORT, DEFAULT_END_PORT, DEFAULT_THREAD_COUNT


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\n\nScan interrupted by user. Exiting...")
    sys.exit(0)


def print_banner():
    """Print application banner"""
    banner = """
    ╔═══════════════════════════════════════╗
    ║           PORT SCANNER v1.0           ║
    ║      Multi-threaded Port Scanner      ║
    ║         Like Nmap but Simple          ║
    ╚═══════════════════════════════════════╝
    """
    print(banner)


def interactive_mode():
    """Run scanner in interactive mode"""
    print("\n🔍 Interactive Mode")
    print("=" * 40)

    try:
        target_ip, start_port, end_port = get_user_input()

        print(f"\n📡 Target: {target_ip}")
        print(f"🔢 Port Range: {start_port}-{end_port}")
        print(f"🧵 Threads: {DEFAULT_THREAD_COUNT}")

        confirm = input("\nProceed with scan? (y/n): ").lower().strip()
        if confirm != 'y':
            print("Scan cancelled.")
            return

        # Create scanner instance
        scanner = PortScanner(target_ip, start_port, end_port)

        # Perform scan
        open_ports = scanner.scan()

        # Display results
        print(scanner.get_scan_summary())

        if open_ports:
            print(f"\n✅ Found {len(open_ports)} open ports")
        else:
            print("\n❌ No open ports found")

    except KeyboardInterrupt:
        print("\n\nScan interrupted by user.")
    except Exception as e:
        print(f"\n❌ Error during scan: {e}")


def command_line_mode(args):
    """Run scanner in command line mode"""
    target = args.target

    # Validate/resolve target
    if validate_ip(target):
        target_ip = target
    else:
        resolved_ip = resolve_hostname(target)
        if resolved_ip:
            target_ip = resolved_ip
            print(f"Resolved {target} to {target_ip}")
        else:
            print(f"❌ Invalid target: {target}")
            sys.exit(1)

    # Validate port range
    if not validate_port_range(args.start_port, args.end_port):
        print("❌ Invalid port range")
        sys.exit(1)

    print(f"\n📡 Target: {target_ip}")
    print(f"🔢 Port Range: {args.start_port}-{args.end_port}")
    print(f"🧵 Threads: {args.threads}")

    try:
        if args.quick:
            print("\n🚀 Quick scan mode")
            open_ports = quick_scan(target_ip, True)

            if open_ports:
                print("\n--- Quick Scan Results ---")
                for port, service in sorted(open_ports):
                    print(f"Port {port}: Open ({service})")
            else:
                print("\n❌ No open ports found in quick scan")
        else:
            # Create scanner instance
            scanner = PortScanner(target_ip, args.start_port, args.end_port, args.threads)

            # Perform scan
            open_ports = scanner.scan()

            # Display results
            print(scanner.get_scan_summary())

    except KeyboardInterrupt:
        print("\n\nScan interrupted by user.")
    except Exception as e:
        print(f"\n❌ Error during scan: {e}")


def main():
    """Main function"""
    # Set up signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Print banner
    print_banner()

    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Multi-threaded port scanner with service identification",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                           # Interactive mode
  python main.py -t 192.168.1.1           # Scan default ports
  python main.py -t google.com -s 80 -e 443  # Scan specific range
  python main.py -t 127.0.0.1 --quick     # Quick scan common ports
        """
    )

    parser.add_argument('-t', '--target', 
                       help='Target IP address or hostname')
    parser.add_argument('-s', '--start-port', 
                       type=int, default=DEFAULT_START_PORT,
                       help=f'Start port (default: {DEFAULT_START_PORT})')
    parser.add_argument('-e', '--end-port', 
                       type=int, default=DEFAULT_END_PORT,
                       help=f'End port (default: {DEFAULT_END_PORT})')
    parser.add_argument('--threads', 
                       type=int, default=DEFAULT_THREAD_COUNT,
                       help=f'Number of threads (default: {DEFAULT_THREAD_COUNT})')
    parser.add_argument('-q', '--quick', 
                       action='store_true',
                       help='Quick scan of common ports only')
    parser.add_argument('--version', 
                       action='version', version='Port Scanner 1.0.0')

    args = parser.parse_args()

    # Run in appropriate mode
    if args.target:
        command_line_mode(args)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
