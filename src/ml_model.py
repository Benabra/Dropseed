import math
from typing import Iterable, Sequence

from sklearn.linear_model import LogisticRegression


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

        clf = LogisticRegression()
        clf.fit(normalized, list(y))

        self.weights = clf.coef_[0].tolist()
        self.bias = float(clf.intercept_[0])
        self._model = clf
