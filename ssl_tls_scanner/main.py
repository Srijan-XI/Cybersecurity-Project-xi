from scanner.ssl_scanner import get_certificate_info
from scanner.utils import check_expiry, write_report

def main():
    targets = []
    print("Enter the hostnames to scan (type 'done' to finish):")
    while True:
        target = input("Enter hostname: ").strip()
        if target.lower() == 'done':
            break
        if target:  # non-empty input
            targets.append(target)

    if not targets:
        print("No targets provided. Exiting.")
        return

    report = "SSL/TLS Certificate Report\n"
    report += "="*40 + "\n\n"

    for target in targets:
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

    write_report(report)
    print("SSL scan completed. Report saved to reports/scan_report.txt.")

if __name__ == "__main__":
    main()
