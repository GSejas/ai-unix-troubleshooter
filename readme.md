ChatGPT Troubleshooter CLI

This repository contains code for a ChatGPT Troubleshooter CLI, which is a command-line interface that allows users to troubleshoot errors using OpenAI's ChatGPT API. The CLI is designed to read and analyze the command history file ".commands_history" and provide users with a response from the ChatGPT model.

## Installation

To use the ChatGPT Troubleshooter, follow these steps:

1. Clone the repository onto your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set the OpenAI API key in the environment variable `OPENAI_API_KEY`.
4. Add the following line to your `.bashrc` file: `python3 /path/to/chatgpt_troubleshooter.py`.
5. Save the changes to `.bashrc` and exit.

## Usage

To use the ChatGPT Troubleshooter, simply open a new terminal window and enter a command. The CLI will automatically read and analyze the command history file `.commands_history`, and provide a response from the ChatGPT model. 

## Files

- `.bashrc.replace`: A file containing commands to be added to the `.bashrc` file.
- `.gitignore`: A file that specifies which files and directories should be ignored by Git when committing changes.
- `chatgpt_troubleshooter.py`: The main Python script for the ChatGPT Troubleshooter CLI.
- `requirements.txt`: A file listing the required Python dependencies for the project.
- `run_troubleshoot.sh`: A shell script that runs the ChatGPT Troubleshooter.

## Notes

The ChatGPT Troubleshooter CLI is a work in progress and may not work for all users. If you encounter any issues, please feel free to submit an issue or pull request.