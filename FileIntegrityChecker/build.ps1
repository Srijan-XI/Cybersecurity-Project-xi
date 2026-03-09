# PowerShell build script for File Integrity Checker

Write-Host "🛡️  Building File Integrity Checker..." -ForegroundColor Cyan

# Create directories if they don't exist
if (!(Test-Path "obj")) { New-Item -ItemType Directory -Path "obj" }
if (!(Test-Path "data")) { New-Item -ItemType Directory -Path "data" }

# Check for OpenSSL installation
$opensslPaths = @(
    "C:\vcpkg\installed\x64-windows",
    "C:\OpenSSL-Win64",
    "C:\Program Files\OpenSSL-Win64"
)

$opensslPath = $null
foreach ($path in $opensslPaths) {
    if (Test-Path -Path "$path\include\openssl\sha.h") {
        $opensslPath = $path
        break
    }
}

if ($opensslPath) {
    Write-Host "✓ Found OpenSSL at: $opensslPath" -ForegroundColor Green
    $includeFlag = "-I`"$opensslPath\include`""
    $libFlag = "-L`"$opensslPath\lib`" -lssl -lcrypto"
} else {
    Write-Host "⚠️  OpenSSL not found in common locations. Trying default paths..." -ForegroundColor Yellow
    $includeFlag = ""
    $libFlag = "-lssl -lcrypto"
}

# Build command
$buildCmd = "g++ -std=c++17 -Wall -Wextra -I include $includeFlag src/*.cpp -o FileIntegrityChecker.exe $libFlag"

Write-Host "Executing: $buildCmd" -ForegroundColor Gray

try {
    Invoke-Expression $buildCmd
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Build successful! Executable: FileIntegrityChecker.exe" -ForegroundColor Green
        
        # Test the executable
        if (Test-Path "FileIntegrityChecker.exe") {
            Write-Host "`n🧪 Testing executable..." -ForegroundColor Cyan
            ./FileIntegrityChecker.exe help
        }
    } else {
        throw "Compilation failed with exit code $LASTEXITCODE"
    }
} catch {
    Write-Host "❌ Build failed!" -ForegroundColor Red
    Write-Host "Please ensure:" -ForegroundColor Yellow
    Write-Host "  1. MinGW-w64 or MSYS2 with g++ is installed" -ForegroundColor Yellow
    Write-Host "  2. OpenSSL development libraries are available" -ForegroundColor Yellow
    Write-Host "  3. vcpkg install openssl:x64-windows (if using vcpkg)" -ForegroundColor Yellow
    Write-Host "  4. All source files are present and accessible" -ForegroundColor Yellow
}

Read-Host "`nPress Enter to continue..."