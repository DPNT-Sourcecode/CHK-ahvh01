from collections import defaultdict
PRODUCT_PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

DISCOUNT_OFFERS = {
    # Item: [[Amount, Price], ...]
    "A": [[5, 200], [3, 130]],
    "B": [[2, 45]],
}

freebies_offers = {
    # Product: Amount, Freebie_Product, Freebie_Amount
    "E": [2, "B", 1],
}

def checkout(skus):
    cart = defaultdict(lambda: 0)
    total = 0

    def process_freebies(cart, total):
        
    
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
        for item, offers in DISCOUNT_OFFERS.items():
            if item in cart.keys():
                for item_amount_required, discount_price in offers:
                    while True:
                        if cart[item] // item_amount_required:
                            cart[item] -= item_amount_required
                            total += discount_price
                        else:
                            break
        return total, cart
                
    def process_cart(cart, total):
        for item, amount in cart.items()
            total += amount * PRODUCT_PRICES[item]
        
        
        
        

    try:
        for i in skus:
            cart[i] += 1
        
            
        

        for item in items_order:
            amount = cart[item]

        # ! PROCESS FREEBIES
        total, cart = process_freebies(cart, total)
        # ! PROCESS DISCOUNTS
        total, cart = process_discounts(cart, total)
        # ! PROCESS REST

    except Exception as e:
        total = -1

    return total


print(checkout("EEB"))






