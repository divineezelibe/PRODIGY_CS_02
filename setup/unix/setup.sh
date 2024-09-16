#!/bin/bash

# Function to display a message and exit with an error code
function error_exit {
    echo "$1" >&2
    exit 1
}

# Function to show a spinner while a process is running
function show_spinner {
    local pid=$1
    local delay=0.1
    local spinstr='|/-\' 
    local temp

    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        temp="${spinstr#?}${spinstr%?}"
        printf " [%c]  " "$temp" "\r"
        sleep $delay
    done
    printf "    \r"
}

# Path to the requirements.txt file
REQUIREMENTS_FILE="./requirements.txt"

# Script Description
echo "*************************************************"
echo "*                                               *"
echo "*         Welcome to PixCrypt Setup Script      *"
echo "*                                               *"
echo "* PixCrypt: A tool for secure image encryption  *"
echo "* and decryption. Thank you for trying PixCrypt!*"
echo "* This is the installation phase.               *"
echo "*                                               *"
echo "*************************************************"
echo ""

# Update package list
echo "Updating package list..."
sudo apt-get update &> /dev/null &
show_spinner $!

# Install Python and pip if they are not already installed
echo "Checking for Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Installing Python3..."
    sudo apt-get install -y python3 python3-pip &> /dev/null &
    show_spinner $!
else
    echo "Python3 is already installed."
fi

# Upgrade pip to the latest version
echo "Upgrading pip..."
python3 -m pip install --upgrade pip &> /dev/null &
show_spinner $!

# Install required Python packages from requirements.txt
echo "Installing required Python packages..."
if [ -f "$REQUIREMENTS_FILE" ]; then
    python3 -m pip install -r "$REQUIREMENTS_FILE" &> /dev/null &
    show_spinner $!
else
    error_exit "requirements.txt file not found at $REQUIREMENTS_FILE. Ensure that this file is present in the correct directory."
fi

echo ""
echo "Setup complete. All dependencies have been installed successfully."

# End of script
