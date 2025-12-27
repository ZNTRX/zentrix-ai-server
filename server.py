import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "google/gemini-3-flash-preview",
    "messages": [
        {"role": "system", "content": "Vei vorbi ca un player Roblox român."},
        {"role": "user", "content": prompt}
    ]
}

r = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
response_text = r.json()["choices"][0]["message"]["content"]
