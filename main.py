# main.py
from src.exporter import export_to_csv
from src.product_evaluator import find_best_products


def main():
    keyword = input("Enter product keyword: ").strip()
    top_products = find_best_products(keyword)

    print("\nTop Dropshipping Products:\n")
    for p in top_products:
        print(
            f"{p['name']}\n  Score: {p['score']:.2f} | Orders: {p['orders']} | Margin: ${p['margin']:.2f} | Trend: {p['trend']:.2f} | Comp: {p['competition']}\n"
        )

    export_to_csv(top_products)
    print("\n✔ Results saved to top_products.csv")


if __name__ == "__main__":
    main()
