# noinspection PyUnusedLocal
# skus = unicode string
from collections import defaultdict

PRODUCT_PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    # ---
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}

DISCOUNT_OFFERS = {
    # Item: [[Amount, Price], ...]
    "A": [[5, 200], [3, 130]],
    "B": [[2, 45]],
    "H": [[5, 45], [10, 80]],
    "K": [[2000, 150]],
    "P": [[5, 200]],
    "Q": [[3, 80]],
    "V": [[2, 90], [3, 130]],
}

FREEBIES_OFFERS = {
    # Product: Amount, Freebie_Product, Freebie_Amount
    "E": [2, "B", 1],
    "F": [2, "F", 1],
    "N": [3, "M", 1],
    "R": [3, "Q", 1],
    "U": [3, "U", 1],
}


def process_freebies(cart, total):
    for item, offer in FREEBIES_OFFERS.items():
        if cart.get(item):
            item_amount_required, freebie_product, freebies_amount = offer
            if item == freebie_product:
                item_amount_required += freebies_amount

            while True:
                if (
                    cart[item] // item_amount_required
                    and cart[freebie_product] // freebies_amount
                ):
                    if item == freebie_product:
                        total += (
                            item_amount_required - freebies_amount
                        ) * PRODUCT_PRICES[item]
                        cart[item] -= item_amount_required
                    else:
                        total += item_amount_required * PRODUCT_PRICES[item]
                        cart[item] -= item_amount_required
                        cart[freebie_product] -= freebies_amount
                else:
                    break

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
    for item, amount in cart.items():
        total += amount * PRODUCT_PRICES[item]
    return total, cart


def checkout(skus):
    cart = defaultdict(lambda: 0)
    total = 0

    try:
        for i in skus:
            cart[i] += 1

        total, cart = process_freebies(cart, total)
        total, cart = process_discounts(cart, total)
        total, cart = process_cart(cart, total)

    except Exception as e:
        total = -1

    return total

