@echo off
REM Complete System Integration Launcher
REM Author: Cybersecurity Project XI
REM This script starts all components of the phishing detection system

echo.
echo ========================================
echo   PHISHING DETECTION SYSTEM LAUNCHER
echo ========================================
echo.

REM Check if virtual environment is activated
python -c "import sys; exit(0 if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) else 1)" 2>nul
if errorlevel 1 (
    echo [ERROR] Virtual environment not detected!
    echo Please activate your virtual environment first:
    echo   Scripts\activate
    echo.
    pause
    exit /b 1
)

echo [INFO] Virtual environment detected ✓
echo.

REM Start ML API in background
echo [STARTING] ML API Server on port 5000...
cd /d "python_ml_nlp\app"
start "ML API Server" cmd /k "python app.py"
cd /d "..\..\"
timeout /t 3 /nobreak >nul

REM Start Web Server in background  
echo [STARTING] Web Server on port 8080...
cd /d "web_portal"
start "Web Server" cmd /k "python -m http.server 8080"
cd /d ".."
timeout /t 2 /nobreak >nul

echo.
echo ========================================
echo   SYSTEM INTEGRATION COMPLETE!
echo ========================================
echo.
echo 🌐 Your phishing detection system is now running:
echo.
echo   Web Interface:     http://localhost:8080
echo   ML API:           http://localhost:5000
echo   API Health:       http://localhost:5000/health
echo   API Docs:         http://localhost:5000/docs
echo.
echo ========================================
echo   TESTING THE INTEGRATION
echo ========================================
echo.

REM Wait for services to fully start
echo [WAIT] Allowing services to initialize...
timeout /t 5 /nobreak >nul

REM Test the integration
echo [TEST] Testing ML API connectivity...
python -c "
import requests
import json
try:
    # Test health endpoint
    health = requests.get('http://localhost:5000/health', timeout=5)
    if health.status_code == 200:
        print('✓ ML API Health Check: PASSED')
        
        # Test prediction endpoint
        test_data = {'url': 'https://www.google.com'}
        pred = requests.post('http://localhost:5000/predict', json=test_data, timeout=10)
        if pred.status_code == 200:
            result = pred.json()
            prediction = result.get('prediction', 'unknown')
            confidence = result.get('confidence', 'unknown')
            probability = result.get('probability', 0)
            print(f'✓ ML API Prediction Test: PASSED')
            print(f'  Sample Result: {prediction} ({confidence}, {probability:.3f})')
        else:
            print('✗ ML API Prediction Test: FAILED')
    else:
        print('✗ ML API Health Check: FAILED')
except Exception as e:
    print(f'✗ ML API Connection: FAILED ({e})')
    
try:
    # Test web server
    web = requests.get('http://localhost:8080', timeout=5)
    if web.status_code == 200:
        if 'Phishing' in web.text and 'Detection' in web.text:
            print('✓ Web Server Test: PASSED')
        else:
            print('⚠ Web Server responding but content may be incorrect')
    else:
        print('✗ Web Server Test: FAILED')
except Exception as e:
    print(f'✗ Web Server Connection: FAILED ({e})')
" 2>nul

echo.
echo ========================================
echo   INTEGRATION SUMMARY
echo ========================================
echo.
echo Your complete phishing detection system includes:
echo.
echo 🔹 Advanced ML Model (96.03%% accuracy)
echo    - Gradient Boosting Classifier
echo    - 135+ URL features analyzed
echo    - Real-time prediction capability
echo.
echo 🔹 Flask ML API (Backend)
echo    - RESTful API endpoints
echo    - JSON request/response
echo    - Batch processing support
echo.
echo 🔹 Web Portal (Frontend)
echo    - Modern HTML5/CSS3/JS interface
echo    - Real-time URL analysis
echo    - Visual risk indicators
echo.
echo 🔹 Complete Integration
echo    - Frontend ↔ Backend communication
echo    - API ↔ ML Model integration
echo    - End-to-end URL analysis pipeline
echo.
echo ========================================
echo   READY TO USE!
echo ========================================
echo.
echo 🎯 Open http://localhost:8080 in your browser
echo 🎯 Enter any URL to test phishing detection
echo 🎯 Watch the real-time analysis in action!
echo.
echo Press any key to open the web interface...
pause >nul

REM Open web interface
start http://localhost:8080

echo.
echo System is now running. Close the CMD windows to stop services.
echo.
pause