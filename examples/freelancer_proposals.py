"""
Freelancer Proposal Generator — AI-Powered Bidding Assistant
==============================================================
Generate winning freelancer proposals in seconds using API Shop.
Covers: cover letters, price estimates, project timelines, and
client-tailored pitches.

API Shop: https://shop.pricepulseapi.site
Hire me: https://freelancer.com/get/rocks081?f=give
Author: @rock2089
"""

import requests
import json
import sys
import os

# ============================================================
# CONFIGURATION
# ============================================================

API_KEY = os.environ.get("API_SHOP_KEY", "your-api-key")
API_URL = "https://pricepulseapi.site/v1/chat/completions"

# Get key at: https://shop.pricepulseapi.site


def call_ai(prompt, model="deepseek-v4-flash", temperature=0.8, max_tokens=1000):
    """Call API Shop with any model."""
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": max_tokens,
        },
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


# ============================================================
# 1. COVER LETTER GENERATOR
# ============================================================
# Paste a project description from Freelancer/Upwork and get
# a tailored cover letter that highlights relevant skills.

def generate_cover_letter(project_description, your_skills, model="deepseek-v4-pro"):
    """Generate a professional freelancer cover letter."""
    prompt = f"""You are an experienced freelancer writing a cover letter for a project.
    
PROJECT DESCRIPTION:
{project_description}

MY SKILLS:
{your_skills}

Write a compelling, professional cover letter (200-300 words) that:
1. Opens with a personalized hook referencing the project
2. Highlights 2-3 specific relevant skills from my list
3. Briefly describes my approach or similar past work
4. Ends with a clear call-to-action and enthusiasm

Keep it natural — not overly salesy. Use a warm but professional tone."""

    return call_ai(prompt, model=model)


# ============================================================
# 2. PRICE ESTIMATOR
# ============================================================

def estimate_price(project_description, complexity="medium", model="deepseek-v4-flash"):
    """Generate a price estimate with breakdown."""
    prompt = f"""Analyze this freelancing project and provide a price estimate:

PROJECT DESCRIPTION:
{project_description}

COMPLEXITY LEVEL: {complexity} (choose: simple, medium, complex)

Respond in JSON format with:
- estimated_hours: number
- hourly_rate: number (USD)
- total_price: number (USD)
- breakdown: array of 3-5 line items with task name and estimated hours
- confidence: "low", "medium", or "high"
- reasoning: brief explanation

Use realistic freelancer rates ($25-75/hr depending on complexity).
Only output valid JSON, no markdown or explanation."""

    result = call_ai(prompt, model=model)
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        return {"raw": result, "error": "Could not parse JSON — try again"}


# ============================================================
# 3. PROJECT TIMELINE GENERATOR
# ============================================================

def generate_timeline(project_description, model="deepseek-v4-flash"):
    """Generate a milestone-based project timeline."""
    prompt = f"""Create a realistic project timeline for this freelancing gig:

{project_description}

Output as a markdown table with columns: Phase, Task, Duration (days), Deliverable.
Include 3-6 phases. Be specific and actionable.
Add a "Total" row at the bottom."""

    return call_ai(prompt, model=model)


# ============================================================
# 4. CLIENT QUESTIONNAIRE GENERATOR
# ============================================================

def generate_questions(project_description, model="deepseek-v4-flash"):
    """Generate smart questions to ask the client before bidding."""
    prompt = f"""For this project:
{project_description}

Generate 5-8 smart, professional questions I should ask the client
before submitting a proposal. Questions should:
- Clarify scope and requirements
- Uncover hidden complexity
- Show expertise and professionalism
- Help me price the project accurately

Format as a numbered list with brief explanation for why each question matters."""

    return call_ai(prompt, model=model)


# ============================================================
# 5. SKILLS GAP ANALYZER
# ============================================================

def analyze_skills_gap(project_description, your_skills, model="deepseek-v4-pro"):
    """Find gaps between your skills and project requirements."""
    prompt = f"""Compare my skills against this project's requirements:

PROJECT:
{project_description}

MY SKILLS:
{your_skills}

Output as:
1. SKILLS MATCH (what I can do well — 3-5 points)
2. SKILLS GAP (what I need to learn or subcontract — 2-4 points)
3. BID RECOMMENDATION: "strong match" / "possible with prep" / "not recommended"
4. LEARNING RESOURCES: 1-3 specific things to study if there are gaps

Keep it honest and actionable."""

    return call_ai(prompt, model=model)


# ============================================================
# DEMO: Run all tools on a sample project
# ============================================================

if __name__ == "__main__":
    SAMPLE_PROJECT = """
    I need a Python developer to build a web scraping dashboard.
    It should scrape product prices from 5 e-commerce sites daily,
    store the data in PostgreSQL, and display trends with charts.
    Must handle anti-bot detection and rate limiting. Budget is $500-2000.
    """

    MY_SKILLS = """
    - Python (5+ years, web scraping, automation)
    - PostgreSQL, SQLAlchemy
    - Flask/Django for web dashboards
    - BeautifulSoup, Selenium, Playwright
    - Chart.js, Plotly for data visualization
    - API integration (REST, GraphQL)
    """

    print("=" * 60)
    print("  🤖 FREELANCER PROPOSAL GENERATOR")
    print("  Powered by API Shop — shop.pricepulseapi.site")
    print("=" * 60)

    print("\n📝 1. COVER LETTER")
    print("-" * 40)
    try:
        letter = generate_cover_letter(SAMPLE_PROJECT, MY_SKILLS)
        print(letter)
    except Exception as e:
        print(f"[Error: {e}]")

    print("\n\n💰 2. PRICE ESTIMATE")
    print("-" * 40)
    try:
        estimate = estimate_price(SAMPLE_PROJECT, complexity="medium")
        print(json.dumps(estimate, indent=2))
    except Exception as e:
        print(f"[Error: {e}]")

    print("\n\n📅 3. PROJECT TIMELINE")
    print("-" * 40)
    try:
        timeline = generate_timeline(SAMPLE_PROJECT)
        print(timeline)
    except Exception as e:
        print(f"[Error: {e}]")

    print("\n\n❓ 4. CLIENT QUESTIONS")
    print("-" * 40)
    try:
        questions = generate_questions(SAMPLE_PROJECT)
        print(questions)
    except Exception as e:
        print(f"[Error: {e}]")

    print("\n\n🎯 5. SKILLS GAP ANALYSIS")
    print("-" * 40)
    try:
        gap = analyze_skills_gap(SAMPLE_PROJECT, MY_SKILLS)
        print(gap)
    except Exception as e:
        print(f"[Error: {e}]")

    print("\n" + "=" * 60)
    print("  🧑‍💻 Need custom automation? Hire me:")
    print("  https://freelancer.com/get/rocks081?f=give")
    print("  Get your API key: https://shop.pricepulseapi.site")
    print("=" * 60)
