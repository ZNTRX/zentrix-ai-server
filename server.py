from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ai", methods=["POST"])
def ai():
    data = request.get_json()
    prompt = data.get("prompt", "")
    return jsonify({"text": f"[AI Zentrix] Am primit: {prompt}"})

@app.route("/")
def home():
    return "AI Zentrix server is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
