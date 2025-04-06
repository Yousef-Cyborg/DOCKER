import requests

API_URL = "http://localhost:5001/chat"

def test_bot_response():
    response = requests.post(API_URL, json={"message": "Hi"})
    data = response.json()
    assert response.status_code == 200
    assert "response" in data
    assert data["response"] in ["Hello!", "Hi there!", "Greetings! How can I assist you today?"]

def test_bot_unknown_message():
    response = requests.post(API_URL, json={"message": "unknown"})
    data = response.json()
    assert response.status_code == 200
    assert "response" in data
    assert data["response"] == "Sorry, I didn't understand that. Can you rephrase?"
