stores = {}
tokens = input()

while tokens != "END":
    tokens = tokens.split("->")
    command = tokens[0]
    store = tokens[1]

    if command == "Add":
        if store not in stores:
            stores[store] = []

        items = [x for x in tokens[2].split(",")]
        [stores[store].append(x) for x in items]

    elif command == "Remove":
        if store in stores:
            stores.pop(store)

    tokens = input()

sorted_stores = dict(sorted(stores.items(), key=lambda x: (len(x[1]), x[0]), reverse=True))

print("Stores list:")
for (k, v) in sorted_stores.items():
    print(k)
    for item in v:
        print(f"<<{item}>>")
