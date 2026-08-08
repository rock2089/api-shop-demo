# API Shop Demo 🚀

> **Affordable AI API Access — DeepSeek V4, Kimi K2, and more. Pay once, use any model.**

[![API Shop](https://img.shields.io/badge/API%20Shop-Live-brightgreen)](https://shop.pricepulseapi.site)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Models](https://img.shields.io/badge/models-DeepSeek%20%7C%20Kimi-purple)]()

---

## 🆕 What's New

**🧪 AI Unit Test Generator** — Drop in any Python source file and get production-ready pytest tests. Detects functions, classes, edge cases, and generates comprehensive test suites. [Try it →](examples/unit_test_generator.py)

```bash
python examples/unit_test_generator.py your_code.py tests/test_your_code.py
```

**🖥️ Web Chat Demo** — A beautiful Streamlit-powered chat UI with streaming, model switching, cost tracking, and chat export. [Try it →](examples/streamlit_chat.py)

```bash
pip install streamlit
streamlit run examples/streamlit_chat.py
```

**AI SQL Generator** — Convert natural language to SQL queries. Type what you want in plain English, get production-ready SQL with comments and indexing hints. [Try it →](examples/sql_generator.py)

**📣 Content Repurposer** — Paste any content and get it transformed into 6 formats: Twitter threads, LinkedIn posts, newsletters, blog summaries, SEO descriptions, and YouTube scripts. [Try it →](examples/content_repurposer.py)

```bash
python examples/content_repurposer.py
```


```bash
python examples/sql_generator.py "top 10 customers by total spend last month"
```

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
  -H "Authorization: Bearer *** \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Write a Python function to sort a list"}]
  }'
```

## Python Example

```python
import requests

API_KEY="***"
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
const API_KEY="***";
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

This repo includes 15 working demo scripts — from basic chat to developer tools and freelancer automation:

| File | Description |
|------|-------------|
| `chat.py` | Basic chat completion in Python |
| `openai_sdk.py` | Using the official OpenAI SDK |
| `stream.py` | Streaming responses |
| `chat.sh` | Bash/curl one-liner |
| **examples/** | |
| `examples/content_repurposer.py` | **NEW** 📣 — Repurpose content into tweets, LinkedIn posts, newsletters, YouTube scripts |
| `examples/batch_process.py` | Parallel batch processing (8 tasks, thread pool) |
| `examples/tool_calling.py` | AI agent with function calling |
| `examples/langchain_demo.py` | LangChain integration (RAG, chains, agents) |
| `examples/scraper_ai_demo.py` | Web scraping + AI analysis combo |
| `examples/freelancer_proposals.py` | AI proposal generator: cover letters, pricing, timelines |
| `examples/unit_test_generator.py` | **NEW** 🧪 — Auto-generate pytest tests from source code |
| `examples/streamlit_chat.py` | **NEW** 🖥️ — Web chat UI with streaming, model switch, cost tracking |
| `examples/sql_generator.py` | Natural language to SQL with comments & index hints |
| `examples/model_comparison.py` | Compare output across models |
| `examples/streaming_chat.py` | Real-time streaming demo |
| `examples/basic_chat.py` | Minimal Python chat example |
| `examples/nodejs_chat.js` | Node.js fetch example |

## Developer Tools 🛠️

Practical AI-powered utilities you can drop into your workflow:

| Tool | What It Does |
|------|-------------|
| `unit_test_generator.py` | **🧪 Test Gen** — Auto-generate pytest tests: edge cases, mocks, fixtures |
| `streamlit_chat.py` | **🖥️ Web Chat** — Full chat UI with streaming, 4 models, cost tracking, chat export |
| `sql_generator.py` | **English → SQL** — Type "users who churned last month" → get a JOIN query with indexes |
| `tool_calling.py` | **AI Agents** — Give your AI access to APIs, databases, and external tools |
| `content_repurposer.py` | **📣 Content Repurpose** — Turn any text into 6 formats: tweets, LinkedIn, newsletter, YouTube script |
| `batch_process.py` | **Parallel Processing** — Run 8+ AI tasks simultaneously via thread pool |

```bash
# Generate unit tests from source code:
python examples/unit_test_generator.py your_module.py

# Generate SQL from plain English:
python examples/sql_generator.py "monthly revenue by region, year-over-year comparison"

# Build an AI agent with tool access:
python examples/tool_calling.py

# Process a batch of tasks in parallel:
python examples/batch_process.py
```

## For Freelancers 🧑‍💻

API Shop is built by a freelancer, for freelancers. Check out these demos designed for real freelancing workflows:

| Demo | Use It For |
|------|------------|
| `freelancer_proposals.py` | **Generate winning proposals** — cover letters, price estimates, timelines, client questions |
| `batch_process.py` | Process dozens of AI tasks in parallel — translations, summaries, product descriptions |
| `scraper_ai_demo.py` | Scrape websites + AI analysis — competitor research, lead generation |
| `tool_calling.py` | Build AI agents that can use tools — automate client workflows |
| `content_repurposer.py` | **Repurpose content for clients** — blogs → social posts, newsletters, video scripts |
| `sql_generator.py` | Write SQL queries from plain English — deliver data work faster |

```bash
# Generate a proposal in seconds:
python examples/freelancer_proposals.py

# Convert requirements to SQL instantly:
python examples/sql_generator.py "find duplicate orders placed within 5 minutes"
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