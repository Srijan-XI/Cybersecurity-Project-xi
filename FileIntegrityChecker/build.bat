@echo off
REM Build script for File Integrity Checker on Windows

echo Building File Integrity Checker...

REM Create obj and data directories if they don't exist
if not exist "obj" mkdir obj
if not exist "data" mkdir data

REM Check if vcpkg is available (common way to install OpenSSL on Windows)
if exist "C:\vcpkg\installed\x64-windows\include\openssl" (
    echo Using vcpkg OpenSSL installation...
    set OPENSSL_INCLUDE=-I"C:\vcpkg\installed\x64-windows\include"
    set OPENSSL_LIB=-L"C:\vcpkg\installed\x64-windows\lib" -lssl -lcrypto
) else (
    echo Warning: OpenSSL not found in vcpkg. Please install OpenSSL or modify paths.
    echo You can install OpenSSL via vcpkg with:
    echo   vcpkg install openssl:x64-windows
    set OPENSSL_INCLUDE=
    set OPENSSL_LIB=-lssl -lcrypto
)

REM Compile
g++ -std=c++17 -Wall -Wextra -I include %OPENSSL_INCLUDE% src/*.cpp -o FileIntegrityChecker.exe %OPENSSL_LIB%

if %ERRORLEVEL% EQU 0 (
    echo Build successful! Executable: FileIntegrityChecker.exe
) else (
    echo Build failed. Please check that:
    echo 1. g++ compiler is installed and in PATH
    echo 2. OpenSSL development libraries are installed
    echo 3. All source files are present
)

pause