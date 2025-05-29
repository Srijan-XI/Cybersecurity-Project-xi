import os
from analyzer_py.models.heuristics import flag_suspicious_pattern

LOG_DIR = 'outputs/logs'

def analyze_logs():
    suspicious_lines = []
    for filename in os.listdir(LOG_DIR):
        filepath = os.path.join(LOG_DIR, filename)
        if os.path.isfile(filepath) and filename.endswith('.log'):
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    if flag_suspicious_pattern(line):
                        suspicious_lines.append((filename, line.strip()))
    return suspicious_lines

def main():
    print("Starting analysis of log files...\n")
    flagged = analyze_logs()
    if not flagged:
        print("No suspicious activity detected.")
    else:
        print("Suspicious log entries found:\n")
        for filename, line in flagged:
            print(f"[{filename}] {line}")

if __name__ == '__main__':
    main()
