# src/amazon_scraper.py
import requests
from bs4 import BeautifulSoup


def count_amazon_listings(keyword):
    url = f"https://www.amazon.com/s?k={keyword.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    return len(soup.select("div[data-component-type='s-search-result']"))


def get_amazon_price_estimate(keyword):
    url = f"https://www.amazon.com/s?k={keyword.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")

    prices = []
    for p in soup.select("span.a-price > span.a-offscreen"):
        try:
            price = float(p.text.replace("$", "").strip())
            prices.append(price)
        except:
            continue

    return sum(prices) / len(prices) if prices else 0
