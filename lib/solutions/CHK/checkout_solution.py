# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    is_illegal = False
    products = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        " ": 0,
    }
    total = -1
    try:
        for item in skus:
            total += products[item]

    except Exception:
        pass

    return total

