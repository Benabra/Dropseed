from fastapi import FastAPI, HTTPException
from src.product_evaluator import find_best_products

app = FastAPI()

@app.get("/products")
def read_products(keyword: str):
    """Return a list of best products for the given keyword."""
    products = find_best_products(keyword)
    return {"products": products}

@app.get("/product")
def read_product(keyword: str, name: str):
    """Return details about a specific product."""
    products = find_best_products(keyword)
    for p in products:
        if p["name"].lower() == name.lower():
            return p
    raise HTTPException(status_code=404, detail="Product not found")
