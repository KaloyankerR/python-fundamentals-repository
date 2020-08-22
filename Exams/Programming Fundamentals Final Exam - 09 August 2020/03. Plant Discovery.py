plants_info = {}
n = int(input())

for i in range(n):
    args = input().split("<->")
    plant_discovered = args[0]
    plant_rarity = int(args[1])
    if plant_discovered in plants_info:
        plants_info[plant_discovered]["rarity"] = plant_rarity
    else:
        plants_info[plant_discovered] = {"rarity": None, "ratings": []}
        plants_info[plant_discovered]["rarity"] = plant_rarity

tokens = input()
while tokens != "Exhibition":
    tokens = tokens.split(" ")
    cmd = tokens[0]

    if cmd == "Rate:":
        symbol = tokens[2]
        if symbol != "-":
            print("error")
        else:
            plant = tokens[1]
            if plant not in plants_info:
                print("error")
            else:
                rating = int(tokens[3])
                plants_info[plant]["ratings"].append(rating)

    elif cmd == "Update:":
        symbol = tokens[2]
        if symbol != "-":
            print("error")
        else:
            plant = tokens[1]
            if plant not in plants_info:
                print("error")
            else:
                new_rarity = int(tokens[3])
                plants_info[plant]["rarity"] = new_rarity

    elif cmd == "Reset:":
        plant = tokens[1]
        if plant not in plants_info:
            print("error")
        else:
            plants_info[plant]["ratings"] = []

    else:
        print("error")

    tokens = input()

for k in plants_info.keys():
    plants_ratings = plants_info[k]["ratings"]

    if len(plants_ratings) == 0:
        plants_info[k]["ratings"] = 0
    else:
        plants_info[k]["ratings"] = sum(plants_ratings) / len(plants_ratings)
sorted_plants_info = dict(sorted(plants_info.items(), key=lambda x: (x[1]["rarity"], x[1]["ratings"]), reverse=True))

print("Plants for the exhibition:")
for (k, v) in sorted_plants_info.items():
    rarity = v["rarity"]
    average_rating = v["ratings"]
    print(f"- {k}; Rarity: {rarity}; Rating: {average_rating:.2f}")
