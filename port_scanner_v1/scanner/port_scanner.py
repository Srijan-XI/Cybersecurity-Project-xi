"""
Core port scanning functionality
"""

import socket
import threading
from queue import Queue
import time
from config import DEFAULT_THREAD_COUNT, SOCKET_TIMEOUT
from .service_identifier import identify_service, get_security_info


class PortScanner:
    """
    Multi-threaded port scanner class
    """

    def __init__(self, target_ip, start_port, end_port, thread_count=DEFAULT_THREAD_COUNT):
        """
        Initialize port scanner

        Args:
            target_ip (str): Target IP address
            start_port (int): Starting port number
            end_port (int): Ending port number
            thread_count (int): Number of threads to use
        """
        self.target_ip = target_ip
        self.start_port = start_port
        self.end_port = end_port
        self.thread_count = min(thread_count, end_port - start_port + 1)
        self.open_ports = []
        self.scanned_ports = 0
        self.total_ports = end_port - start_port + 1
        self.lock = threading.Lock()

        # Create queue for ports to scan
        self.port_queue = Queue()
        for port in range(start_port, end_port + 1):
            self.port_queue.put(port)

    def scan_port(self, port):
        """
        Scan a single port

        Args:
            port (int): Port number to scan

        Returns:
            bool: True if port is open, False otherwise
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(SOCKET_TIMEOUT)

            result = sock.connect_ex((self.target_ip, port))
            sock.close()

            return result == 0
        except socket.error:
            return False

    def worker(self):
        """
        Worker thread function
        """
        while not self.port_queue.empty():
            try:
                port = self.port_queue.get(timeout=1)

                if self.scan_port(port):
                    service = identify_service(port)
                    security_info = get_security_info(port)

                    with self.lock:
                        self.open_ports.append((port, service, security_info))
                        print(f"Port {port}: Open ({service})")
                        if security_info:
                            print(f"  {security_info}")

                with self.lock:
                    self.scanned_ports += 1
                    if self.scanned_ports % 100 == 0 or self.scanned_ports == self.total_ports:
                        progress = (self.scanned_ports / self.total_ports) * 100
                        print(f"Progress: {progress:.1f}% ({self.scanned_ports}/{self.total_ports})")

                self.port_queue.task_done()

            except Exception as e:
                continue

    def scan(self):
        """
        Perform the port scan using multiple threads

        Returns:
            list: List of tuples (port, service, security_info)
        """
        print(f"\nStarting port scan on {self.target_ip}")
        print(f"Scanning ports {self.start_port}-{self.end_port}")
        print(f"Using {self.thread_count} threads\n")

        start_time = time.time()

        # Create and start worker threads
        threads = []
        for i in range(self.thread_count):
            thread = threading.Thread(target=self.worker)
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        end_time = time.time()
        scan_duration = end_time - start_time

        print(f"\nScan completed in {scan_duration:.2f} seconds")
        print(f"Scanned {self.total_ports} ports")
        print(f"Found {len(self.open_ports)} open ports")

        return self.open_ports

    def get_scan_summary(self):
        """
        Get formatted scan summary

        Returns:
            str: Formatted summary
        """
        if not self.open_ports:
            return "\n--- Scan Summary ---\nNo open ports found."

        summary = "\n--- Scan Summary ---\n"
        for port, service, security_info in sorted(self.open_ports):
            summary += f"Port {port}: Open ({service})\n"
            if security_info:
                summary += f"  {security_info}\n"

        return summary


def quick_scan(target_ip, common_ports_only=True):
    """
    Perform a quick scan of common ports

    Args:
        target_ip (str): Target IP address  
        common_ports_only (bool): Scan only common ports

    Returns:
        list: List of open ports
    """
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 
                   135, 139, 445, 1433, 3389, 5900, 8080]

    if common_ports_only:
        ports_to_scan = common_ports
    else:
        ports_to_scan = list(range(1, 1025))

    print(f"Quick scanning {len(ports_to_scan)} ports on {target_ip}...")

    open_ports = []
    for port in ports_to_scan:
        scanner = PortScanner(target_ip, port, port, 1)
        if scanner.scan_port(port):
            service = identify_service(port)
            open_ports.append((port, service))
            print(f"Port {port}: Open ({service})")

    return open_ports
