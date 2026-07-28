/**
 * API Shop - Node.js Chat Example
 * Uses native fetch (Node.js 18+)
 */
const API_KEY = "YOUR_API_KEY";
const API_URL = "https://pricepulseapi.site/v1/chat/completions";

async function chat(prompt) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json", "Authorization": `Bearer ${API_KEY}` },
    body: JSON.stringify({ model: "deepseek-chat", messages: [{ role: "user", content: prompt }], max_tokens: 300 })
  });
  const data = await response.json();
  return { content: data.choices[0].message.content, tokens: data.usage.total_tokens };
}

chat("What are the top 3 JavaScript frameworks in 2026?").then(result => {
  console.log(result.content);
  console.log(`\nTokens used: ${result.tokens}`);
}).catch(console.error);
