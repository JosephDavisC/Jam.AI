from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os
import logging

# Create and configure logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
logging.debug('This is a debug message')

# Specify the path to the .env file
dotenv_path = os.path.join(os.getcwd(), 'secrets', '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route("/", methods=["GET"])  # Updated to add GET method
def index():
    return render_template("index.html")

@app.route("/get_api_data", methods=["POST"])
def get_api_data():
    if not request.json or 'message' not in request.json:
        return jsonify({'error': 'Invalid request'}), 400

    user_text = request.json['message']

    # Construct the request to send to OpenAI API with your tuned model
    request_data = {
        "model": "ft:gpt-3.5-turbo-0125:personal:jam:9IvlOxXp",
        "messages": [{"role": "user", "content": user_text }],
        "max_tokens": 2048,
        "temperature": 0.2
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('API_KEY')}"
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=request_data)

    # Handle potential errors here
    if response.status_code != 200:
        return jsonify({"error": "Error from OpenAI API"}), response.status_code

    return jsonify(response.json())  # Send the response back to JavaScript

if __name__ == "__main__":
    app.run(debug=True)
