"""
Utility functions for the port scanner
"""

import ipaddress
import socket


def validate_ip(ip_string):
    """
    Validate if the provided string is a valid IP address (IPv4 or IPv6)

    Args:
        ip_string (str): IP address to validate

    Returns:
        bool: True if valid IP, False otherwise
    """
    try:
        ipaddress.ip_address(ip_string)
        return True
    except ValueError:
        return False


def validate_port_range(start_port, end_port):
    """
    Validate port range

    Args:
        start_port (int): Starting port number
        end_port (int): Ending port number

    Returns:
        bool: True if valid range, False otherwise
    """
    if not isinstance(start_port, int) or not isinstance(end_port, int):
        return False

    if start_port < 1 or end_port > 65535:
        return False

    if start_port > end_port:
        return False

    return True


def resolve_hostname(hostname):
    """
    Resolve hostname to IP address

    Args:
        hostname (str): Hostname to resolve

    Returns:
        str: IP address or None if resolution fails
    """
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return None


def format_scan_results(open_ports):
    """
    Format scan results for display

    Args:
        open_ports (list): List of tuples (port, service)

    Returns:
        str: Formatted results string
    """
    if not open_ports:
        return "No open ports found."

    result = "\n--- Scan Summary ---\n"
    for port, service in sorted(open_ports):
        result += f"Port {port}: Open ({service})\n"

    return result


def get_user_input():
    """
    Get user input for target IP and port range

    Returns:
        tuple: (target_ip, start_port, end_port)
    """
    from config import DEFAULT_START_PORT, DEFAULT_END_PORT

    # Get target IP
    while True:
        target = input("Enter target IP address or hostname: ").strip()
        if not target:
            print("Please enter a valid target.")
            continue

        # Try to validate as IP first
        if validate_ip(target):
            target_ip = target
            break
        else:
            # Try to resolve as hostname
            resolved_ip = resolve_hostname(target)
            if resolved_ip:
                target_ip = resolved_ip
                print(f"Resolved {target} to {target_ip}")
                break
            else:
                print("Invalid IP address or hostname. Please try again.")

    # Get port range
    while True:
        try:
            start_input = input(f"Enter start port (default: {DEFAULT_START_PORT}): ").strip()
            start_port = int(start_input) if start_input else DEFAULT_START_PORT

            end_input = input(f"Enter end port (default: {DEFAULT_END_PORT}): ").strip()
            end_port = int(end_input) if end_input else DEFAULT_END_PORT

            if validate_port_range(start_port, end_port):
                break
            else:
                print("Invalid port range. Ports must be between 1-65535 and start <= end.")
        except ValueError:
            print("Please enter valid numbers for ports.")

    return target_ip, start_port, end_port
