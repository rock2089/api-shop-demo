#!/usr/bin/env python3
"""
Content Repurposer — AI-powered content transformation for freelancers.
Turn one piece of content into tweet threads, LinkedIn posts, newsletters,
blog summaries, and SEO descriptions — all via API Shop.

Usage:
    python content_repurposer.py

API Shop: https://shop.pricepulseapi.site
Freelancer: https://freelancer.com/get/rocks081?f=give
"""

import requests
import json
import os
from typing import Optional

API_KEY = os.environ.get("API_SHOP_KEY", "your-api-key")
API_URL = "https://pricepulseapi.site/v1/chat/completions"
MODEL = "deepseek-v4-flash"

# ── Core AI call ──────────────────────────────────────────────

def ask_ai(prompt: str, model: str = MODEL, temperature: float = 0.7) -> str:
    """Send a prompt to API Shop and return the response."""
    resp = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
        },
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


# ── Repurpose formats ─────────────────────────────────────────

FORMATS = {
    "twitter_thread": {
        "name": "Twitter/X Thread 🧵",
        "prompt": """Rewrite the following content as a Twitter/X thread (6-10 tweets).
Each tweet should be numbered (1/8, 2/8...) and end with an engaging hook.
Include 2-3 relevant hashtags at the end. Make it punchy and scroll-stopping.

Content:
{content}""",
    },
    "linkedin_post": {
        "name": "LinkedIn Post 💼",
        "prompt": """Rewrite the following content as a professional LinkedIn post.
Use line breaks for readability. Include a strong opener, key takeaways as bullet points,
and a CTA at the end. Add 3-5 relevant hashtags. Keep it authentic — no corporate jargon.

Content:
{content}""",
    },
    "newsletter": {
        "name": "Email Newsletter 📧",
        "prompt": """Transform the following content into an email newsletter.
Include: a catchy subject line, greeting, main body (2-3 paragraphs),
"Key Takeaways" section with bullet points, and a friendly sign-off.

Content:
{content}""",
    },
    "blog_summary": {
        "name": "TL;DR Summary 📝",
        "prompt": """Create a concise TL;DR summary of the following content in 3-4 sentences.
Include: the main point, why it matters, and one actionable insight.

Content:
{content}""",
    },
    "seo_description": {
        "name": "SEO Meta Description 🔍",
        "prompt": """Write a compelling SEO meta description (150-160 characters) for the following content.
Include the primary keyword naturally and a call-to-action.

Content:
{content}""",
    },
    "youtube_script": {
        "name": "YouTube Short Script 🎬",
        "prompt": """Convert the following content into a 60-second YouTube Short / TikTok script.
Format as: [HOOK - first 3 seconds], [BODY - 45 seconds], [CTA - last 12 seconds].
Include visual cues like [B-ROLL: ...] or [TEXT OVERLAY: ...].

Content:
{content}""",
    },
}


# ── Main ───────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  📣 Content Repurposer — powered by API Shop")
    print("=" * 60)
    print()

    # Get input content
    print("Paste your content below (type END on a new line when done):")
    print("-" * 40)
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        except (EOFError, KeyboardInterrupt):
            break
    content = "\n".join(lines)

    if not content.strip():
        print("\n⚠️  No content provided. Using a sample for demo...\n")
        content = (
            "API Shop (shop.pricepulseapi.site) is a pay-as-you-go AI API platform "
            "offering DeepSeek V4, Kimi K2, and more at affordable prices. "
            "No monthly subscriptions — just top up and use any model. "
            "Built by a freelancer who uses these APIs daily for automation, "
            "web scraping, content generation, and client projects. "
            "The platform is OpenAI-compatible, so you can drop it into any existing project."
        )

    print(f"\n📄 Source content ({len(content)} chars)\n")

    # Choose format
    print("Choose output format:")
    for key, fmt in FORMATS.items():
        print(f"  [{key[:3]:>3}] {fmt[name]}")
    print(f"  [all] All formats")
    print()

    try:
        choice = input("Format choice (default: all): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        choice = ""

    if not choice:
        choice = "all"

    # Process
    selected = (
        {k: v for k, v in FORMATS.items()}
        if choice == "all"
        else {choice: FORMATS[choice]}
        if choice in FORMATS
        else {}
    )

    if not selected:
        print(f"❌ Unknown format: {choice}")
        return

    for key, fmt in selected.items():
        print(f"\n{─ * 60}")
        print(f"  {fmt[name]}")
        print(f"{─ * 60}\n")

        try:
            prompt = fmt["prompt"].format(content=content[:3000])
            result = ask_ai(prompt, temperature=0.8)
            print(result)
        except Exception as e:
            print(f"  ❌ Error: {e}")

    print(f"\n{= * 60}")
    print("  ✅ Done! Repurpose your content at scale with API Shop")
    print(f"  🔗 https://shop.pricepulseapi.site")
    print(f"  🧑‍💻 Need custom automation? freelancer.com/get/rocks081?f=give")
    print(f"{= * 60}")


if __name__ == "__main__":
    main()
