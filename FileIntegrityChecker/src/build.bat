@echo off
REM Simple build script for src directory
echo Building File Integrity Checker from src directory...

REM Go to project root
cd ..

REM Create directories if needed
if not exist "data" mkdir data

REM Build fallback version (most reliable)
echo Building fallback version...
g++ -std=c++17 -I include src/main_fallback.cpp src/FileManager.cpp src/FileHasherFallback.cpp -o FileIntegrityChecker_fallback.exe

if %ERRORLEVEL% EQU 0 (
    echo Build successful!
    echo Testing...
    FileIntegrityChecker_fallback.exe help
    echo.
    echo To use the program:
    echo   FileIntegrityChecker_fallback.exe add "filename.txt"
    echo   FileIntegrityChecker_fallback.exe check "filename.txt"
) else (
    echo Build failed. Please check that g++ is installed.
)

cd src
pause