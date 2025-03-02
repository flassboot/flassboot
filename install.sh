
#!/bin/bash

echo "Starting installation..."

# Update system
sudo apt-get update -y

# Install Python and pip
sudo apt-get install python3 python3-pip -y

# Install virtual environment
pip3 install virtualenv

# Create and activate virtual environment
virtualenv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Set permissions for .env file
chmod 644 .env

# Make install.sh executable
chmod +x install.sh

echo "Installation complete!"
