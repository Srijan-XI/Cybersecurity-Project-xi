# Simple build script for src directory
Write-Host "Building File Integrity Checker from src directory..." -ForegroundColor Cyan

# Go to project root
Set-Location ..

# Create directories if needed
if (!(Test-Path "data")) { 
    New-Item -ItemType Directory -Path "data" 
}

# Try fallback version (more reliable)
Write-Host "Building fallback version..." -ForegroundColor Yellow

$buildCommand = "g++ -std=c++17 -I include src/main_fallback.cpp src/FileManager.cpp src/FileHasherFallback.cpp -o FileIntegrityChecker_fallback.exe"

try {
    Invoke-Expression $buildCommand
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Build successful!" -ForegroundColor Green
        Write-Host "Testing..." -ForegroundColor Gray
        ./FileIntegrityChecker_fallback.exe help
    } else {
        Write-Host "Build failed. Check that g++ is installed." -ForegroundColor Red
    }
} catch {
    Write-Host "Build failed. Check that g++ is installed." -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
}

# Return to src directory
Set-Location src

Write-Host ""
Write-Host "To use the program, go back to the project root:" -ForegroundColor Cyan
Write-Host "  cd .." -ForegroundColor Gray
Write-Host "  ./FileIntegrityChecker_fallback.exe help" -ForegroundColor Gray