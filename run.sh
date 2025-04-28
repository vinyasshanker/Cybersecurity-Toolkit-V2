#!/bin/bash


if ! command -v seclists &> /dev/null; then
    echo "SecLists is not installed. Please install it first."
    sudo apt install seclists



else
    echo "SecLists is installed. You can now run main.py"
fi





