from collections import defaultdict


def checkout(skus):
    products_prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }
    discount_offers = {
        # Item: [[Amount, New_Total], ...]
        "A": [[5, 200], [3, 130]],
        "B": [[2, 45]],
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

        # ? Workaround: Always start with E products_prices first
        items_order = list(processed_dict.keys())
        items_order.sort(reverse=True)

        for item in items_order:
            amount = processed_dict[item]
            while True:
                # If feebie is valid
                if item in freebies_offers.keys():
                    item_amount_required = freebies_offers[item][0]
                    freebie_product = freebies_offers[item][1]
                    freebies_amount = freebies_offers[item][2]
                    if (
                        amount // item_amount_required
                        and processed_dict[freebie_product] // freebies_amount
                    ):
                        total += amount * products_prices[item]
                        processed_dict[freebie_product] -= freebies_amount
                    else:
                        break

                # If discount is appliable
                elif item in discount_offers.keys():
                    possible_offers = discount_offers[item]
                    for item_amount_required, discount_price in possible_offers:
                        while True:
                            if amount // item_amount_required:
                                amount -= item_amount_required
                                total += discount_price
                            else:
                                break
                    else:
                        break

                else:
                    total += amount * products_prices[item]
                    break

    except Exception as e:
        total = -1

    return total


print(checkout("EEB"))



