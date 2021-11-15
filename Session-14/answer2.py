# No. 2

groceries = ["banana", "orange", "apple"]
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}


def compute_bill(food):
    """
    Computes the prices of items in a list

    Args:
        food (list): A list of food items

    Returns:
        total (int): Total price of all items in a list
    """
    total = 0
    for item in food:
        total += prices.get(item)  # Adds price of item to current total
    return total


print(compute_bill(groceries))


def compute_bill(food):
    """
    Computes the prices of items in a list if their stock is greather than 0.
    Also decreases existing stock by 1

    Args:
        food (list): A list of food items

    Returns:
        total (int): Total price of items with stock greater than 0 in a list
    """
    total = 0
    for item in food:
        if stock.get(item) > 0:  # Checks if item stock is greater than 0
            total += prices.get(item)  # Adds price of item to current total
            stock[item] -= 1  # Reduces stock of item by 1
    return total


print(compute_bill(groceries))

print(stock)