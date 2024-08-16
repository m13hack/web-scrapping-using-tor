#!/bin/bash

# Define the necessary Python packages
PACKAGES="httpx beautifulsoup4 socksio colorama"

# Function to check command success
check_command() {
    if [ $? -ne 0 ]; then
        echo -e "\033[31mError: $1 failed.\033[0m"
        exit 1
    fi
}

# Update package list and install system packages
echo "Updating package list..."
sudo apt-get update -y
check_command "Updating package list"

echo "Installing Python and system packages..."
sudo apt-get install -y python3 python3-pip tor
check_command "Installing Python and system packages"

# Install Python packages
echo "Installing Python packages..."
pip3 install $PACKAGES
check_command "Installing Python packages"

# Start Tor service
echo "Starting Tor service..."
sudo systemctl start tor
check_command "Starting Tor service"

# Enable Tor to start on boot
echo "Enabling Tor to start on boot..."
sudo systemctl enable tor
check_command "Enabling Tor to start on boot"

echo "All dependencies have been installed and Tor service is started."

# Check if Tor service is running
echo "Checking Tor service status..."
sudo systemctl status tor | grep 'Active:'
check_command "Checking Tor service status"

echo "Installation and setup complete."
