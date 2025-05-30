import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# ✅ ওয়েবসাইট লিংক (উদাহরণ)
url = "https://example.com"

# ✅ ডেটা নামাও
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# ✅ ডেটা খুঁজে বের করো (উদাহরণ — class অনুযায়ী নিজে বদলাবে)
products = []
for item in soup.select(".product-item"):
    name = item.select_one(".product-name").text.strip()
    price = item.select_one(".product-price").text.strip()
    
    products.append({
        "name": name,
        "price": price
    })

# ✅ JSON ফাইলে লিখে রাখো
filename = f"products_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print(f"Saved to {filename}")
