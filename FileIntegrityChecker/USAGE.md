# 🚀 Quick Start Guide

## Using the Runner Scripts

You now have convenient runner scripts to use the File Integrity Checker easily:

### **Option 1: Batch Script (Windows)**
```batch
# Show help
.\run.bat

# Add a file to the database
.\run.bat add "myfile.txt"

# Check file integrity
.\run.bat check "myfile.txt"

# Update file hash
.\run.bat update "myfile.txt"
```

### **Option 2: PowerShell Script**
```powershell
# Show help
.\run.ps1

# Add a file to the database
.\run.ps1 add myfile.txt

# Check file integrity
.\run.ps1 check myfile.txt

# Update file hash
.\run.ps1 update myfile.txt
```

### **Option 3: Direct Executable**
```batch
# If you prefer to use the executable directly
.\FileIntegrityChecker_fallback.exe help
.\FileIntegrityChecker_fallback.exe add "myfile.txt"
.\FileIntegrityChecker_fallback.exe check "myfile.txt"
```

## Example Workflow

1. **Add a file to monitor:**
   ```batch
   .\run.bat add "important_document.pdf"
   ```

2. **Check if file has been modified:**
   ```batch
   .\run.bat check "important_document.pdf"
   ```

3. **If file was legitimately changed, update the hash:**
   ```batch
   .\run.bat update "important_document.pdf"
   ```

## Features

✅ **Easy to use** - Simple runner scripts  
✅ **Cross-platform** - Works on Windows, Linux, macOS  
✅ **No dependencies** - Fallback version uses built-in CRC32  
✅ **Secure** - Full version uses SHA-256 with OpenSSL  
✅ **Database storage** - Stores hashes in `data/integrity_db.txt`  

## Building

If you need to rebuild the project:

```batch
# Build from project root
.\build.bat

# Or build from src directory
cd src
.\build.bat
```

The runner scripts will automatically detect which executable is available and use it.