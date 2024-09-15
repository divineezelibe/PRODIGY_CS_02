@echo off
setlocal enabledelayedexpansion

echo ==============================
echo      Welcome to PixCrypt
echo  Developed by Divine E. Ezelibe
echo ==============================
echo This setup script will install the required Python dependencies for PixCrypt.
echo.
echo Let's begin the installation process!
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
python -m pip install -r requirements.txt
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
