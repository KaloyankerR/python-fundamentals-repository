sides_dict = {}
tokens = input()

while tokens != "Lumpawaroo":
    if "|" in tokens:
        tokens = tokens.split(" | ")
        side = tokens[0]
        user = tokens[1]

        if side not in sides_dict.keys():
            sides_dict[side] = []

        all_users = [item for x in sides_dict.values() for item in x]

        if user not in all_users:
            sides_dict[side].append(user)

    else:
        tokens = tokens.split(" -> ")
        user = tokens[0]
        side = tokens[1]
        old_side = ""

        if side not in sides_dict.keys():
            sides_dict[side] = []

        for k in sides_dict.keys():
            for v in sides_dict[k]:
                if user == v:
                    old_side = k
                    break

        if old_side != "":
            sides_dict[old_side].remove(user)
            sides_dict[side].append(user)

        else:
            sides_dict[side].append(user)

        print(f"{user} joins the {side} side!")
    tokens = input()

filtered_side_dict = sides_dict.copy()
for (k, v) in sides_dict.items():
    if len(v) == 0:
        filtered_side_dict.pop(k)

sorted_sides_dict = dict(sorted(filtered_side_dict.items(), key=lambda x: (-len(x[1]), x[0])))

for (k, v) in sorted_sides_dict.items():
    print(f"Side: {k}, Members: {len(v)}")
    for person in sorted(v):
        print(f"! {person}")
