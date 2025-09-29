# Test script for File Integrity Checker
# PowerShell version

Write-Host "🧪 Testing File Integrity Checker..." -ForegroundColor Cyan

# Test variables
$testFile = "test_file.txt"
$testContent = "This is a test file for integrity checking.`nLine 2 of the test file."
$modifiedContent = "This is a MODIFIED test file for integrity checking.`nLine 2 of the test file."

# Clean up any existing test files
if (Test-Path $testFile) { Remove-Item $testFile }
if (Test-Path "data/integrity_db.txt") { Remove-Item "data/integrity_db.txt" }

# Function to run tests
function Test-Command {
    param($Description, $Command, $ExpectedExitCode = 0)
    
    Write-Host "`n📋 Test: $Description" -ForegroundColor Yellow
    Write-Host "Command: $Command" -ForegroundColor Gray
    
    try {
        $result = Invoke-Expression $Command
        $exitCode = $LASTEXITCODE
        
        if ($exitCode -eq $ExpectedExitCode) {
            Write-Host "✅ PASSED" -ForegroundColor Green
        } else {
            Write-Host "❌ FAILED (Exit code: $exitCode, Expected: $ExpectedExitCode)" -ForegroundColor Red
        }
        
        if ($result) {
            Write-Host "Output: $result" -ForegroundColor Gray
        }
    } catch {
        Write-Host "❌ FAILED (Exception: $($_.Exception.Message))" -ForegroundColor Red
    }
}

# Create test file
Write-Host "`n🔧 Setting up test environment..." -ForegroundColor Cyan
$testContent | Out-File -FilePath $testFile -Encoding UTF8

# Test 1: Help command
Test-Command "Help command" "./FileIntegrityChecker_fallback.exe help"

# Test 2: Add file
Test-Command "Add file to database" "./FileIntegrityChecker_fallback.exe add `"$testFile`""

# Test 3: Check integrity (should pass)
Test-Command "Check file integrity (should pass)" "./FileIntegrityChecker_fallback.exe check `"$testFile`""

# Test 4: Check integrity of non-existent file (should fail)
Test-Command "Check non-existent file (should fail)" "./FileIntegrityChecker_fallback.exe check `"nonexistent.txt`"" 1

# Test 5: Modify file and check integrity (should fail)
Write-Host "`n🔧 Modifying test file..." -ForegroundColor Cyan
$modifiedContent | Out-File -FilePath $testFile -Encoding UTF8
Test-Command "Check modified file integrity (should fail)" "./FileIntegrityChecker_fallback.exe check `"$testFile`"" 1

# Test 6: Update file hash
Test-Command "Update file hash" "./FileIntegrityChecker_fallback.exe update `"$testFile`""

# Test 7: Check integrity after update (should pass)
Test-Command "Check file integrity after update (should pass)" "./FileIntegrityChecker_fallback.exe check `"$testFile`""

# Test 8: Try to add existing file (should fail)
Test-Command "Try to add existing file (should fail)" "./FileIntegrityChecker_fallback.exe add `"$testFile`"" 1

# Test 9: Invalid command
Test-Command "Invalid command (should fail)" "./FileIntegrityChecker_fallback.exe invalid" 1

# Test 10: No arguments
Test-Command "No arguments (should fail)" "./FileIntegrityChecker_fallback.exe" 1

# Check database contents
Write-Host "`n📄 Database contents:" -ForegroundColor Cyan
if (Test-Path "data/integrity_db.txt") {
    Get-Content "data/integrity_db.txt" | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }
} else {
    Write-Host "  Database file not found" -ForegroundColor Red
}

# Clean up
Write-Host "`n🧹 Cleaning up..." -ForegroundColor Cyan
if (Test-Path $testFile) { Remove-Item $testFile }

Write-Host "`n✅ Testing completed!" -ForegroundColor Green
Read-Host "Press Enter to continue..."