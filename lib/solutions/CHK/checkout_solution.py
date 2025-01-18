# noinspection PyUnusedLocal
# skus = unicode string
from collections import defaultdict


def checkout(skus):
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
    processed_dict = defaultdict(lambda: 0)
    total = 0

    try:
        for i in skus:
            processed_dict[i] += 1

        for item, amount in processed_dict.items():
            while True:
                if item in offers.keys() and amount // offers[item][0]:
                    amount -= offers[item][0]
                    total += offers[item][1]
                else:
                    total += amount * products[item]
                    break

    except Exception as e:
        total = -1

    return total







