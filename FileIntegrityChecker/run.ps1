# Simple runner script for File Integrity Checker
param([string[]]$Arguments)

# Check if executable exists
$executable = $null
if (Test-Path "FileIntegrityChecker_fallback.exe") {
    $executable = "FileIntegrityChecker_fallback.exe"
} elseif (Test-Path "FileIntegrityChecker.exe") {
    $executable = "FileIntegrityChecker.exe"
} else {
    Write-Host "Error: No executable found!" -ForegroundColor Red
    Write-Host "Please build the project first." -ForegroundColor Yellow
    exit 1
}

# If no arguments, show help
if ($Arguments.Count -eq 0) {
    Write-Host "File Integrity Checker - PowerShell Runner" -ForegroundColor Cyan
    Write-Host "Using: $executable" -ForegroundColor Green
    Write-Host ""
    & ".\$executable" help
    Write-Host ""
    Write-Host "Usage: .\run.ps1 <command> <filepath>" -ForegroundColor Cyan
    Write-Host "Examples:" -ForegroundColor Gray
    Write-Host "  .\run.ps1 add myfile.txt" -ForegroundColor Gray
    Write-Host "  .\run.ps1 check myfile.txt" -ForegroundColor Gray
    Write-Host "  .\run.ps1 update myfile.txt" -ForegroundColor Gray
    exit 0
}

# Execute with arguments
Write-Host "Running: $executable $($Arguments -join ' ')" -ForegroundColor Gray
& ".\$executable" @Arguments

if ($LASTEXITCODE -eq 0) {
    Write-Host "Command completed successfully!" -ForegroundColor Green
} else {
    Write-Host "Command failed with exit code: $LASTEXITCODE" -ForegroundColor Red
}