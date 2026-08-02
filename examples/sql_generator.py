#!/usr/bin/env python3
"""
AI SQL Query Generator — Convert natural language to SQL using API Shop.

Usage:
    python sql_generator.py "find all users who registered in the last 7 days"
    python sql_generator.py "top 10 products by sales amount, with categories"

Requirements: pip install requests
"""

import requests
import sys
import os

API_KEY = os.getenv("API_SHOP_KEY", "your-api-key-here")
API_URL = "https://pricepulseapi.site/v1/chat/completions"

SYSTEM_PROMPT = """You are a SQL expert. Convert the user's natural language request into a clean, 
well-formatted SQL query. Follow these rules:

1. Use standard SQL syntax (PostgreSQL-compatible)
2. Include brief comments explaining each major clause
3. Use snake_case for table/column names
4. Add a short explanation of what the query does
5. If the user doesn't specify table names, use reasonable placeholder names
   (e.g., users, orders, products)
6. Include proper indexing hints as comments where relevant

Output format:
```sql
-- Explanation: <one-line description>
<the query>
```"""


def generate_sql(prompt: str, model: str = "deepseek-v4-flash") -> str:
    """Generate SQL from a natural language description."""
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.3,
            "max_tokens": 1000,
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def main():
    if len(sys.argv) < 2:
        print("Usage: python sql_generator.py \"your natural language query\"")
        print()
        print("Examples:")
        print('  python sql_generator.py "find all users who signed up this month"')
        print('  python sql_generator.py "total revenue by product category last quarter"')
        print('  python sql_generator.py "users who placed orders but never paid"')
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    print(f"Generating SQL for: {prompt}\n")
    print("=" * 60)

    try:
        sql = generate_sql(prompt)
        print(sql)
        print("=" * 60)
        print("\nPowered by API Shop — https://shop.pricepulseapi.site")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("Invalid API key. Set API_SHOP_KEY environment variable.")
            print("   Get a key at https://shop.pricepulseapi.site")
        else:
            print(f"API error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
