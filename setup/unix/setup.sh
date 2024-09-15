#!/bin/bash

# Function to display a message and exit with an error code
function error_exit {
    echo "$1" >&2
    exit 1
}

# Script Description
echo "*************************************************"
echo "*                                               *"
echo "*         Setup Script for Python Project       *"
echo "*                                               *"
echo "* This script sets up the environment for       *"
echo "* a Python project by installing required       *"
echo "* packages and dependencies. It ensures that     *"
echo "* Python3, pip, and any necessary Python         *"
echo "* libraries specified in requirements.txt are   *"
echo "* installed and up-to-date.                     *"
echo "*                                               *"
echo "*************************************************"

# Update package list
echo "Updating package list..."
sudo apt-get update || error_exit "Failed to update package list. Please check your network connection and try again."

# Install Python and pip if they are not already installed
echo "Checking for Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Installing Python3..."
    sudo apt-get install -y python3 python3-pip || error_exit "Failed to install Python3 and pip. Please check your package manager and try again."
else
    echo "Python3 is already installed."
fi

# Upgrade pip to the latest version
echo "Upgrading pip..."
python3 -m pip install --upgrade pip || error_exit "Failed to upgrade pip. Ensure you have the necessary permissions or check your network connection."

# Install required Python packages from requirements.txt
echo "Installing required Python packages..."
if [ -f requirements.txt ]; then
    python3 -m pip install -r requirements.txt || error_exit "Failed to install Python packages. Please check the requirements.txt file for accuracy."
else
    error_exit "requirements.txt file not found. Ensure that this file is present in the current directory."
fi

echo "Setup complete. All dependencies have been installed successfully."

# End of script
