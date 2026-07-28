# 🏪 API Shop Demo — Affordable AI API Access

> **Pay once, use any model.** No subscription. Free trial. OpenAI-compatible.

[![API Shop](https://img.shields.io/badge/API%20Shop-shop.pricepulseapi.site-blue)](https://shop.pricepulseapi.site)
[![Live Demo](https://img.shields.io/badge/Live-Demo-green)](https://shop.pricepulseapi.site/demo)
[![Models](https://img.shields.io/badge/Models-DeepSeek%20%7C%20Kimi-orange)](https://shop.pricepulseapi.site)

---

## 🚀 Why API Shop?

| Problem | Solution |
|---------|----------|
| ❌ Monthly subscriptions | ✅ Pay once, use anytime |
| ❌ Multiple accounts for different models | ✅ One key for all models |
| ❌ Complex per-token billing | ✅ Simple credit packs |
| ❌ No way to try before buying | ✅ 10K free trial tokens |

---

## ⚡ Quick Start (30 seconds)

```bash
curl -X POST https://pricepulseapi.site/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer *** \
  -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"Explain quantum computing in one sentence."}]}'
```

---

## 📦 Available Models

| Model | Best For | Context Window |
|-------|----------|---------------|
| `deepseek-chat` | General chat, reasoning, coding | 64K |
| `deepseek-reasoner` | Complex reasoning, math, logic | 64K |
| `moonshot-v1-8k` | Chinese content, long-form | 8K |
| `moonshot-v1-32k` | Long context, research | 32K |
| `moonshot-v1-128k` | Ultra-long context | 128K |

---

## 💻 Code Examples

### Python (OpenAI SDK — drop-in replacement)

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://pricepulseapi.site/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Write a Python function to reverse a linked list."}]
)

print(response.choices[0].message.content)
```

### Python (requests)

```python
import requests

response = requests.post(
    "https://pricepulseapi.site/v1/chat/completions",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json={
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": "Hello!"}],
        "temperature": 0.7,
        "max_tokens": 500
    }
)
print(response.json()["choices"][0]["message"]["content"])
```

### Node.js

```javascript
const response = await fetch("https://pricepulseapi.site/v1/chat/completions", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
  },
  body: JSON.stringify({
    model: "deepseek-chat",
    messages: [{ role: "user", content: "Hello!" }]
  })
});
const data = await response.json();
console.log(data.choices[0].message.content);
```

### Python Streaming

```python
import requests, json

response = requests.post(
    "https://pricepulseapi.site/v1/chat/completions",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json={
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": "Write a short story."}],
        "stream": True
    },
    stream=True
)

for line in response.iter_lines():
    if line:
        line = line.decode("utf-8")
        if line.startswith("data: ") and line[6:] != "[DONE]":
            delta = json.loads(line[6:])["choices"][0]["delta"]
            print(delta.get("content", ""), end="", flush=True)
```

---

## 💰 Pricing

| Plan | Tokens | Price | Best For |
|------|--------|-------|----------|
| 🎁 **Free Trial** | 10K | **$0** | Testing |
| 🥉 Starter | 2M | $5 | Hobby projects |
| 🥈 Pro | 10M | $20 | Side projects |
| 🥇 Enterprise | 100M | $100 | Production |

> 💡 Credits never expire. Top up anytime via WeChat Pay or PayPal.

---

## 🔧 Integration Guide

API Shop uses the standard OpenAI chat completions format. If your app already uses the OpenAI SDK, just change `base_url`:

```python
# Before (OpenAI)
client = OpenAI(api_key="sk-...")

# After (API Shop)
client = OpenAI(
    api_key="YOUR_API_SHOP_KEY",
    base_url="https://pricepulseapi.site/v1"
)
# Everything else stays the same!
```

---

## 🔗 Links

- 🏪 **API Shop**: [shop.pricepulseapi.site](https://shop.pricepulseapi.site)
- 📝 **Live Demo**: [shop.pricepulseapi.site/demo](https://shop.pricepulseapi.site/demo)
- 👨‍💻 **Freelancer**: [freelancer.com/get/rocks081](https://www.freelancer.com/get/rocks081?f=give)

---

## 📄 License

MIT — use it however you want.

---

Built with ❤️ by [@rock2089](https://github.com/rock2089)