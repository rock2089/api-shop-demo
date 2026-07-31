"""
LangChain + API Shop Integration Demo
======================================
Use LangChain with API Shop for RAG, chains, agents, and more.
Cheaper than OpenAI — same API format, same LangChain compatibility.

API Shop: https://shop.pricepulseapi.site
Freelancer: https://freelancer.com/get/rocks081?f=give
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage

# ============================================================
# 1. BASIC CHAT — Use API Shop as drop-in replacement for OpenAI
# ============================================================

llm = ChatOpenAI(
    model="deepseek-v4-flash",
    openai_api_key="your-api-key",          # Get key at shop.pricepulseapi.site
    openai_api_base="https://pricepulseapi.site/v1",
    temperature=0.7,
    max_tokens=500,
)

response = llm.invoke("Explain Python decorators in one sentence.")
print("1. BASIC CHAT:", response.content)

# ============================================================
# 2. CHAIN — Prompt template → LLM → Output parser
# ============================================================

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Python code reviewer. Be concise and practical."),
    ("human", "Review this code:\n\n```python\n{code}\n```")
])

chain = prompt | llm | StrOutputParser()

code_to_review = """
def get_users():
    users = []
    for i in range(100):
        r = requests.get(f"https://api.example.com/users/{i}")
        users.append(r.json())
    return users
"""

result = chain.invoke({"code": code_to_review})
print("\n2. CHAIN REVIEW:", result[:300])

# ============================================================
# 3. SYSTEM/USER MESSAGES — Direct message formatting
# ============================================================

messages = [
    SystemMessage(content="You extract JSON from text. Return ONLY valid JSON."),
    HumanMessage(content="User John (age 30, email john@example.com) lives in NYC.")
]

response = llm.invoke(messages)
print("\n3. JSON EXTRACTION:", response.content)

# ============================================================
# 4. STREAMING — Real-time token output (DeepSeek V4 Pro)
# ============================================================

llm_pro = ChatOpenAI(
    model="deepseek-v4-pro",
    openai_api_key="your-api-key",
    openai_api_base="https://pricepulseapi.site/v1",
    temperature=0.5,
    streaming=True,
)

print("\n4. STREAMING:", end=" ")
for chunk in llm_pro.stream("Write a haiku about API programming."):
    print(chunk.content, end="", flush=True)
print()

print("\n✅ Done! Visit https://shop.pricepulseapi.site for your API key.")
print("👨‍💻 Need custom AI automation? Hire me: https://freelancer.com/get/rocks081?f=give")
