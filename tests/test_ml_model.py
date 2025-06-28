import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.ml_model import ProductScoringModel


def test_fit_updates_weights():
    model = ProductScoringModel()
    X = [
        [1000, 10, 50, 20],
        [2000, 20, 60, 30],
        [3000, 15, 40, 25],
        [4000, 25, 70, 40],
    ]
    y = [0, 0, 1, 1]
    old_weights = model.weights.copy()
    model.fit(X, y)
    assert model.weights != old_weights
