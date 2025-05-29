import subprocess

subprocess.run(["g++", "-o", "scanner_cpp/scanner", "scanner_cpp/main.cpp"])
subprocess.run(["./scanner_cpp/scanner"])
subprocess.run(["go", "run", "net_analyzer_go/netscan.go"])
from analyzer_py.analyzer import analyze_logs
analyze_logs()
