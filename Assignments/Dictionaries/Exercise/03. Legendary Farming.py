def print_dict(dictionary: dict):
    for k, v in dictionary.items():
        print(f"{k}: {v}")


stack = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
junk = {}
winner = ""

while winner == "":
    resources = input().split(" ")

    for ind in range(0, len(resources), 2):
        key = (resources[ind + 1]).lower()
        value = int(resources[ind])

        if key not in stack:
            if key not in junk:
                junk[key] = value
            else:
                junk[key] += value

        else:
            stack[key] += value

            if stack[key] >= 250:
                if key == "shards":
                    print("Shadowmourne obtained!")
                    winner = "Shadowmourne"

                elif key == "fragments":
                    print("Valanyr obtained!")
                    winner = "Valanyr"

                elif key == "motes":
                    print("Dragonwrath obtained!")
                    winner = "Dragonwrath"

                stack[key] -= 250
                break

sorted_stack = dict(sorted(stack.items(), key=lambda x: (-x[1], x[0])))
sorted_junk = dict(sorted(junk.items()))

print_dict(sorted_stack)
print_dict(sorted_junk)
