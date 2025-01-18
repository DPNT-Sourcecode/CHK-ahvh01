from collections import defaultdict


def checkout(skus):
    products = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }
    discount_offers = {
        # Item: {Amount, New_Total}
        "A": {3: 130, 5: 200},
        "B": {2: 45},
    }
    freebies_offers = {
        # Product: Amount, Freebie_Product, Freebie_Amount
        "E": [2, "B", 1],
    }

    processed_dict = defaultdict(lambda: 0)
    total = 0

    try:
        for i in skus:
            processed_dict[i] += 1

        # ? Workaround: Always start with E products first
        items_order = list(processed_dict.keys())
        items_order.sort(reverse=True)

        for item in items_order:
            while True:
                # If discount is appliable
                if (
                    item in discount_offers.keys()
                    and processed_dict[item] // discount_offers[item][0]
                ):
                    processed_dict[item] -= discount_offers[item][0]
                    total += discount_offers[item][1]

                # If feebie is valid
                elif (
                    item in freebies_offers.keys()
                    and processed_dict[item] // freebies_offers[item][0]
                    # if products left
                    and processed_dict[freebies_offers[item][1]] // freebies_offers[item][2]
                ):
                else:
                    total += amount * products[item]
                    break

    except Exception as e:
        total = -1

    return total


print(checkout("AAAEEBB"))





