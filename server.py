from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.route("/ai", methods=["POST"])
def ai():
    data = request.get_json()
    prompt = data.get("prompt", "")

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "google/gemini-3-flash-preview",
        "messages": [
            {"role": "system", "content": "Răspunde ca un player Roblox român, natural, cu emoji."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    data_ai = response.json()

    try:
        ai_text = data_ai["choices"][0]["message"]["content"]
    except:
        ai_text = "Eroare la AI."

    return jsonify({"text": ai_text})

@app.route("/")
def home():
    return "AI Zentrix server is running with Gemini 3 Flash Preview via OpenRouter."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
