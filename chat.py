#!/usr/bin/env python3
"""
API Shop Demo — Basic Chat Completion

Usage:
  1. Set your API key:  export APISHOP_KEY="sk-..."
  2. Run:               python chat.py
"""

import os
import requests

API_KEY = os.getenv("APISHOP_KEY", "sk-your-key-here")
API_URL = "https://pricepulseapi.site/v1/chat/completions"


def chat(prompt: str, model: str = "deepseek-v4-flash") -> str:
    """Send a chat completion request and return the response text."""
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


def main():
    # --- Example prompts ---
    prompts = [
        "Explain Python decorators in one sentence.",
        "Write a haiku about coding at midnight.",
        "List 3 productivity tips for developers.",
    ]

    model = "deepseek-v4-flash"

    print(f"🤖 API Shop Demo — model: {model}")
    print(f"🔑 Key: {API_KEY[:10]}...{'*' * max(0, len(API_KEY) - 14)}")
    print("=" * 60)

    for i, prompt in enumerate(prompts, 1):
        print(f"\n📝 Prompt {i}: {prompt}")
        try:
            result = chat(prompt, model=model)
            print(f"💬 Response: {result}")
        except Exception as e:
            print(f"❌ Error: {e}")

    print("\n" + "=" * 60)
    print("✨ Get your API key: https://shop.pricepulseapi.site")
    print("🧑‍💻 Freelancer: https://www.freelancer.com/get/rocks081?f=give")


if __name__ == "__main__":
    main()
