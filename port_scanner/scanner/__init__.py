"""
Port Scanner Package

A multi-threaded port scanner with service identification capabilities.
"""

from .port_scanner import PortScanner, quick_scan, run_scanner
from .service_identifier import identify_service, get_service_description, is_common_service, get_security_info
from .utils import validate_ip, validate_port_range, get_user_input, format_scan_results, resolve_hostname

__version__ = "1.0.0"
__author__ = "Port Scanner Team"

__all__ = [
    'PortScanner',
    'quick_scan',
    'run_scanner',
    'identify_service',
    'get_service_description',
    'get_security_info',
    'is_common_service',
    'validate_ip',
    'validate_port_range',
    'get_user_input',
    'format_scan_results',
    'resolve_hostname'
]
