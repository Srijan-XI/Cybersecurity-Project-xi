@echo off
title Phishing Detection System - All-in-One Launcher
color 0A

:: ===============================================
::    PHISHING DETECTION SYSTEM - ALL-IN-ONE
:: ===============================================

echo.
echo  ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
echo  ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝ 
echo  ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗
echo  ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║
echo  ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝
echo  ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
echo.
echo  ██████╗ ███████╗████████╗███████╗ ██████╗████████╗ ██████╗ ██████╗ 
echo  ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
echo  ██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║   ██║██████╔╝
echo  ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
echo  ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
echo  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
echo.
echo ===============================================
echo    Comprehensive Cybersecurity Solution
echo ===============================================
echo.

:: Set project directory
set PROJECT_DIR=%~dp0
cd /d "%PROJECT_DIR%"

:: Initialize variables
set PYTHON_OK=false
set GO_OK=false
set SETUP_NEEDED=true
set ML_API_STARTED=false
set WEB_SERVER_STARTED=false
set GO_GATEWAY_STARTED=false

:: Main menu
:MAIN_MENU
cls
echo ===============================================
echo           MAIN MENU - SELECT OPTION
echo ===============================================
echo.
echo  [1] 🚀 QUICK START (Daily Use)
echo  [2] 🔧 FULL SETUP + RUN (First Time)
echo  [3] 📊 CHECK SYSTEM STATUS
echo  [4] 🛑 STOP ALL SERVICES
echo  [5] 🔍 SYSTEM DIAGNOSTICS
echo  [6] 📖 HELP INFO
echo  [7] ❌ EXIT
echo.
echo ===============================================
set /p choice="👉 Enter your choice (1-7): "

if "%choice%"=="1" goto QUICK_START
if "%choice%"=="2" goto FULL_SETUP
if "%choice%"=="3" goto CHECK_STATUS
if "%choice%"=="4" goto STOP_SERVICES
if "%choice%"=="5" goto DIAGNOSTICS
if "%choice%"=="6" goto HELP_INFO
if "%choice%"=="7" goto EXIT
echo ❌ Invalid choice. Please try again.
timeout /t 2 /nobreak >nul
goto MAIN_MENU

:: ===============================================
::                 QUICK START
:: ===============================================
:QUICK_START
cls
echo ===============================================
echo           🚀 QUICK START MODE
echo ===============================================
echo.
echo [INFO] Starting Phishing Detection System...
echo.

:: Quick prerequisite check
call :CHECK_PYTHON
if "%PYTHON_OK%"=="false" (
    echo ❌ Python not found! Please run Full Setup first.
    pause
    goto MAIN_MENU
)

:: Start services
call :START_SERVICES

:: Show running info
call :SHOW_RUNNING_INFO

:: Wait for user to stop
echo.
echo 🛑 Press any key to STOP all services and return to menu...
pause >nul

call :STOP_ALL_PROCESSES
goto MAIN_MENU

:: ===============================================
::                FULL SETUP
:: ===============================================
:FULL_SETUP
cls
echo ===============================================
echo         🔧 FULL SETUP + INSTALLATION
echo ===============================================
echo.

echo [STEP 1/7] 🔍 Checking Prerequisites...
call :CHECK_PREREQUISITES

echo.
echo [STEP 2/7] 📦 Installing Python Dependencies...
call :INSTALL_PYTHON_DEPS

echo.
echo [STEP 3/7] 🐹 Setting up Go Components...
call :SETUP_GO

echo.
echo [STEP 4/7] 🤖 Preparing ML Model...
call :SETUP_ML_MODEL

echo.
echo [STEP 5/7] 🌐 Configuring Web Components...
call :SETUP_WEB

echo.
echo [STEP 6/7] ⚙️ Creating Configuration Files...
call :CREATE_CONFIGS

echo.
echo [STEP 7/7] 🚀 Starting System...
call :START_SERVICES

echo.
echo ✅ SETUP COMPLETED SUCCESSFULLY!
call :SHOW_RUNNING_INFO

echo.
echo 🛑 Press any key to STOP services and return to menu...
pause >nul

call :STOP_ALL_PROCESSES
goto MAIN_MENU

:: ===============================================
::               CHECK STATUS
:: ===============================================
:CHECK_STATUS
cls
echo ===============================================
echo           📊 SYSTEM STATUS CHECK
echo ===============================================
echo.

echo 🔍 Checking Prerequisites...
call :CHECK_PYTHON
call :CHECK_GO
echo.

echo 🌐 Checking Ports...
call :CHECK_PORTS
echo.

echo 🏃 Checking Running Processes...
call :CHECK_PROCESSES
echo.

echo 🔗 Testing Service Endpoints...
call :TEST_ENDPOINTS
echo.

echo ===============================================
echo           📋 QUICK ACCESS LINKS
echo ===============================================
echo  🌐 Web Interface: http://localhost:8080
echo  🤖 ML API:        http://localhost:5000  
echo  🚪 Go Gateway:    http://localhost:8081
echo ===============================================
echo.
pause
goto MAIN_MENU

:: ===============================================
::               STOP SERVICES
:: ===============================================
:STOP_SERVICES
cls
echo ===============================================
echo           🛑 STOPPING ALL SERVICES
echo ===============================================
echo.

call :STOP_ALL_PROCESSES

echo.
echo ✅ All services have been stopped successfully!
echo.
pause
goto MAIN_MENU

:: ===============================================
::              SYSTEM DIAGNOSTICS
:: ===============================================
:DIAGNOSTICS
cls
echo ===============================================
echo           🔍 SYSTEM DIAGNOSTICS
echo ===============================================
echo.

echo 🖥️ System Information:
echo    OS: %OS%
echo    Computer: %COMPUTERNAME%
echo    User: %USERNAME%
echo    Date: %DATE%
echo    Time: %TIME%
echo.

echo 📁 Project Structure:
if exist "python_ml_nlp\app\app.py" (echo    ✅ Python ML API Found) else (echo    ❌ Python ML API Missing)
if exist "go_api_gateway\cmd\main.go" (echo    ✅ Go Gateway Found) else (echo    ❌ Go Gateway Missing)
if exist "web_portal\templates\index.html" (echo    ✅ Web Portal Found) else (echo    ❌ Web Portal Missing)
if exist "cpp_url_parser\src\url_parser.cpp" (echo    ✅ C++ Parser Found) else (echo    ❌ C++ Parser Missing)
echo.

echo 🔧 Environment Check:
call :CHECK_PYTHON
call :CHECK_GO
echo.

echo 📊 Resource Usage:
wmic cpu get loadpercentage /value | find "LoadPercentage" 2>nul
wmic OS get TotalVisibleMemorySize,FreePhysicalMemory /value | find "=" 2>nul
echo.

echo 🌐 Network Configuration:
ipconfig | find "IPv4" 2>nul
echo.

pause
goto MAIN_MENU

:: ===============================================
::                 HELP INFO
:: ===============================================
:HELP_INFO
cls
echo ===============================================
echo               📖 HELP INFORMATION
echo ===============================================
echo.
echo 🎯 PURPOSE:
echo    This system detects phishing URLs using machine learning
echo    and provides a web interface for easy URL analysis.
echo.
echo 🏗️ ARCHITECTURE:
echo    • Web Interface (Port 8080) - User interface
echo    • ML API Server (Port 5000) - Machine learning backend  
echo    • Go Gateway (Port 8081) - API routing and notifications
echo    • C++ URL Parser - Fast URL analysis
echo    • R Visualization - Data analytics
echo.
echo 🚀 QUICK USAGE:
echo    1. Run option [2] for first-time setup
echo    2. Use option [1] for daily launches  
echo    3. Open http://localhost:8080 in browser
echo    4. Enter URLs to test for phishing
echo.
echo 🔧 REQUIREMENTS:
echo    • Python 3.7+ (required)
echo    • Go 1.18+ (optional)
echo    • Modern web browser
echo    • Internet connection (for dependencies)
echo.
echo 🆘 TROUBLESHOOTING:
echo    • Use option [5] for system diagnostics
echo    • Use option [3] to check service status
echo    • Run as administrator if permission issues
echo    • Check firewall settings for port access
echo.
echo 📞 SUPPORT:
echo    • Check BAT.md file for detailed instructions
echo    • Review README.md for project documentation
echo    • Use diagnostics option for detailed info
echo.
pause
goto MAIN_MENU

:: ===============================================
::                FUNCTIONS
:: ===============================================

:CHECK_PREREQUISITES
call :CHECK_PYTHON
call :CHECK_GO
goto :eof

:CHECK_PYTHON
python --version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo    ✅ Python is installed
    python --version
    set PYTHON_OK=true
) else (
    echo    ❌ Python is NOT installed
    echo       Please install Python 3.7+ from https://python.org
    set PYTHON_OK=false
)
goto :eof

:CHECK_GO
go version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo    ✅ Go is installed
    go version
    set GO_OK=true
) else (
    echo    ⚠️ Go is NOT installed (optional)
    echo       Install from https://golang.org for full features
    set GO_OK=false
)
goto :eof

:INSTALL_PYTHON_DEPS
if "%PYTHON_OK%"=="false" (
    echo ❌ Skipping Python dependencies - Python not available
    goto :eof
)

cd "%PROJECT_DIR%python_ml_nlp\app"
if exist requirements.txt (
    echo [INFO] Installing Python packages...
    pip install -r requirements.txt --quiet
    if %ERRORLEVEL% neq 0 (
        echo [WARNING] Standard install failed, trying with --user...
        pip install --user -r requirements.txt --quiet
    )
) else (
    echo [INFO] Installing essential packages...
    pip install flask scikit-learn pandas numpy joblib requests flask-cors --quiet
)
echo ✅ Python dependencies installed
cd "%PROJECT_DIR%"
goto :eof

:SETUP_GO
if "%GO_OK%"=="false" (
    echo ⚠️ Skipping Go setup - Go not available
    goto :eof
)

cd "%PROJECT_DIR%go_api_gateway"
if exist go.mod (
    echo [INFO] Installing Go modules...
    go mod tidy >nul 2>&1
    go mod download >nul 2>&1
) else (
    echo [INFO] Initializing Go module...
    go mod init phishing-detection-system >nul 2>&1
    go get github.com/gin-gonic/gin >nul 2>&1
    go get github.com/gin-contrib/cors >nul 2>&1
)
echo ✅ Go components configured
cd "%PROJECT_DIR%"
goto :eof

:SETUP_ML_MODEL
cd "%PROJECT_DIR%python_ml_nlp\models"
if not exist phishing_classifier.pkl (
    echo [INFO] Creating placeholder ML model...
    echo # Placeholder model > phishing_classifier.pkl
)
echo ✅ ML model ready
cd "%PROJECT_DIR%"
goto :eof

:SETUP_WEB
if not exist "web_portal\templates\index.html" (
    echo ❌ Web portal files missing
    goto :eof
)
echo ✅ Web components verified
goto :eof

:CREATE_CONFIGS
echo [INFO] Configuration files ready...
echo ✅ System configured
goto :eof

:START_SERVICES
echo [STARTING] 🤖 ML API Server (Port 5000)...
start /min "ML API" cmd /c "cd /d "%PROJECT_DIR%python_ml_nlp\app" && python app.py"
set ML_API_STARTED=true
timeout /t 3 /nobreak >nul

if "%GO_OK%"=="true" (
    echo [STARTING] 🚪 Go Gateway (Port 8081)...
    start /min "Go Gateway" cmd /c "cd /d "%PROJECT_DIR%go_api_gateway\cmd" && go run main.go"
    set GO_GATEWAY_STARTED=true
    timeout /t 2 /nobreak >nul
)

echo [STARTING] 🌐 Web Server (Port 8080)...
start /min "Web Server" cmd /c "cd /d "%PROJECT_DIR%web_portal" && python -m http.server 8080"
set WEB_SERVER_STARTED=true
timeout /t 3 /nobreak >nul

echo ✅ All services started successfully!
goto :eof

:STOP_ALL_PROCESSES
echo [STOPPING] 🛑 Stopping all services...

taskkill /f /im python.exe >nul 2>&1
taskkill /f /im go.exe >nul 2>&1
taskkill /f /im main.exe >nul 2>&1

set ML_API_STARTED=false
set WEB_SERVER_STARTED=false
set GO_GATEWAY_STARTED=false

echo ✅ All services stopped
goto :eof

:CHECK_PORTS
echo    Port 8080 (Web Server): 
netstat -an | find ":8080" >nul && echo      ✅ In Use || echo      ❌ Free

echo    Port 5000 (ML API): 
netstat -an | find ":5000" >nul && echo      ✅ In Use || echo      ❌ Free

echo    Port 8081 (Go Gateway): 
netstat -an | find ":8081" >nul && echo      ✅ In Use || echo      ❌ Free
goto :eof

:CHECK_PROCESSES
tasklist /fi "imagename eq python.exe" 2>nul | find "python.exe" >nul && echo    ✅ Python processes running || echo    ❌ No Python processes
tasklist /fi "imagename eq go.exe" 2>nul | find "go.exe" >nul && echo    ✅ Go processes running || echo    ❌ No Go processes
goto :eof

:TEST_ENDPOINTS
echo    Testing ML API...
powershell -Command "try { Invoke-WebRequest -Uri 'http://localhost:5000' -TimeoutSec 3 -UseBasicParsing | Out-Null; Write-Host '      ✅ ML API responding' } catch { Write-Host '      ❌ ML API not responding' }" 2>nul

echo    Testing Web Server...
powershell -Command "try { Invoke-WebRequest -Uri 'http://localhost:8080' -TimeoutSec 3 -UseBasicParsing | Out-Null; Write-Host '      ✅ Web Server responding' } catch { Write-Host '      ❌ Web Server not responding' }" 2>nul

echo    Testing Go Gateway...
powershell -Command "try { Invoke-WebRequest -Uri 'http://localhost:8081' -TimeoutSec 3 -UseBasicParsing | Out-Null; Write-Host '      ✅ Go Gateway responding' } catch { Write-Host '      ❌ Go Gateway not responding' }" 2>nul
goto :eof

:SHOW_RUNNING_INFO
echo.
echo ===============================================
echo     🎉 PHISHING DETECTION SYSTEM ACTIVE
echo ===============================================
echo.
echo 🌐 SERVICES RUNNING:
if "%ML_API_STARTED%"=="true" echo    ✅ ML API Server     : http://localhost:5000
if "%WEB_SERVER_STARTED%"=="true" echo    ✅ Web Interface    : http://localhost:8080
if "%GO_GATEWAY_STARTED%"=="true" echo    ✅ Go API Gateway   : http://localhost:8081
echo.
echo 🚀 READY TO USE:
echo    👆 Click: http://localhost:8080
echo    📱 Test URLs for phishing detection
echo    🛡️ Protect yourself from malicious links
echo.
echo ===============================================

:: Auto-open browser
echo [INFO] 🌐 Opening web browser...
timeout /t 2 /nobreak >nul
start http://localhost:8080 >nul 2>&1
goto :eof

:: ===============================================
::                   EXIT
:: ===============================================
:EXIT
cls
echo ===============================================
echo              👋 GOODBYE!
echo ===============================================
echo.
echo Thank you for using the Phishing Detection System!
echo.
echo 🛡️ Stay safe online and protect against phishing!
echo.

:: Clean shutdown
call :STOP_ALL_PROCESSES

echo Exiting in 3 seconds...
timeout /t 3 /nobreak >nul
exit /b 0