#!/bin/bash

# Get the directory where the script resides
TROUBLESHOOTER_DIR=$(dirname "$0")

# Prompt for the OpenAI API key
read -p "Enter your OpenAI API key: " OPENAI_KEY

# Check if content already exists, if not append
if ! grep -q "your-openai-api-key-here" ~/.bashrc; then
    cat "$TROUBLESHOOTER_DIR/.bashrc.replace" | \
    sed "s|your-openai-api-key-here|$OPENAI_KEY|g" | \
    sed "s|PLACEHOLDER_PATH|$TROUBLESHOOTER_DIR|g" >> ~/.bashrc
fi

echo "Installation complete. Please restart your terminal or run 'source ~/.bashrc' to apply changes."
