#!/bin/bash
# API Shop Demo — Quick curl examples
# Get your key: https://shop.pricepulseapi.site

: "${APISHOP_KEY:?Set APISHOP_KEY environment variable}"

API_URL="https://pricepulseapi.site/v1/chat/completions"

echo "🤖 API Shop — curl demo"
echo "========================"
echo ""

# Simple chat
echo "📝 Simple chat:"
curl -s "$API_URL" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $APISHOP_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Hi! Say hello in 3 languages."}]
  }' | python3 -c "import sys,json; print(json.load(sys.stdin)['choices'][0]['message']['content'])"

echo ""
echo ""

# Coding help
echo "💻 Coding help:"
curl -s "$API_URL" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $APISHOP_KEY" \
  -d '{
    "model": "deepseek-v4-pro",
    "messages": [{"role": "user", "content": "Write a one-line bash command to find the 5 largest files in current directory."}]
  }' | python3 -c "import sys,json; print(json.load(sys.stdin)['choices'][0]['message']['content'])"

echo ""
echo "========================"
echo "✨ Get your key: https://shop.pricepulseapi.site"
