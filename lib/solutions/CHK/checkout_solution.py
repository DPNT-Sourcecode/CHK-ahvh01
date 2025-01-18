# noinspection PyUnusedLocal
# skus = unicode string
from collections import defaultdict


def checkout(skus):
    if not skus:
        return -1

    products = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }
    
    processed_dict = defaultdict(0)
    total = 0
    try:
        for i in skus:
            processed_dict[i] += 1

        processed_dict

    except Exception:
        total = -1

    return total


