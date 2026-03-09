import socket
import ssl
from OpenSSL import crypto
from datetime import datetime

def get_certificate_info(hostname, port=443):
    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    try:
        conn.settimeout(5.0)
        conn.connect((hostname, port))
        cert_bin = conn.getpeercert(True)
        x509 = crypto.load_certificate(crypto.FILETYPE_ASN1, cert_bin)
        
        subject = dict(x509.get_subject().get_components())
        issuer = dict(x509.get_issuer().get_components())
        not_before = datetime.strptime(x509.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
        not_after = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
        
        return {
            'hostname': hostname,
            'issuer': issuer,
            'subject': subject,
            'not_before': not_before.strftime('%Y-%m-%d'),
            'not_after': not_after.strftime('%Y-%m-%d')
        }
    except Exception as e:
        return {'hostname': hostname, 'error': str(e)}
    finally:
        conn.close()
