items = input().split(" ")
bakery = {}

for item in range(0, len(items), 2):
    key = items[item]
    value = int(items[item + 1])
    bakery[key] = value

print(bakery)
