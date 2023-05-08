import os
import sys
import openai
import json

openai.api_key = os.environ["OPENAI_API_KEY"]

# Function to classify the keywords using ChatGPT API
def get_chatgpt_response(prompt):
    default_messages = [
    {"role": "system", "content": "You are a helpful, pattern-following assistant that translates corporate jargon into plain English."},
    {"role": "system", "name":"example_user", "content": "New synergies will help drive top-line growth."},
    {"role": "system", "name": "example_assistant", "content": "Things working well together will increase revenue."},
    {"role": "system", "name":"example_user", "content": "Let's circle back when we have more bandwidth to touch base on opportunities for increased leverage."},
    {"role": "system", "name": "example_assistant", "content": "Let's talk later when we're less busy about how to do better."},
    {"role": "user", "content": f"help me troubleshoot the last error. be detailed and extensive. suggest next command that can be entered:  \"{prompt}\""},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=default_messages,
        max_tokens=1024*3,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message.content

def main():
    # Read the history from the .commands_history file
    with open(os.path.expanduser("~/.commands_history"), "r") as f:
        lines = f.read(512)

        # Get the response from the model
        response = get_chatgpt_response(lines)
        print(response)

if __name__ == "__main__":
    main()
