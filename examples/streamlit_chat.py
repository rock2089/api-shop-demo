#!/usr/bin/env python3
"""
🖥️  API Shop Web Chat — Streamlit-powered chat interface

A beautiful, interactive web UI for the API Shop AI models.
Features streaming responses, model switching, cost tracking, and chat export.

Usage:
    pip install streamlit
    streamlit run examples/streamlit_chat.py

Then open http://localhost:8501 in your browser.
"""

import streamlit as st
import requests
import json
import time
import os
from datetime import datetime

# ── Page Config ──────────────────────────────────────────────────
st.set_page_config(
    page_title="API Shop Chat",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .cost-badge {
        background: #f0f0f0;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        color: #666;
    }
    .model-badge {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.75rem;
        margin-left: 0.5rem;
    }
    .footer {
        text-align: center;
        padding: 1rem;
        color: #999;
        font-size: 0.85rem;
    }
    .footer a { color: #667eea; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p class="main-header">🤖 API Shop Chat</p>', unsafe_allow_html=True)
    st.caption("Powered by [shop.pricepulseapi.site](https://shop.pricepulseapi.site)")

    st.divider()

    # API Key
    api_key = st.text_input(
        "🔑 API Key",
        type="password",
        placeholder="sk-...",
        help="Get your key at shop.pricepulseapi.site"
    )

    # Model selection
    st.subheader("🧠 Model")
    model = st.selectbox(
        "Choose a model",
        ["deepseek-v4-flash", "deepseek-v4-pro", "kimi-k2", "deepseek-r1-0528"],
        format_func=lambda x: {
            "deepseek-v4-flash": "⚡ DeepSeek V4 Flash (Fast)",
            "deepseek-v4-pro": "🧠 DeepSeek V4 Pro (Smart)",
            "kimi-k2": "📚 Kimi K2 (128K Context)",
            "deepseek-r1-0528": "🔍 DeepSeek R1 (Reasoning)",
        }.get(x, x),
        help="Different models for different tasks — Flash is fastest, Pro is smartest"
    )

    # Parameters
    st.subheader("⚙️ Parameters")
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.1, help="Higher = more creative, Lower = more focused")
    max_tokens = st.slider("Max Tokens", 64, 4096, 2048, 64, help="Maximum response length")

    st.divider()

    # Stats
    st.subheader("📊 Session Stats")
    if "total_cost" not in st.session_state:
        st.session_state.total_cost = 0.0
        st.session_state.total_tokens = 0
        st.session_state.msg_count = 0

    col1, col2 = st.columns(2)
    col1.metric("Messages", st.session_state.msg_count)
    col2.metric("Tokens", f"{st.session_state.total_tokens:,}")

    col3, col4 = st.columns(2)
    col3.metric("Est. Cost", f"${st.session_state.total_cost:.4f}")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.total_cost = 0.0
        st.session_state.total_tokens = 0
        st.session_state.msg_count = 0
        st.rerun()

    # System prompt
    with st.expander("🛠️ System Prompt"):
        system_prompt = st.text_area(
            "Set a system prompt",
            value="You are a helpful AI assistant. Be concise and accurate.",
            height=100,
        )

    st.divider()

    # Footer
    st.markdown("""
    <div class="footer">
        🔌 <a href="https://shop.pricepulseapi.site" target="_blank">Get API Key</a> ·
        🐙 <a href="https://github.com/rock2089/api-shop-demo" target="_blank">GitHub</a> ·
        👨‍💻 <a href="https://www.freelancer.com/get/rocks081?f=give" target="_blank">Hire Me</a>
    </div>
    """, unsafe_allow_html=True)

# ── Main Chat Area ───────────────────────────────────────────────
st.title("💬 Chat with AI")
st.caption(f"Active model: **{model}** · Temperature: {temperature} · Max tokens: {max_tokens}")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "model" in msg:
            st.caption(f"<span class='model-badge'>{msg['model']}</span> · <span class='cost-badge'>${msg.get('cost', 0):.5f}</span>", unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    if not api_key:
        st.error("⚠️ Please enter your API key in the sidebar.")
        st.stop()

    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call API
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        API_URL = "https://pricepulseapi.site/v1/chat/completions"

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True,
        }

        try:
            with requests.post(
                API_URL,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
                stream=True,
                timeout=60,
            ) as response:
                if response.status_code != 200:
                    try:
                        error_data = response.json()
                        st.error(f"❌ API Error: {error_data}")
                    except Exception:
                        st.error(f"❌ HTTP {response.status_code}: {response.text[:200]}")
                    st.stop()

                for line in response.iter_lines():
                    if line:
                        line = line.decode("utf-8")
                        if line.startswith("data: "):
                            data = line[6:]
                            if data == "[DONE]":
                                break
                            try:
                                chunk = json.loads(data)
                                delta = chunk.get("choices", [{}])[0].get("delta", {})
                                content = delta.get("content", "")
                                if content:
                                    full_response += content
                                    message_placeholder.markdown(full_response + "▌")
                            except json.JSONDecodeError:
                                continue
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection error: {e}")
            st.stop()

        # Final render
        message_placeholder.markdown(full_response)

        # Estimate cost (approximate)
        token_estimate = len(prompt.split()) + len(full_response.split())
        cost_per_1k = {
            "deepseek-v4-flash": 0.0001,
            "deepseek-v4-pro": 0.0003,
            "kimi-k2": 0.0003,
            "deepseek-r1-0528": 0.0003,
        }
        cost = (token_estimate / 1000) * cost_per_1k.get(model, 0.0003)

        # Update stats
        st.session_state.total_cost += cost
        st.session_state.total_tokens += token_estimate
        st.session_state.msg_count += 1

        # Save assistant message
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response,
            "model": model,
            "cost": cost,
        })

        # Show cost badge
        st.caption(f"<span class='model-badge'>{model}</span> · <span class='cost-badge'>${cost:.5f} est.</span>", unsafe_allow_html=True)

# ── Action Buttons ───────────────────────────────────────────────
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📋 Copy Last Response", use_container_width=True):
        if st.session_state.messages:
            last = st.session_state.messages[-1]
            if last["role"] == "assistant":
                st.code(last["content"], language="markdown")

with col2:
    if st.button("💾 Export Chat", use_container_width=True):
        export = "\n\n".join([
            f"**{m['role'].upper()}**: {m['content']}"
            for m in st.session_state.messages
        ])
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        st.download_button(
            "📥 Download chat.md",
            export,
            f"chat_{timestamp}.md",
            "text/markdown",
        )

with col3:
    if st.button("🔄 New Session", use_container_width=True):
        st.session_state.messages = []
        st.session_state.total_cost = 0.0
        st.session_state.total_tokens = 0
        st.session_state.msg_count = 0
        st.rerun()
