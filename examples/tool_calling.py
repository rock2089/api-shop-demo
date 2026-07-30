#!/usr/bin/env python3
"""
API Shop Demo — Tool Calling (Function Calling)

Demonstrates how API Shop models support tool/function calling,
enabling AI agents that can execute code, search the web, and more.

Usage:
  1. pip install openai
  2. export APISHOP_KEY="sk-..."
  3. python tool_calling.py
"""

import os
import json
from openai import OpenAI

API_KEY = os.getenv("APISHOP_KEY", "***")
BASE_URL = "https://pricepulseapi.site/v1"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


# --- Define tools the AI can call ---

def calculate(expression: str) -> str:
    """Evaluate a mathematical expression safely."""
    try:
        allowed = set("0123456789+-*/().%^ ")
        if not all(c in allowed for c in expression):
            return "Error: only basic math allowed"
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def get_weather(city: str) -> str:
    """Mock weather lookup (replace with real API)."""
    weather_db = {
        "beijing": "☀️ Sunny, 32°C",
        "london": "🌧️ Rainy, 15°C",
        "tokyo": "⛅ Partly cloudy, 28°C",
        "new york": "🌤️ Clear, 25°C",
        "singapore": "🌦️ Showers, 30°C",
    }
    return weather_db.get(city.lower(), f"No data for {city}")


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a mathematical expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Math expression to evaluate"}
                },
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"}
                },
                "required": ["city"],
            },
        },
    },
]

AVAILABLE_FUNCTIONS = {
    "calculate": calculate,
    "get_weather": get_weather,
}


def run_agent(user_query: str, model: str = "deepseek-v4-pro") -> str:
    """Run an AI agent that can call tools to answer queries."""
    messages = [{"role": "user", "content": user_query}]

    print(f"👤 User: {user_query}")

    for turn in range(5):  # Max 5 tool calls
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )

        msg = response.choices[0].message

        # If the model wants to call a tool
        if msg.tool_calls:
            for tool_call in msg.tool_calls:
                func_name = tool_call.function.name
                func_args = json.loads(tool_call.function.arguments)

                print(f"🔧 Calling: {func_name}({json.dumps(func_args)})")

                result = AVAILABLE_FUNCTIONS[func_name](**func_args)
                print(f"   Result: {result}")

                messages.append(msg)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                })
        else:
            # Final answer
            print(f"🤖 AI: {msg.content}")
            return msg.content

    return "Max tool calls reached"


def main():
    print("🤖 API Shop — Tool Calling Demo")
    print("=" * 60)

    # Example 1: Math + weather
    queries = [
        "What's the weather in Tokyo? Also calculate 156 * 34 + 1000.",
        "Compare the weather in London and Singapore — where would you rather be?",
    ]

    for q in queries:
        print()
        run_agent(q)
        print("-" * 40)

    print("\n" + "=" * 60)
    print("✨ Build AI agents with tool calling — only $2 to start!")
    print("🔗 https://shop.pricepulseapi.site")
    print("🧑‍💻 Hire me: https://www.freelancer.com/get/rocks081?f=give")


if __name__ == "__main__":
    main()
