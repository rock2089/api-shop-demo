"""
API Shop - Multi-Model Comparison
Compare responses from different models with one API key
"""
from openai import OpenAI

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://pricepulseapi.site/v1"

models = {
    "deepseek-chat": "DeepSeek Chat (Fast, General)",
    "deepseek-reasoner": "DeepSeek Reasoner (Deep thinking)",
    "moonshot-v1-8k": "Kimi 8K (Chinese optimized)"
}

prompt = "Compare Python and Go for backend development. Be concise."

for model_id, model_name in models.items():
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    print(f"\n{'='*60}")
    print(f"{model_name}")
    print(f"{'='*60}")
    response = client.chat.completions.create(model=model_id, messages=[{"role": "user", "content": prompt}], max_tokens=200)
    print(response.choices[0].message.content)
    print(f"Tokens: {response.usage.total_tokens}")
