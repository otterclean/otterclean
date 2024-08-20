#!/bin/bash

# Check if virtual environment directory exists
if [ ! -d "venv" ]; then
    # Create virtual environment
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate virtual environment
source venv/bin/activate
echo "Virtual environment activated."

# Install dependencies
pip install -r requirements.txt
echo "Dependencies installed."

# Run the program
python3 system_cleanup.py

# Deactivate virtual environment after running
deactivate
