def flag_suspicious_pattern(log_line: str) -> bool:
    suspicious_keywords = ['error', 'failed', 'unauthorized', 'attack', 'intrusion', 'malware']
    log_line_lower = log_line.lower()
    return any(keyword in log_line_lower for keyword in suspicious_keywords)
