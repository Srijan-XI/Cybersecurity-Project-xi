# Configuration settings for the port scanner

# Default port range
DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 1024

# Threading configuration
DEFAULT_THREAD_COUNT = 100

# Timeout settings (in seconds)
SOCKET_TIMEOUT = 1

# Common service ports mapping
COMMON_SERVICES = {
    21: "FTP",
    22: "SSH", 
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    993: "IMAPS",
    995: "POP3S"
}
