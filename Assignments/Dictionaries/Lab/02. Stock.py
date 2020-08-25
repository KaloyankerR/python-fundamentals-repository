products = input().split(" ")
bakery = {}

for product in range(0, len(products), 2):
    key = products[product]
    value = int(products[product + 1])
    bakery[key] = value

wanted_items = input().split(" ")
for item in wanted_items:
    if item in bakery.keys():
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
