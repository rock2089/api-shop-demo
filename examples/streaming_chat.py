"""
API Shop - Streaming Chat Example
Shows real-time token-by-token output
"""
import requests, json

API_KEY = "YOUR_API_KEY"
API_URL = "https://pricepulseapi.site/v1/chat/completions"

payload = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Write a creative short story about a robot learning to paint."}],
    "stream": True,
    "temperature": 0.9,
    "max_tokens": 1000
}

response = requests.post(API_URL, headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}, json=payload, stream=True)

print("Robot Artist Story:\n")
for line in response.iter_lines():
    if line:
        line = line.decode("utf-8")
        if line.startswith("data: ") and line[6:] != "[DONE]":
            delta = json.loads(line[6:])["choices"][0]["delta"]
            content = delta.get("content", "")
            if content:
                print(content, end="", flush=True)
print("\n")
