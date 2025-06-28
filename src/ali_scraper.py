# ali_scraper.py
import requests
from bs4 import BeautifulSoup

def get_china_products(keyword, max_results=5):
    url = f"https://www.aliexpress.com/wholesale?SearchText={keyword.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US"
    }

    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    products = []

    items = soup.select("div[data-widget-type='productCard']")[:max_results]

    for item in items:
        name_tag = item.select_one("a._3t7zg")
        price_tag = item.select_one("div._12A8D")
        order_tag = item.select_one("span._1kNf9")

        if not (name_tag and price_tag):
            continue

        name = name_tag.text.strip()
        price = float(price_tag.text.replace('$', '').split()[0])
        orders = int(order_tag.text.split()[0].replace(',', '')) if order_tag else 0

        products.append({
            "name": name,
            "china_price": price,
            "orders": orders,
            "rating": 4.5  # Placeholder
        })

    return products
