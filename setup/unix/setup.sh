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
    local spinstr='|/-\'  # Spinner characters
    local temp

    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        temp="${spinstr#?}${spinstr%?}"
        printf " [%c]  " "$temp" "\r"
        sleep $delay
    done
    printf "    \r"
}

# Script Description
echo "*************************************************"
echo "*                                               *"
echo "*            Welcome to PixCrypt Setup         *"
echo "*                                               *"
echo "*  This script will clone the PixCrypt repository, *"
echo "*  set up your environment, and install all       *"
echo "*  necessary dependencies. Thank you for trying  *"
echo "*  PixCrypt! This is the installation phase.      *"
echo "*                                               *"
echo "*************************************************"
echo ""

# Clone the PixCrypt repository
echo "Cloning the PixCrypt repository..."
git clone https://github.com/divineezelibe/PRODIGY_CS_02.git &> /dev/null &
show_spinner $!

# Change to the project directory
echo "Changing directory to PixCrypt..."
cd PRODIGY_CS_02 || error_exit "Failed to change directory to PRODIGY_CS_02."

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
if [ -f "requirements.txt" ]; then
    python3 -m pip install -r "requirements.txt" &> /dev/null &
    show_spinner $!
else
    error_exit "requirements.txt file not found. Ensure that this file is present in the correct directory."
fi

echo ""
echo "Setup complete. All dependencies have been installed successfully."

# End of script
