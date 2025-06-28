import math
from typing import Iterable, Sequence


class ProductScoringModel:
    """Simple logistic regression model for product scoring."""

    def __init__(self):
        # coefficients and bias pre-determined using heuristic data
        self.weights = [0.3, 0.2, 0.3, -0.2]
        self.bias = 0.1
        
        self._model = None

    def predict(self, orders, margin, trend, competition):
        # normalize features to 0-1 scale
        features = [
            orders / 20000,
            margin / 30,
            trend / 100,
            competition / 100,
        ]
        z = self.bias
        for w, x in zip(self.weights, features):
            z += w * x
        return 1 / (1 + math.exp(-z))

    def fit(self, X: Iterable[Sequence[float]], y: Iterable[int]):
        """Train the logistic regression model using historical data."""
        # Normalize training features similar to prediction
        normalized = []
        for orders, margin, trend, competition in X:
            normalized.append([
                orders / 20000,
                margin / 30,
                trend / 100,
                competition / 100,
            ])

        # Implement a very small batch gradient descent logistic regression
        n_features = len(normalized[0]) if normalized else 0
        self.weights = [0.0 for _ in range(n_features)]
        self.bias = 0.0

        lr = 0.1
        for _ in range(1000):
            for features, target in zip(normalized, y):
                z = self.bias + sum(w * x for w, x in zip(self.weights, features))
                pred = 1 / (1 + math.exp(-z))
                error = pred - target
                for i in range(n_features):
                    self.weights[i] -= lr * error * features[i]
                self.bias -= lr * error

        self._model = None
