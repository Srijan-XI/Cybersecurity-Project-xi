"""
Service identification module for the port scanner
"""

from config import COMMON_SERVICES


# Extended service mapping
EXTENDED_SERVICES = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    37: "Time",
    42: "WINS",
    43: "WHOIS",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client", 
    69: "TFTP",
    79: "Finger",
    80: "HTTP",
    88: "Kerberos",
    110: "POP3",
    111: "RPC",
    119: "NNTP",
    123: "NTP",
    135: "Microsoft RPC",
    137: "NetBIOS Name",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    445: "Microsoft DS",
    465: "SMTPS",
    514: "Syslog",
    515: "LPD/LPR",
    587: "SMTP Submission",
    631: "IPP",
    636: "LDAPS",
    873: "rsync",
    993: "IMAPS",
    995: "POP3S",
    1433: "Microsoft SQL",
    1521: "Oracle DB",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Proxy",
    8443: "HTTPS Alt",
    9200: "Elasticsearch",
    27017: "MongoDB"
}


def identify_service(port):
    """
    Identify service running on a given port

    Args:
        port (int): Port number

    Returns:
        str: Service name or 'Unknown Service'
    """
    # First check common services
    if port in COMMON_SERVICES:
        return COMMON_SERVICES[port]

    # Then check extended services
    if port in EXTENDED_SERVICES:
        return EXTENDED_SERVICES[port]

    return "Unknown Service"


def get_service_description(port):
    """
    Get detailed service description

    Args:
        port (int): Port number

    Returns:
        str: Service description
    """
    service_descriptions = {
        21: "File Transfer Protocol - Used for transferring files",
        22: "Secure Shell - Encrypted remote login protocol", 
        23: "Telnet - Unencrypted remote login protocol",
        25: "Simple Mail Transfer Protocol - Email transmission",
        53: "Domain Name System - Name resolution service",
        80: "Hypertext Transfer Protocol - Web traffic",
        110: "Post Office Protocol v3 - Email retrieval",
        143: "Internet Message Access Protocol - Email access",
        443: "HTTP Secure - Encrypted web traffic",
        993: "IMAP over SSL/TLS - Secure email access",
        995: "POP3 over SSL/TLS - Secure email retrieval"
    }

    service_name = identify_service(port)
    description = service_descriptions.get(port, f"{service_name} service")

    return f"{service_name} - {description}" if port in service_descriptions else service_name


def is_common_service(port):
    """
    Check if port runs a commonly known service

    Args:
        port (int): Port number

    Returns:
        bool: True if common service, False otherwise
    """
    return port in COMMON_SERVICES or port in EXTENDED_SERVICES


def get_security_info(port):
    """
    Get basic security information about a service

    Args:
        port (int): Port number

    Returns:
        str: Security warning or info
    """
    high_risk_ports = {
        21: "FTP - Often uses plain text authentication",
        23: "Telnet - Unencrypted, high security risk",
        135: "RPC - Common target for attacks",
        445: "SMB - Vulnerable to various attacks",
        1433: "SQL Server - Database access, secure properly"
    }

    if port in high_risk_ports:
        return f"⚠️  {high_risk_ports[port]}"

    return ""
