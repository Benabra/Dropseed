dropseer/
├── main.py
├── api.py
├── requirements.txt
├── src/
│   ├── ali_scraper.py
│   ├── amazon_scraper.py
│   ├── google_trends.py
│   ├── product_evaluator.py
│   ├── ml_model.py
│   ├── exporter.py
│   └── utils.py
├── train_model.py
├── record_trend.py
└── src/trending_tags.py

## Running the API

Install the dependencies and start the FastAPI server. The product score is now
computed using a lightweight logistic regression model defined in `ml_model.py`:

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

Use `/products?keyword=your+keyword` to get the best products and `/product?keyword=your+keyword&name=Product+Name` to get details for a specific product including its image URL.

## Training the model

Provide a CSV file with columns `orders`, `margin`, `trend`, `competition` and `label` (1 if a product became a best seller, else 0). Run:

```bash
python train_model.py your_training_data.csv
```

The learned weights will be written to `trained_weights.csv`.

## Recording trend data

To build a time series of Google Trends data run daily:

```bash
python record_trend.py "your keyword"
```

This will append the current trend score to `trend_timeseries.csv`.

## Fetching trending tags

Retrieve the latest trending hashtags from TikTok:

```python
from src.trending_tags import get_tiktok_trending_hashtags

print(get_tiktok_trending_hashtags())
```
