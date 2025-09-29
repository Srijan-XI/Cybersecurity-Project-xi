@echo off
REM Quick demo script for File Integrity Checker

echo ==================================================
echo         File Integrity Checker Demo
echo ==================================================
echo.

REM Create a test file
echo This is a test file for integrity checking. > test_demo.txt
echo Created test file: test_demo.txt
echo.

echo 1. Adding file to database...
call run.bat add "test_demo.txt"
echo.

echo 2. Checking file integrity (should pass)...
call run.bat check "test_demo.txt"
echo.

echo 3. Modifying the file...
echo This file has been modified! >> test_demo.txt
echo.

echo 4. Checking file integrity (should fail)...
call run.bat check "test_demo.txt"
echo.

echo 5. Updating the hash with new file content...
call run.bat update "test_demo.txt"
echo.

echo 6. Checking integrity again (should pass)...
call run.bat check "test_demo.txt"
echo.

echo Demo completed! Cleaning up...
del test_demo.txt
echo.
echo The File Integrity Checker is working correctly!
pause