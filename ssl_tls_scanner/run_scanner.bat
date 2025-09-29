@echo off
title SSL/TLS Certificate Scanner
color 0A
echo.
echo ================================
echo    SSL/TLS Certificate Scanner
echo ================================
echo.
echo This tool will scan SSL/TLS certificates for the domains you provide.
echo Reports will be saved in the reports/ folder.
echo.
pause
cd /d "%~dp0"
build\exe.win-amd64-3.13\ssl_tls_scanner.exe
echo.
echo Scan completed. Press any key to exit.
pause >nul