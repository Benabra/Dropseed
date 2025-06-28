import csv
from datetime import datetime

from .google_trends import get_trend_score


def append_daily_trend(keyword, filename="trend_timeseries.csv"):
    """Append today's trend score for a keyword to a CSV time series."""
    trend = get_trend_score(keyword)
    row = {
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "keyword": keyword,
        "trend": trend,
    }
    write_header = False
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            pass
    except FileNotFoundError:
        write_header = True

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(row)
