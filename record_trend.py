import argparse

from src.trend_tracker import append_daily_trend


def main(keyword: str):
    append_daily_trend(keyword)
    print("Trend data recorded")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Record daily trend score")
    parser.add_argument("keyword", help="Keyword to track")
    args = parser.parse_args()
    main(args.keyword)
