
# Tests that the function returns a non-empty string when given a non-empty prompt. 
from chatgpt_troubleshooter import get_chatgpt_response
from unittest.mock import patch

def test_get_chatgpt_response_happy_path():
    prompt = "How can I improve my productivity?"
    response = get_chatgpt_response(prompt)
    assert response != ""

# Tests that the function uses the openai.ChatCompletion.create method to generate a response. 
def test_get_chatgpt_response_api_call( mocker):
    prompt = "How can I improve my productivity?"
    mock_create = mocker.patch("openai.ChatCompletion.create")
    get_chatgpt_response(prompt)
    mock_create.assert_called_once()

# Tests that the function returns an empty string when given an empty prompt. 
def test_get_chatgpt_response_empty_string():
    prompt = ""
    response = get_chatgpt_response(prompt)
    assert response == ""

# Tests that the function returns an empty string when given a None prompt. 
def test_get_chatgpt_response_none():
    prompt = None
    response = get_chatgpt_response(prompt)
    assert response == ""

# Tests that the function returns an empty string when the response.choices[0].message.content is None. 
def test_get_chatgpt_response_none_content( mocker):
    prompt = "How can I improve my productivity?"
    mock_choice = mocker.Mock()
    mock_choice.message.content = None
    mock_response = mocker.Mock()
    mock_response.choices = [mock_choice]
    mocker.patch("openai.ChatCompletion.create", return_value=mock_response)
    response = get_chatgpt_response(prompt)
    assert response == ""

# Tests that the function returns an empty string when the response.choices[0].message.content is an empty string. 
def test_get_chatgpt_response_empty_content( mocker):
    prompt = "How can I improve my productivity?"
    mock_choice = mocker.Mock()
    mock_choice.message.content = ""
    mock_response = mocker.Mock()
    mock_response.choices = [mock_choice]
    mocker.patch("openai.ChatCompletion.create", return_value=mock_response)
    response = get_chatgpt_response(prompt)
    assert response == ""