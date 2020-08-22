quantity = int(input())
days = int(input())
budget = 0
spirit = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        budget += ornament_set * quantity
        spirit += 5

    if day % 3 == 0:
        budget += (tree_skirt + tree_garlands) * quantity
        spirit += 13

    if day % 5 == 0:
        budget += tree_lights * quantity
        spirit += 17

    if day % 15 == 0:
        spirit += 30

    if day % 10 == 0:
        budget += (tree_skirt + tree_garlands + tree_lights)
        spirit -= 20

if days % 10 == 0:
    spirit -= 30

print(f'Total cost: {budget}\nTotal spirit: {spirit}')
