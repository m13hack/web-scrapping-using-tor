#!/bin/bash

# Update package lists
sudo apt-get update

# Install Python3 and pip if they are not already installed
sudo apt-get install -y python3 python3-pip tor

# Install Python dependencies
pip3 install requests beautifulsoup4 stem pytorctl

# Check if Tor service is installed
if ! pgrep -x "tor" > /dev/null
then
    echo "Tor is not running. Starting Tor service..."
    sudo service tor start
else
    echo "Tor service is already running."
fi

echo "All dependencies have been installed."
