#!/bin/bash

# Prompt for the OpenAI API key
read -p "Enter your OpenAI API key: " OPENAI_KEY
export OPENAI_API_KEY=$OPENAI_KEY

# Get the last command executed
LAST_COMMAND=$(history | tail -n 1 | sed 's/^[ \t]*//;s/[ \t]*$//;s/^[0-9]*\s*//')

# Execute the last command, capturing both output and errors
COMMAND_OUTPUT=$(eval "$LAST_COMMAND" 2>&1)

# Display the output
echo "$COMMAND_OUTPUT"

# Call the troubleshooter python script and pass the output
echo $(python3 chatgpt_troubleshooter.py "$COMMAND_OUTPUT")

