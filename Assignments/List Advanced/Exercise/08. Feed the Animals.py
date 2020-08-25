animals = {}
areas = {}
tokens = input()

while tokens != "Last Info":
    tokens = tokens.split(":")
    cmd = tokens[0]
    animal = tokens[1]
    food = int(tokens[2])
    area = tokens[3]

    if cmd == "Add":
        if animal not in animals:
            animals[animal] = food
            if area not in areas:
                areas[area] = 1
            else:
                areas[area] += 1
        else:
            animals[animal] += food

    elif cmd == "Feed":
        if animal in animals:
            animals[animal] -= food
            if animals[animal] <= 0:
                print(f"{animal} was successfully fed")
                animals.pop(animal)
                areas[area] -= 1
                if areas[area] <= 0:
                    areas.pop(area)

    tokens = input()

animals_sorted = dict(sorted(animals.items(), key=lambda x: (-x[1], x[0])))
areas_sorted = dict(sorted(areas.items(), key=lambda x: -x[1]))

print("Animals:")
for (k, v) in animals_sorted.items():
    print(f"{k} -> {v}g")

print("Areas with hungry animals:")
for (k, v) in areas_sorted.items():
    print(f"{k} : {v}")
