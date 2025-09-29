import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_options = {
    'packages': [],
    'excludes': [],
    'include_files': ['scanner/']
}

base = 'Console'

executables = [
    Executable('main.py', base=base, target_name='ssl_tls_scanner.exe'),
    Executable('main_cli.py', base=base, target_name='ssl_tls_scanner_cli.exe')
]

setup(
    name='SSL TLS Scanner',
    version='1.0',
    description='A tool to scan SSL/TLS certificates',
    options={'build_exe': build_options},
    executables=executables
)