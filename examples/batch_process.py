#!/usr/bin/env python3
"""
API Shop Demo — Batch Processing for Freelancers

Process multiple prompts efficiently — perfect for:
- Translating multiple documents
- Summarizing articles in bulk
- Generating product descriptions
- Data cleaning & transformation

Usage:
  1. export APISHOP_KEY="sk-..."
  2. python batch_process.py
"""

import os
import time
import concurrent.futures
import requests

API_KEY = os.getenv("APISHOP_KEY", "***")
API_URL = "https://pricepulseapi.site/v1/chat/completions"


def single_chat(prompt: str, model: str = "deepseek-v4-flash") -> str:
    """Send one chat request and return the response."""
    resp = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def batch_process(tasks: list[dict], workers: int = 5) -> list[dict]:
    """
    Process multiple prompts in parallel with a thread pool.

    Args:
        tasks: List of {"id": str, "prompt": str, "model": str}
        workers: Number of concurrent threads

    Returns:
        List of {"id": str, "prompt": str, "response": str, "model": str, "time": float}
    """
    results = []

    def worker(task):
        start = time.time()
        try:
            response = single_chat(task["prompt"], task.get("model", "deepseek-v4-flash"))
            elapsed = time.time() - start
            return {**task, "response": response, "time": round(elapsed, 2), "status": "ok"}
        except Exception as e:
            elapsed = time.time() - start
            return {**task, "response": str(e), "time": round(elapsed, 2), "status": "error"}

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(worker, task) for task in tasks]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    # Sort by original order (by id)
    results.sort(key=lambda r: int(r["id"]) if r["id"].isdigit() else r["id"])
    return results


def main():
    import json

    # Example: translate 8 phrases to different languages
    tasks = [
        {"id": "1", "prompt": "Translate to French: 'Good morning, how are you?'", "model": "deepseek-v4-flash"},
        {"id": "2", "prompt": "Translate to Spanish: 'The weather is beautiful today.'", "model": "deepseek-v4-flash"},
        {"id": "3", "prompt": "Translate to German: 'I would like a coffee please.'", "model": "deepseek-v4-flash"},
        {"id": "4", "prompt": "Translate to Japanese: 'Where is the train station?'", "model": "deepseek-v4-flash"},
        {"id": "5", "prompt": "Generate 3 product taglines for a smart water bottle.", "model": "deepseek-v4-flash"},
        {"id": "6", "prompt": "Summarize in one sentence: Python is great for automation.", "model": "deepseek-v4-flash"},
        {"id": "7", "prompt": "Write a short cold email to pitch API services.", "model": "deepseek-v4-pro"},
        {"id": "8", "prompt": "List 5 Python libraries every freelancer should know.", "model": "deepseek-v4-flash"},
    ]

    print("🚀 API Shop — Batch Processing Demo for Freelancers")
    print(f"📦 Processing {len(tasks)} tasks with 5 workers...")
    print("=" * 60)

    start_time = time.time()
    results = batch_process(tasks, workers=5)
    total_time = time.time() - start_time

    for r in results:
        emoji = "✅" if r["status"] == "ok" else "❌"
        print(f"\n{emoji} Task {r['id']} [{r['time']}s] | {r.get('model', 'deepseek-v4-flash')}")
        print(f"   Prompt: {r['prompt'][:80]}...")
        response_preview = r["response"][:200].replace("\n", " ")
        print(f"   Result: {response_preview}")

    print("\n" + "=" * 60)
    print(f"⏱️  Total time: {total_time:.1f}s | Parallel speedup: ~{len(tasks)}x vs sequential")
    print(f"💰 Perfect for freelancers who process bulk data with AI.")
    print(f"🔗 Get your API key: https://shop.pricepulseapi.site")
    print(f"🧑‍💻 Hire me: https://www.freelancer.com/get/rocks081?f=give")


if __name__ == "__main__":
    main()
