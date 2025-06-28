dropseer/
├── main.py
├── api.py
├── requirements.txt
├── src/
│   ├── ali_scraper.py
│   ├── amazon_scraper.py
│   ├── google_trends.py
│   ├── product_evaluator.py
│   ├── exporter.py
│   └── utils.py

## Running the API

Install the dependencies and start the FastAPI server:

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

Use `/products?keyword=your+keyword` to get the best products and `/product?keyword=your+keyword&name=Product+Name` to get details for a specific product including its image URL.
