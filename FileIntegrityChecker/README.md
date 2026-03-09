# 🛡️ File Integrity Checker

A C++ based File Integrity Checker that uses cryptographic hashing algorithms to verify file integrity. Designed for cybersecurity monitoring tools, this utility can detect unauthorized changes to critical files.

## ✨ Features

- **SHA-256 Hashing**: Uses OpenSSL's SHA-256 for secure cryptographic hashing (main version)
- **CRC32 Fallback**: Alternative version with CRC32 hashing (no external dependencies)
- **Persistent Database**: Stores file hashes in a simple text-based database
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Easy CLI Interface**: Simple command-line interface for all operations
- **Error Handling**: Comprehensive error handling and validation

## 🚀 Quick Start

### Building (OpenSSL Version)

#### Windows (with vcpkg)
```bash
# Install OpenSSL via vcpkg
vcpkg install openssl:x64-windows

# Build using PowerShell script
.\build.ps1

# Or build manually
g++ -std=c++17 -I include -I"C:\vcpkg\installed\x64-windows\include" src/*.cpp -L"C:\vcpkg\installed\x64-windows\lib" -lssl -lcrypto -o FileIntegrityChecker.exe
```

#### Linux/macOS
```bash
# Install OpenSSL development libraries
# Ubuntu/Debian: sudo apt-get install libssl-dev
# CentOS/RHEL: sudo yum install openssl-devel
# macOS: brew install openssl

# Build using Makefile
make

# Or build manually
g++ -std=c++17 -I include src/*.cpp -lssl -lcrypto -o FileIntegrityChecker
```

### Building (Fallback Version - No OpenSSL Required)

```bash
# Windows
.\build_fallback.bat

# Linux/macOS
g++ -std=c++17 -I include src/main_fallback.cpp src/FileManager.cpp src/FileHasherFallback.cpp -o FileIntegrityChecker_fallback
```

## 📖 Usage

```bash
# Add a file to the integrity database
FileIntegrityChecker add "path/to/file.txt"

# Check file integrity
FileIntegrityChecker check "path/to/file.txt"

# Update stored hash for an existing file
FileIntegrityChecker update "path/to/file.txt"

# Show help
FileIntegrityChecker help
```

## 🛠️ Build Options

| Build Method | Description | Requirements |
|--------------|-------------|--------------|
| CMake | Cross-platform build system | CMake 3.16+, OpenSSL |
| Makefile | Traditional Unix build | Make, OpenSSL |
| PowerShell Script | Windows automated build | PowerShell, MinGW/MSYS2, OpenSSL |
| Batch Script | Windows simple build | MinGW/MSYS2, OpenSSL |
| Fallback Build | No external dependencies | Just a C++17 compiler |

## 🔧 Project Structure

```
FileIntegrityChecker/
├── include/
│   ├── FileHasher.h              # SHA-256 hasher (OpenSSL)
│   ├── FileHasherFallback.h      # CRC32 hasher (no deps)
│   ├── FileManager.h             # Database management
│   └── IntegrityChecker.h        # Integrity verification
├── src/
│   ├── main.cpp                  # Main program (OpenSSL version)
│   ├── main_fallback.cpp         # Main program (fallback version)
│   ├── FileHasher.cpp            # SHA-256 implementation
│   ├── FileHasherFallback.cpp    # CRC32 implementation
│   ├── FileManager.cpp           # Database operations
│   └── IntegrityChecker.cpp      # Integrity checking logic
├── data/                         # Database storage directory
├── CMakeLists.txt               # CMake build configuration
├── Makefile                     # Make build configuration
├── build.ps1                    # PowerShell build script
├── build.bat                    # Windows batch build script
├── build_fallback.bat           # Fallback version build script
└── README.md                    # This file
```

## 🔒 Security Notes

- **Production Use**: Always use the OpenSSL version with SHA-256 for production environments
- **Fallback Version**: The CRC32 fallback is suitable for development/testing but not cryptographically secure
- **Database Protection**: Store the integrity database in a secure location
- **Regular Updates**: Regularly update stored hashes for files that legitimately change

## 🐛 Fixes Applied

### Code Quality Improvements
- ✅ Fixed C++17 structured binding compatibility
- ✅ Added comprehensive error handling and validation
- ✅ Improved command-line argument processing
- ✅ Added missing standard library includes
- ✅ Enhanced file validation in hash calculations

### Build System Enhancements
- ✅ Created CMake configuration for cross-platform builds
- ✅ Added Makefile with dependency installation targets
- ✅ Created Windows PowerShell and batch build scripts
- ✅ Implemented fallback build system (no OpenSSL required)

### User Experience Improvements
- ✅ Enhanced help messages with examples
- ✅ Added colored output indicators (✓/✗)
- ✅ Improved error messages with context
- ✅ Added automatic directory creation
- ✅ Better database validation and error reporting

### Platform Compatibility
- ✅ Windows path handling improvements
- ✅ Cross-platform build configurations
- ✅ Multiple compiler toolchain support
- ✅ Dependency detection and installation guidance

---