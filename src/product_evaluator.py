# src/product_evaluator.py
from .ali_scraper import get_china_products
from .amazon_scraper import count_amazon_listings, get_amazon_price_estimate
from .google_trends import get_trend_score
from .utils import normalize


def score_product(p):
    trend = get_trend_score(p["name"])
    competition = count_amazon_listings(p["name"])
    amazon_price = get_amazon_price_estimate(p["name"])
    margin = amazon_price - p["china_price"]

    orders_score = normalize(p["orders"], 0, 20000)
    trend_score = normalize(trend, 0, 100)
    comp_score = normalize(100 - competition, 0, 100)  # less is better
    margin_score = normalize(margin, 0, 30)

    final_score = (
        orders_score * 0.25
        + trend_score * 0.35
        + comp_score * 0.25
        + margin_score * 0.15
    )

    p.update(
        {
            "trend": trend,
            "competition": competition,
            "margin": margin,
            "score": final_score,
            "amazon_price_est": amazon_price,
        }
    )

    return p


def find_best_products(keyword):
    products = get_china_products(keyword)
    return sorted(
        [score_product(p) for p in products], key=lambda x: x["score"], reverse=True
    )
