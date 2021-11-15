# No. 1

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

for key in prices: # Iterates through all 4 keys in prices
    print(key, f"price: {prices.get(key)}", f"stock: {stock.get(key)}", sep="\n") # Prints all the info in 3 different lines
    print()

total = 0
for key in prices:
    x = prices.get(key) * stock.get(key) # Multiplies value with stock and adds it to total
    print(f"{key}: {x}")
    total += x
print(f"Total: {total}")