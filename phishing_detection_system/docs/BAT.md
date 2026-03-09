# 🚀 Phishing Detection System - Batch File Setup Guide

## 📋 Overview

This guide explains how to use the automated batch files to set up and run your Phishing Detection System with just one click. The system includes multiple batch files for different purposes, making it easy to manage your cybersecurity project.

## 📁 Batch File Included

### � All-in-One Solution
- **`RUN.bat`** - Complete system launcher with menu-driven interface

## 🚀 Quick Start Instructions

### Step 1: Launch the System
1. Navigate to your project folder: `phishing detection system`
2. **Double-click** on `RUN.bat`
3. **Select option [2]** for first-time setup (or [1] for daily use)
4. Wait for the automated setup to complete
5. Your browser will open automatically to `http://localhost:8080`

### Step 2: Menu Options
- **[1] Quick Start** - Daily use launcher (fast startup)
- **[2] Full Setup** - Complete first-time setup and launch
- **[3] Check Status** - System health monitoring
- **[4] Stop Services** - Clean shutdown of all services
- **[5] Diagnostics** - Detailed system information
- **[6] Help Info** - Usage instructions and troubleshooting
- **[7] Exit** - Safe exit with cleanup

## 📖 Detailed Menu Options

### 🔍 What Each Option Does

#### [1] Quick Start
- ✅ Fast service startup (assumes setup complete)
- ✅ Launches ML API, Web Server, and Go Gateway
- ✅ Opens browser automatically

#### [2] Full Setup
- ✅ Verifies Python installation (3.7+)
- ✅ Checks Go installation (optional)
- ✅ Installs Python dependencies from requirements.txt
- ✅ Downloads Go modules if available
- ✅ Sets up ML model and training environment
- ✅ Launches all services with monitoring

#### [3] Check Status
- 🔍 Monitors all service ports (5000, 8080, 8081)
- 🔍 Shows running/stopped status
- 🔍 Tests basic connectivity
- 🔍 Displays system health information

#### [4] Stop Services
- 🛑 Gracefully stops all running services
- � Kills any hanging processes on ports 5000, 8080, 8081
- 🛑 Cleans up temporary files and connections

#### [5] Diagnostics
- 🔧 Comprehensive system information
- 🔧 Port usage analysis
- 🔧 Service dependency checks
- 🔧 Error log review

#### [6] Help Info
- 📚 Usage instructions and best practices
- 📚 Troubleshooting guide
- 📚 System requirements
- 📚 Feature explanations

## 🎯 System Architecture

### Services Started
| Service | Port | Purpose |
|---------|------|---------|
| **Web Interface** | 8080 | Main user interface |
| **ML API Server** | 5000 | Machine learning backend |
| **Go API Gateway** | 8081 | API routing (optional) |

### Service Flow
```
User → Web Interface (8080) → ML API (5000) → Phishing Detection
                            ↘ Go Gateway (8081) ↗
```

## 🛠️ Troubleshooting

### Common Issues & Solutions

#### ❌ "Python is not installed"
**Solution:**
1. Download Python from https://python.org
2. During installation, check "Add Python to PATH"
3. Restart your computer
4. Run `setup_and_run.bat` again

#### ❌ "Permission denied" errors
**Solution:**
1. Right-click on the batch file
2. Select "Run as administrator"
3. Allow the script to make changes

#### ❌ "Port already in use"
**Solution:**
1. Run `stop_services.bat` to clean up
2. Check `check_status.bat` for running services
3. Restart your computer if needed
4. Try `quick_start.bat` again

#### ❌ Dependencies installation fails
**Solution:**
```batch
# Try manual installation
pip install --user -r requirements.txt
# Or upgrade pip first
python -m pip install --upgrade pip
```

## 📊 System Monitoring

### Using `check_status.bat`
This script provides comprehensive system monitoring:

#### Process Status
- 🐍 Python services status
- 🐹 Go services status  
- 🌐 Port availability (8080, 5000, 8081)

#### Health Checks
- ✅ Service endpoint testing
- 📡 Network connectivity
- 🔍 Response verification

#### Sample Output
```
===============================================
     PHISHING DETECTION SYSTEM - STATUS
===============================================

🐍 Python Services:
   ✅ Python processes are running

🌐 Port Status:
   ✅ Port 8080 is in use
   ✅ Port 5000 is in use

🔍 Service Health Check:
   ✅ ML API is responding
   ✅ Web Server is responding
```

## 🎮 Usage Workflows

### Development Workflow
```
1. setup_and_run.bat     (First time only)
2. quick_start.bat       (Daily development)
3. check_status.bat      (Monitor health)
4. stop_services.bat     (Clean shutdown)
```

### Testing Workflow  
```
1. quick_start.bat       (Start system)
2. Test URLs in browser  (http://localhost:8080)
3. check_status.bat      (Verify all services)
4. stop_services.bat     (Clean exit)
```

### Demo Workflow
```
1. setup_and_run.bat     (Fresh setup)
2. Browser opens automatically
3. Demo phishing detection
4. Press any key to stop
```

## ⚙️ Advanced Configuration

### Manual Service Control

#### Start Individual Services
```batch
# ML API only
cd python_ml_nlp\app
python app.py

# Web server only  
cd web_portal
python -m http.server 8080

# Go gateway only (if available)
cd go_api_gateway\cmd
go run main.go
```

#### Custom Port Configuration
Edit the batch files to change default ports:
- Web Server: Change `8080` to desired port
- ML API: Change `5000` to desired port
- Go Gateway: Change `8081` to desired port

### Environment Variables
Set these for custom configuration:
```batch
set ML_API_PORT=5000
set WEB_SERVER_PORT=8080
set GO_GATEWAY_PORT=8081
```

## 🔒 Security Considerations

### Firewall Settings
- Allow Python through Windows Firewall
- Allow Go applications if using Go gateway
- Ports 5000, 8080, 8081 should be accessible locally

### Network Access
- Services run on `localhost` by default
- For network access, modify host settings in service files
- Use caution when exposing services to network

## 📝 Logs & Debugging

### Log Locations
- **Python logs**: Console output in ML API window
- **Go logs**: Console output in Go Gateway window
- **Web server logs**: HTTP server console

### Debug Mode
Enable verbose logging by modifying service files:
```python
# In app.py
app.run(debug=True, host='localhost', port=5000)
```

## 🔄 Updates & Maintenance

### Updating Dependencies
```batch
# Update Python packages
pip install --upgrade -r requirements.txt

# Update Go modules
go get -u ./...
go mod tidy
```

### Cleaning Up
```batch
# Stop all services
stop_services.bat

# Clean Python cache
rmdir /s __pycache__

# Clean Go build cache
go clean -cache
```

## 🆘 Support & Help

### Getting Help
1. Check `check_status.bat` for system status
2. Review console output for error messages
3. Ensure all prerequisites are installed
4. Try running as administrator

### Common Commands
```batch
# Check Python version
python --version

# Check Go version  
go version

# Test network connectivity
ping localhost

# Check port usage
netstat -an | find ":8080"
```

## 🎉 Success Indicators

You know the system is working when:
- ✅ Browser opens automatically to http://localhost:8080
- ✅ You see the "Phishing URL Detector" interface
- ✅ You can enter URLs and get analysis results
- ✅ `check_status.bat` shows all services running
- ✅ No error messages in console windows

## 📞 Next Steps

After successful setup:
1. 🧪 **Test the system** with known safe/malicious URLs
2. 🎯 **Train your model** with custom data
3. 🔧 **Customize the interface** as needed
4. 📊 **Monitor performance** using status checks
5. 🚀 **Deploy to production** environment if desired

---

**🛡️ Happy Phishing Detection!** 

Your cybersecurity system is now fully automated and ready to protect users from malicious URLs.