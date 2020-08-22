budget = float(input())
flour_price = float(input())
cozonacs_count = 0
eggs_count = 0

egg_pack_price = flour_price * 0.75
milk_price = (flour_price + (flour_price * 0.25)) / 4
cozonac_total_price = flour_price + egg_pack_price + milk_price

while budget >= cozonac_total_price:
    budget -= cozonac_total_price
    cozonacs_count += 1
    eggs_count += 3

    if cozonacs_count % 3 == 0:
        eggs_count -= (cozonacs_count - 2)

print(f'You made {cozonacs_count} cozonacs! Now you have {eggs_count} eggs and {budget:.2f}BGN left.')
