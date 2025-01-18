# noinspection PyUnusedLocal
# skus = unicode string
from collections import defaultdict


def checkout(skus):
    if not skus:
        return -1
    
    skus = skus.upper()

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
            while True
                if item in offers.keys() and amount // offers[item][0]:
                    amount -= offers[item][0]
                    total += offers[item][1]

                elif not amount // offers[item][0]:
                    total += amount * products[item]
                    break
                

    except Exception:
        total = -1

    return total




