"""
API Shop - Basic Chat Example
Uses the OpenAI SDK for easy integration
"""
from openai import OpenAI

# Replace with your API Shop key from https://shop.pricepulseapi.site
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://pricepulseapi.site/v1"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful Python expert."},
        {"role": "user", "content": "Explain decorators in Python with a simple example."}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
print(f"\n--- Used {response.usage.total_tokens} tokens ---")
