@echo off
REM Easy-to-use runner script for File Integrity Checker

REM Check if the executable exists
if exist "FileIntegrityChecker_fallback.exe" (
    set EXECUTABLE=FileIntegrityChecker_fallback.exe
) else if exist "FileIntegrityChecker.exe" (
    set EXECUTABLE=FileIntegrityChecker.exe
) else (
    echo Error: No executable found!
    echo Please build the project first by running:
    echo   build.bat
    echo   or
    echo   cd src && build.bat
    pause
    exit /b 1
)

REM If no arguments provided, show help
if "%1"=="" (
    echo File Integrity Checker - Quick Runner
    echo ====================================
    echo.
    %EXECUTABLE% help
    echo.
    echo Usage examples:
    echo   run.bat add "myfile.txt"
    echo   run.bat check "myfile.txt"
    echo   run.bat update "myfile.txt"
    echo   run.bat help
    echo.
    pause
    exit /b 0
)

REM Pass all arguments to the executable
%EXECUTABLE% %*

REM Show exit code if not successful
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Command failed with exit code: %ERRORLEVEL%
    pause
) else (
    echo.
    echo Command completed successfully!
)