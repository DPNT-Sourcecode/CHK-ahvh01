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
    offers = {
        # Item: [Amount, Total]
        "A": [3, 130],
        "B": [2, 45],   
    }
    processed_dict = defaultdict(0)
    total = 0
    try:
        for i in skus:
            processed_dict[i] += 1

        for item, amount in processed_dict.items():
            if item in offers.keys():
                amount % offers

    except Exception:
        total = -1

    return total



