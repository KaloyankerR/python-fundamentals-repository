tokens = input()
products = {}

while tokens != "buy":
    tokens = tokens.split(" ")
    product = tokens[0]
    price = float(tokens[1])
    quantity = int(tokens[2])

    if product in products:
        products[product][0] = price
        products[product][1] += quantity
    else:
        products[product] = [price, quantity]

    tokens = input()

for (k, v) in products.items():
    product_price = v[0]
    product_quantity = v[1]
    total = product_price * product_quantity

    print(f"{k} -> {total:.2f}")
