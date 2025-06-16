# SSL/TLS Certificate Scanner

A Python-based SSL/TLS Certificate Scanner that checks SSL certificate validity, parses certificate details, warns about upcoming expiry, and generates a comprehensive report.

---

## 📝 Features

- ✅ **SSL/TLS Certificate Parsing**
- ✅ **Certificate Expiry Validation**
- ✅ **Expiry Warnings (Default: 30 Days)**
- ✅ **Report Generation (Text File)**
- ✅ **Interactive Target Entry**

---

## 📦 Project Structure

```
ssl_tls_scanner/
│
├── main.py                  # Entry point
├── scanner/
│   ├── __init__.py
│   ├── ssl_scanner.py       # Core SSL scanning logic
│   └── utils.py             # Utility functions (date handling, warnings)
├── reports/
│   └── scan_report.txt      # Generated report file
└── requirements.txt         # Project dependencies

```

---

## ⚙️ Requirements

```pyOpenSSL```

## ✅ Workflow
1. User runs ```python main.py```.

  - Input target domains interactively:

```
Enter the hostnames to scan (type 'done' to finish):
Enter hostname: google.com
Enter hostname: example.com
Enter hostname: expired.badssl.com
Enter hostname: done
```
2. Targets in main.py are scanned.

3. Each domain's SSL certificate is parsed:

   - Issuer

    - Subject

    - Valid From / Valid To

4. Checks expiration:

- Valid / Expiring Soon / Expired

5. Report saved to ```reports/scan_report.txt```.

## Sample Report:
```
SSL/TLS Certificate Report
========================================

Host: google.com
Issuer: {b'C': b'US', b'O': b'Google Trust Services LLC', b'CN': b'GTS CA 1C3'}
Subject: {b'C': b'US', b'ST': b'California', b'L': b'Mountain View', b'O': b'Google LLC', b'CN': b'*.google.com'}
Valid From: 2024-05-15
Valid To: 2024-08-10
Status: Valid (55 days left)

Host: expired.badssl.com
Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)

```