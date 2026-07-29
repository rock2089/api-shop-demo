#!/usr/bin/env python3
"""
API Shop Demo — OpenAI SDK Compatibility

Shows that API Shop is a drop-in replacement for OpenAI SDK projects.
Just change base_url and api_key.

Usage:
  1. pip install openai
  2. export APISHOP_KEY="sk-..."
  3. python openai_sdk.py
"""

import os
from openai import OpenAI

API_KEY = os.getenv("APISHOP_KEY", "sk-your-key-here")
BASE_URL = "https://pricepulseapi.site/v1"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def chat(prompt: str, model: str = "deepseek-v4-flash") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def stream_chat(prompt: str, model: str = "deepseek-v4-flash"):
    """Stream tokens as they arrive."""
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()


def main():
    print("🤖 API Shop with OpenAI SDK")
    print("=" * 60)

    # Standard chat
    print("\n📝 Standard chat:")
    result = chat("What is the capital of France? Answer in one word.")
    print(f"   {result}")

    # Streaming
    print("\n📝 Streaming response:")
    stream_chat("Count from 1 to 5 with an emoji for each number.")

    print("\n" + "=" * 60)
    print("✨ Drop-in replacement — just change base_url and api_key!")
    print("🔗 https://shop.pricepulseapi.site")


if __name__ == "__main__":
    main()
