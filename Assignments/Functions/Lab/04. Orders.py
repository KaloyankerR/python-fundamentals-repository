def price(product, quantity):
    product_price = 0
    if product == 'coffee':
        product_price = 1.50
    elif product == 'water':
        product_price = 1.00
    elif product == 'coke':
        product_price = 1.40
    elif product == 'snacks':
        product_price = 2.00
    product_price *= quantity
    return product_price


drink = input()
n = int(input())
print(f'{price(drink, n):.2f}')
