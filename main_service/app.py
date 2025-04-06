# main_service/app.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# main_service/app.py
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        response = requests.post('http://api-service:5001/chat', json={'message': user_message})  # Ensure the host is `api-service`
        bot_response = response.json().get('response')
        return jsonify({'response': bot_response})
    else:
        return jsonify({'response': "Please enter a message."})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
