#!/usr/bin/env python3
"""
SSL/TLS Certificate Scanner - Command Line Version
This version supports command line arguments for automation.
"""

import sys
import argparse
from scanner.ssl_scanner import get_certificate_info
from scanner.utils import check_expiry, write_report

def main():
    parser = argparse.ArgumentParser(description='SSL/TLS Certificate Scanner')
    parser.add_argument('hosts', nargs='*', help='Hostnames to scan')
    parser.add_argument('-f', '--file', help='File containing hostnames (one per line)')
    parser.add_argument('-o', '--output', default='reports/scan_report.txt', 
                       help='Output file path (default: reports/scan_report.txt)')
    parser.add_argument('--batch', action='store_true', 
                       help='Run in batch mode (no interactive prompts)')
    
    args = parser.parse_args()
    
    targets = []
    
    # Get hosts from command line arguments
    if args.hosts:
        targets.extend(args.hosts)
    
    # Get hosts from file
    if args.file:
        try:
            with open(args.file, 'r') as f:
                file_hosts = [line.strip() for line in f if line.strip()]
                targets.extend(file_hosts)
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            return 1
        except Exception as e:
            print(f"Error reading file '{args.file}': {e}")
            return 1
    
    # Interactive mode if no hosts provided and not in batch mode
    if not targets and not args.batch:
        print("Enter the hostnames to scan (type 'done' to finish):")
        while True:
            target = input("Enter hostname: ").strip()
            if target.lower() == 'done':
                break
            if target:  # non-empty input
                targets.append(target)
    
    if not targets:
        print("No targets provided. Exiting.")
        return 1

    report = "SSL/TLS Certificate Report\n"
    report += "="*40 + "\n\n"

    for target in targets:
        print(f"Scanning {target}...")
        info = get_certificate_info(target)
        report += f"Host: {info.get('hostname')}\n"

        if 'error' in info:
            report += f"Error: {info['error']}\n\n"
            continue

        report += f"Issuer: {info.get('issuer')}\n"
        report += f"Subject: {info.get('subject')}\n"
        report += f"Valid From: {info.get('not_before')}\n"
        report += f"Valid To: {info.get('not_after')}\n"

        status = check_expiry(info.get('not_after'))
        report += f"Status: {status}\n\n"

    # Write report
    try:
        write_report(report, args.output)
        print(f"SSL scan completed. Report saved to {args.output}.")
        return 0
    except Exception as e:
        print(f"Error writing report: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())