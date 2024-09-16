@echo off
setlocal enabledelayedexpansion

:: Set the path to requirements.txt file
set "REQUIREMENTS_PATH=%~dp0..\requirements.txt"

:: Resolve the absolute path
for %%i in ("%REQUIREMENTS_PATH%") do set "REQUIREMENTS_PATH=%%~fi"

echo ==============================
echo      Welcome to PixCrypt
echo  Developed by Divine E. Ezelibe
echo ==============================
echo PixCrypt: A tool for secure image encryption and decryption.
echo Thank you for trying PixCrypt!
echo This is the installation phase.
echo.
echo Let's begin the setup process!
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Python is not installed on your system.
    echo Please download and install Python from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo.
echo Python is installed! Version:
python --version
echo.
pause

REM Upgrade pip to the latest version
echo.
echo ==============================
echo Upgrading pip to the latest version...
echo ==============================
python -m pip install --upgrade pip
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: An issue occurred while upgrading pip.
    pause
    exit /b 1
)
echo Pip has been successfully upgraded.
echo.
pause

REM Install required Python packages
echo.
echo ==============================
echo Installing required packages for PixCrypt...
echo ==============================
python -m pip install -r "%REQUIREMENTS_PATH%"
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: An issue occurred while installing dependencies.
    pause
    exit /b 1
)
echo.
echo All required packages for PixCrypt have been successfully installed.
echo.
pause

echo ==============================
echo Setup complete!
echo PixCrypt is now ready to use.
echo ==============================
pause
