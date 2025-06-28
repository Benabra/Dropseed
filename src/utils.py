# src/utils.py
def normalize(value, min_val, max_val):
    if value <= min_val:
        return 0.0
    elif value >= max_val:
        return 1.0
    return (value - min_val) / (max_val - min_val)
