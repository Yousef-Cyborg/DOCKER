# api_service/app.py
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Predefined responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Greetings! How can I assist you today?"],
    "how are you": ["I'm doing well, thank you!", "I'm great, how about you?", "I'm just a chatbot, but I'm doing fine!"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
}

def get_bot_response(user_input):
    user_input = user_input.lower()
    return random.choice(responses.get(user_input, ["Sorry, I didn't understand that. Can you rephrase?"]))

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        bot_response = get_bot_response(user_message)
        return jsonify({'response': bot_response})
    else:
        return jsonify({'response': "Please send a message!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
