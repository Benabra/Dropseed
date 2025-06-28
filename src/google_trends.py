# google_trends.py
from pytrends.request import TrendReq


def get_trend_score(keyword):
    pytrends = TrendReq(hl="en-US", tz=360)
    pytrends.build_payload([keyword], cat=0, timeframe="today 12-m", geo="", gprop="")
    data = pytrends.interest_over_time()

    if not data.empty and keyword in data.columns:
        return float(data[keyword].mean())
    return 0
