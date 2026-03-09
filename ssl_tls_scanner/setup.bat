@echo off
setlocal enabledelayedexpansion
title SSL/TLS Scanner Setup
color 0B

echo.
echo ==========================================
echo    SSL/TLS Certificate Scanner Setup
echo ==========================================
echo.
echo This will set up the SSL/TLS scanner executable.
echo.

:: Create a directory for the executable
set "INSTALL_DIR=%USERPROFILE%\SSLScanner"
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

:: Copy the executable and necessary files
echo Copying files...
xcopy /E /I /Y "build\exe.win-amd64-3.13\*" "%INSTALL_DIR%\" >nul

:: Create reports directory in install location
if not exist "%INSTALL_DIR%\reports" mkdir "%INSTALL_DIR%\reports"

:: Create a shortcut batch file
echo @echo off > "%INSTALL_DIR%\ssl_scanner.bat"
echo cd /d "%%~dp0" >> "%INSTALL_DIR%\ssl_scanner.bat"
echo ssl_tls_scanner.exe >> "%INSTALL_DIR%\ssl_scanner.bat"
echo pause >> "%INSTALL_DIR%\ssl_scanner.bat"

echo.
echo Setup completed successfully!
echo.
echo Executable location: %INSTALL_DIR%\ssl_tls_scanner.exe
echo Batch file location: %INSTALL_DIR%\ssl_scanner.bat
echo.
echo You can now run the scanner from: %INSTALL_DIR%
echo.
echo Adding to PATH (optional)...
echo You can add '%INSTALL_DIR%' to your system PATH to run 'ssl_tls_scanner.exe' from anywhere.
echo.

pause