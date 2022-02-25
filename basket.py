import pdb
DEFAULT_INITIAL_BASKET = ["orange", "apple"]

def create_picnic_basket(healthy, hungry, initial_basket=DEFAULT_INITIAL_BASKET):
    basket = initial_basket
    if healthy:
        breakpoint()
        basket.append("strawberry")
    else:
        breakpoint()
        basket.append("jam")

    if hungry:
        breakpoint()
        basket.append("sandwich")
    return basket

# Reproducer
print("First basket:", create_picnic_basket(True, False))
print("Second basket:", create_picnic_basket(False, True, ["tea"]))
print("Third basket:", create_picnic_basket(True, True))
print("WHY DO I HAVE 2 STRAWBERRIES WHEN I AM HEALTH AND HUNGRY?")
