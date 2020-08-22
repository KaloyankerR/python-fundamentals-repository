items = input().split('|')
budget = float(input())
bought_items = []
BUDGET = budget

for item in items:
    item = item.split('->')
    item_type = item[0]
    price = float(item[1])

    if item_type == 'Clothes':
        if price <= 50.00 and budget >= price:
            bought_items.append(price)
            budget -= price

    elif item_type == 'Shoes':
        if price <= 35.00 and budget >= price:
            bought_items.append(price)
            budget -= price

    elif item_type == 'Accessories':
        if price <= 20.50 and budget >= price:
            bought_items.append(price)
            budget -= price

for i in range(len(bought_items)):
    bought_items[i] = bought_items[i] + (bought_items[i] * 0.40)
    print(f'{bought_items[i]:.2f}', end=' ')


print()
items_sum = sum(bought_items)
print(f'Profit: {(items_sum + budget) - BUDGET:.2f}')
if (items_sum + budget) >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
