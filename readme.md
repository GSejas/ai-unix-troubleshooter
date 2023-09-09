ChatGPT Troubleshooter CLI

This repository contains code for a ChatGPT Troubleshooter CLI, which is a command-line interface that allows users to troubleshoot errors using OpenAI's ChatGPT API. The CLI is designed to read and analyze the command history file ".commands_history" and provide users with a response from the ChatGPT model.

## Installation

Clone the repository onto your local machine.
```bash
git clone git@github.com:GSejas/ai-unix-troubleshooter.git
```
Navigate to the cloned directory.
```bash
cd ai-unix-troubleshooter
```
Run the installation script:
```bash
bash install_troubleshooter.sh
```
This script will prompt you for your OpenAI API key.

With this setup, the user experience is enhanced since they won't have to provide the path to the ChatGPT Troubleshooter directory explicitly.

## Usage

To use the ChatGPT Troubleshooter, simply open a new terminal window and enter a command. The CLI will automatically read and analyze the command history file `.commands_history`, and provide a response from the ChatGPT model. 

## Files

- `.bashrc.replace`: A file containing commands to be added to the `.bashrc` file.
- `.gitignore`: A file that specifies which files and directories should be ignored by Git when committing changes.
- `chatgpt_troubleshooter.py`: The main Python script for the ChatGPT Troubleshooter CLI.
- `run_troubleshoot.sh`: A shell script that runs the ChatGPT Troubleshooter.

## Notes

The ChatGPT Troubleshooter CLI is a work in progress and may not work for all users. If you encounter any issues, please feel free to submit an issue or pull request.
