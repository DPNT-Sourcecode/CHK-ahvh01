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

        # ? Workaround: Always start with E products_prices first
        items_order = list(processed_dict.keys())
        items_order.sort(reverse=True)

        for item in items_order:
            amount = amount
            while True:
                # If feebie is valid
                if (
                    item in freebies_offers.keys()
                    and amount // freebies_offers[item][0]
                    # if products_prices left
                    and processed_dict[freebies_offers[item][1]]
                    // freebies_offers[item][2]
                ):
                    total += amount * products_prices[item]
                    total -= (
                        freebies_offers[item][2]
                        * products_prices[freebies_offers[item][1]]
                    )
                    
                # If discount is appliable
                elif (
                    item in discount_offers.keys()
                    and amount // discount_offers[item][0]
                ):
                    amount -= discount_offers[item][0]
                    total += discount_offers[item][1]

                else:
                    total += amount * products_prices[item]
                    break

    except Exception as e:
        total = -1

    return total


print(checkout("AAAEEBB"))






