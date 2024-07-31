#!/bin/bash

# Define the necessary Python packages
PACKAGES="httpx beautifulsoup4"

# Update package list and install system packages
echo "Updating package list..."
sudo apt-get update -y

echo "Installing Python and system packages..."
sudo apt-get install -y python3 python3-pip tor

# Install Python packages
echo "Installing Python packages..."
pip3 install $PACKAGES

# Start Tor service
echo "Starting Tor service..."
sudo systemctl start tor

# Enable Tor to start on boot
echo "Enabling Tor to start on boot..."
sudo systemctl enable tor

echo "All dependencies have been installed and Tor service is started."

# Check if Tor service is running
echo "Checking Tor service status..."
sudo systemctl status tor | grep 'Active:'

echo "Installation and setup complete."
