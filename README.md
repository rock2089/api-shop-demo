# API Shop Demo 🚀

> **Affordable AI API Access — DeepSeek V4, Kimi K2, and more. Pay once, use any model.**

[![API Shop](https://img.shields.io/badge/API%20Shop-Live-brightgreen)](https://shop.pricepulseapi.site)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Models](https://img.shields.io/badge/models-DeepSeek%20%7C%20Kimi-purple)]()

---

## What is API Shop?

API Shop provides **cheap, reliable AI API access** with OpenAI-compatible endpoints. Unlike other providers, we offer a **pay-once, top-up-when-needed** model — no monthly subscriptions, no recurring fees.

### Available Models

| Model | Context | Use Case |
|-------|---------|----------|
| **DeepSeek V4 Flash** | 128K | Fast, affordable general-purpose chat |
| **DeepSeek V4 Pro** | 128K | Advanced reasoning & coding |
| **Kimi K2 (Moonshot)** | 128K | Long-context understanding |
| **DeepSeek R1-0528** | 128K | Chain-of-thought reasoning |

## Quick Start

```bash
# 1. Get your API key from https://shop.pricepulseapi.site
# 2. Send a request

curl -X POST https://pricepulseapi.site/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Write a Python function to sort a list"}]
  }'
```

## Python Example

```python
import requests

API_KEY = "your-api-key-here"
API_URL = "https://pricepulseapi.site/v1/chat/completions"

def chat(prompt, model="deepseek-v4-flash"):
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

# Example usage
print(chat("Explain quantum computing in simple terms"))
```

## OpenAI SDK Compatibility

API Shop is fully compatible with the OpenAI Python SDK:

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://pricepulseapi.site/v1"
)

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## Node.js Example

```javascript
const API_KEY = "your-api-key-here";
const API_URL = "https://pricepulseapi.site/v1/chat/completions";

async function chat(prompt, model = "deepseek-v4-flash") {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model,
      messages: [{ role: "user", content: prompt }]
    })
  });
  const data = await response.json();
  return data.choices[0].message.content;
}

// Usage
chat("Write a haiku about programming").then(console.log);
```

## Demo Scripts

This repo includes working demo scripts in this directory and the [`/examples`](./examples) folder:

| File | Description |
|------|-------------|
| `chat.py` | Basic chat completion in Python |
| `openai_sdk.py` | Using the official OpenAI SDK |
| `stream.py` | Streaming responses |
| `chat.sh` | Bash/curl one-liner |
| `examples/batch_process.py` | **NEW** — Parallel batch processing for freelancers |
| `examples/tool_calling.py` | **NEW** — AI agent with function calling |

## For Freelancers 🧑‍💻

API Shop is built by a freelancer, for freelancers. The batch processing demo (`examples/batch_process.py`) shows how to process dozens of AI tasks in parallel — perfect for:

- 📝 Translating documents in bulk
- 📊 Summarizing articles and reports
- 🏷️ Generating product descriptions
- 🤖 Building AI-powered automation tools for clients

```bash
# Process 8 tasks in parallel with just a few lines:
python examples/batch_process.py
```

👉 **Need custom automation? Hire me:** [freelancer.com/get/rocks081](https://www.freelancer.com/get/rocks081?f=give)

## Pricing

💰 **Pay-as-you-go** — Top up any amount, use any model.

| Plan | Price | What You Get |
|------|-------|--------------|
| **Starter** | $2 | 2M tokens — try all models |
| **Standard** | $5 | 6M tokens — best value |
| **Pro** | $10 | 15M tokens — heavy usage |

👉 **Visit [shop.pricepulseapi.site](https://shop.pricepulseapi.site) to get started.**

---

## Why API Shop?

- 🔌 **OpenAI-compatible** — Drop-in replacement for any OpenAI SDK project
- 💸 **No monthly fees** — Pay once, use until your balance runs out
- 🧠 **Multiple models** — DeepSeek, Kimi K2 in one account
- 🆓 **Free trial** — Test before you buy
- ⚡ **Fast inference** — Optimized infrastructure

---

## About the Author

Built by a freelance developer who automates everything with Python. If you need custom automation, web scraping, or AI integration work:

- 🧑‍💻 **Hire me on Freelancer:** [freelancer.com/get/rocks081](https://www.freelancer.com/get/rocks081?f=give)
- 🐙 **GitHub:** [@rock2089](https://github.com/rock2089)

---

## License

MIT — use freely, attribution appreciated.
