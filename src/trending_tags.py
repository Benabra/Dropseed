import requests
from bs4 import BeautifulSoup


def get_tiktok_trending_hashtags(limit=10):
    """Scrape trending hashtags from TikTok discover page."""
    url = "https://www.tiktok.com/discover"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")

    tags = []
    for a in soup.select("a[href^='/tag/']"):
        tag = a.text.strip().lstrip('#')
        if tag and tag not in tags:
            tags.append(tag)
        if len(tags) >= limit:
            break
    return tags
