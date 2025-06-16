import socket
import threading
from .service_identifier import identify_service

def scan_port(ip, port, results):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                service = identify_service(port)
                results.append((port, service))
    except Exception:
        pass

def run_scanner(ip, start_port, end_port, thread_count):
    threads = []
    results = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, results))
        threads.append(thread)
        thread.start()

        if len(threads) >= thread_count:
            for t in threads:
                t.join()
            threads.clear()

    # Join any remaining threads
    for t in threads:
        t.join()

    return sorted(results)
