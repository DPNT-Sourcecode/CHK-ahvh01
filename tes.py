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
    

    processed_dict = defaultdict(lambda: 0)
    total = 0

    def process_freebies(cart):
        freebies_offers = {
            # Product: Amount, Freebie_Product, Freebie_Amount
            "E": [2, "B", 1],
        }
        
        for item, offer in freebies_offers.items():
            if cart.get(item):
                item_amount_required, freebie_product, freebies_amount = offer
                if (
                    amount // item_amount_required
                    and cart[freebie_product] // freebies_amount
                ):
                    total += amount * cart[item]
                    cart[freebie_product] -= freebies_amount
                else:
                    break
                
        
        
        

    try:
        for i in skus:
            processed_dict[i] += 1
            

        # ? Workaround: Always start with E products_prices first
        items_order = list(processed_dict.keys())
        items_order.sort(reverse=True)
        
        # ! PROCESS FREEBIES
        # ! PROCESS DISCOUNTS
        # ! PROCESS REST

        for item in items_order:
            amount = processed_dict[item]
            while True:
                # If feebie is valid
                if item in freebies_offers.keys():
                    

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




