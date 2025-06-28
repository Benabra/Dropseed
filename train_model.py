import csv
from pathlib import Path

from src.ml_model import ProductScoringModel


def load_training_data(path: str):
    X = []
    y = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            X.append(
                [
                    float(row["orders"]),
                    float(row["margin"]),
                    float(row["trend"]),
                    float(row["competition"]),
                ]
            )
            y.append(int(row["label"]))
    return X, y


def main(data_file: str, output_file: str = "trained_weights.csv"):
    X, y = load_training_data(data_file)
    model = ProductScoringModel()
    model.fit(X, y)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["bias"] + ["w" + str(i) for i in range(len(model.weights))])
        writer.writerow([model.bias] + model.weights)
    print(f"Weights saved to {output_file}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Train product scoring model")
    parser.add_argument("data", help="Path to training CSV file")
    parser.add_argument("--out", default="trained_weights.csv", help="Output file for weights")
    args = parser.parse_args()
    main(args.data, args.out)
