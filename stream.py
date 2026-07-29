#!/usr/bin/env python3
"""
API Shop Demo — Streaming Chat with Multiple Models

Usage:
  1. export APISHOP_KEY="sk-..."
  2. python stream.py
"""

import os
import requests
import json

API_KEY = os.getenv("APISHOP_KEY", "sk-your-key-here")
API_URL = "https://pricepulseapi.site/v1/chat/completions"


def stream_chat(prompt: str, model: str = "deepseek-v4-flash"):
    """Stream a chat completion and print tokens as they arrive."""
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": True,
        },
        stream=True,
        timeout=120,
    )
    response.raise_for_status()

    for line in response.iter_lines():
        if line:
            line = line.decode("utf-8")
            if line.startswith("data: ") and line != "data: [DONE]":
                chunk = json.loads(line[6:])
                if chunk["choices"][0]["delta"].get("content"):
                    print(chunk["choices"][0]["delta"]["content"], end="", flush=True)
    print()


def main():
    models = ["deepseek-v4-flash", "deepseek-v4-pro", "kimi-k2"]
    prompt = "Write a one-line poem about the ocean."

    print("🌊 API Shop — Multi-Model Streaming Demo")
    print("=" * 60)

    for model in models:
        print(f"\n🔹 {model}:")
        try:
            stream_chat(prompt, model=model)
        except Exception as e:
            print(f"   ❌ Error: {e}")

    print("\n" + "=" * 60)
    print("🚀 Try all models with one API key: https://shop.pricepulseapi.site")


if __name__ == "__main__":
    main()
