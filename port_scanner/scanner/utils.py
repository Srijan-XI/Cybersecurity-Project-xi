import ipaddress

def validate_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def validate_port_range(start, end):
    return 0 < start <= 65535 and 0 < end <= 65535 and start <= end
