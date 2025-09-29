@echo off
REM Build script for File Integrity Checker (Fallback Version) on Windows

echo Building File Integrity Checker (Fallback Version)...

REM Create obj and data directories if they don't exist
if not exist "obj" mkdir obj
if not exist "data" mkdir data

echo Compiling fallback version (no OpenSSL required)...

REM Compile fallback version
g++ -std=c++17 -Wall -Wextra -I include src/main_fallback.cpp src/FileManager.cpp src/FileHasherFallback.cpp -o FileIntegrityChecker_fallback.exe

if %ERRORLEVEL% EQU 0 (
    echo Build successful! Executable: FileIntegrityChecker_fallback.exe
    echo.
    echo Testing the executable:
    FileIntegrityChecker_fallback.exe help
) else (
    echo Build failed. Please check that:
    echo 1. g++ compiler is installed and in PATH
    echo 2. All source files are present
)

pause