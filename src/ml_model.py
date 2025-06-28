import math

class ProductScoringModel:
    """Simple logistic regression model for product scoring."""

    def __init__(self):
        # coefficients and bias pre-determined using heuristic data
        self.weights = [0.3, 0.2, 0.3, -0.2]
        self.bias = 0.1

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
