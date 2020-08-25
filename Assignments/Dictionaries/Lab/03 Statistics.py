stock = {}
tokens = input()

while tokens != "statistics":
    tokens = tokens.split(": ")
    key = tokens[0]
    value = int(tokens[1])

    if key in stock.keys():
        stock[key] += value
    else:
        stock[key] = value

    tokens = input()

print(f"Products in stock:")
for (prod, quantity) in stock.items():
    print(f"- {prod}: {quantity}")

total_products = len(stock.keys())
total_quantity = sum(stock.values())

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
