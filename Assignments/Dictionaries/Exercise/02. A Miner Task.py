tokens = input()
dictionary = {}
counter = 1
resource = ""

while tokens != "stop":
    if counter % 2 == 0:
        quantity = int(tokens)

        if resource in dictionary.keys():
            dictionary[resource] += quantity
        else:
            dictionary[resource] = quantity

    else:
        resource = tokens

    counter += 1
    tokens = input()


for (key, value) in dictionary.items():
    print(f"{key} -> {value}")
