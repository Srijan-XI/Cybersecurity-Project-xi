from datetime import datetime, timedelta

def check_expiry(expiry_date_str, warning_days=30):
    expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
    remaining = expiry_date - datetime.utcnow()
    if remaining < timedelta(days=0):
        return "Expired"
    elif remaining < timedelta(days=warning_days):
        return f"Expiring Soon ({remaining.days} days left)"
    else:
        return f"Valid ({remaining.days} days left)"

def write_report(report_data, filepath='reports/scan_report.txt'):
    with open(filepath, 'w') as f:
        f.write(report_data)
