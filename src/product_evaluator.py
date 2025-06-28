# src/product_evaluator.py
from .ali_scraper import get_china_products
from .amazon_scraper import count_amazon_listings, get_amazon_price_estimate
from .google_trends import get_trend_score
from .ml_model import ProductScoringModel

model = ProductScoringModel()


def score_product(p):
    trend = get_trend_score(p["name"])
    competition = count_amazon_listings(p["name"])
    amazon_price = get_amazon_price_estimate(p["name"])
    margin = amazon_price - p["china_price"]


    final_score = model.predict(
        p["orders"],
        margin,
        trend,
        competition,
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
