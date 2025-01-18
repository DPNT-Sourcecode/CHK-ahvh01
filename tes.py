from collections import defaultdict


def checkout(skus):
    products = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }
    offers = {
        # Item: {Amount, New_Total}
        "A": {3: 130, 5: 200},
        "B": {2, 45},
    }
    # ! E OFFER???

    processed_dict = defaultdict(lambda: 0)
    total = 0

    try:
        for i in skus:
            processed_dict[i] += 1

        items_order = list(processed_dict.keys())
        items_order.sort(reverse=True)
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


print(checkout("AAAEEBB"))


