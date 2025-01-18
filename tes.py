from collections import defaultdict


def checkout(skus):
    products_prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }
    

    cart = defaultdict(lambda: 0)
    total = 0

    def process_freebies(cart, total):
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
        
        return total, cart

    
    def process_discounts(cart, total):
        discount_offers = {
            # Item: [[Amount, New_Total], ...]
            "A": [[5, 200], [3, 130]],
            "B": [[2, 45]],
        }
        
        for item, offers in discount_offers.items():
            if item in discount_offers.keys():
                for item_amount_required, discount_price in offers:
                    while True:
                        if amount // item_amount_required:
                            amount -= item_amount_required
                            total += discount_price
                
        
        
        

    try:
        for i in skus:
            cart[i] += 1
        
        # ! PROCESS FREEBIES
        total, cart = process_freebies(cart, total)
        # ! PROCESS DISCOUNTS
        total, cart = process_discounts(cart, total)
            
        
        # ! PROCESS REST

        for item in items_order:
            amount = cart[item]
            while True:
                    

                # If discount is appliable
                el

                else:
                    total += amount * products_prices[item]
                    break

    except Exception as e:
        total = -1

    return total


print(checkout("EEB"))





