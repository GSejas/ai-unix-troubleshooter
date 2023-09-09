#!/bin/bash

# Get the current directory where the script is being executed
TROUBLESHOOTER_DIR=$PWD

# Prompt for the OpenAI API key
read -p "Enter your OpenAI API key: " OPENAI_KEY

# Append bashrc.replace content to .bashrc
cat "$TROUBLESHOOTER_DIR/.bashrc.replace" >> ~/.bashrc

# Replace placeholders with actual values in .bashrc
sed -i "s|your-openai-api-key-here|$OPENAI_KEY|g" ~/.bashrc

# Add the contents of .bashrc.replace to .bashrc, replacing placeholder with actual path
cat .bashrc.replace | sed "s|PLACEHOLDER_PATH|$PWD|" >> ~/.bashrc


echo "Installation complete. Please restart your terminal or run 'source ~/.bashrc' to apply changes."
