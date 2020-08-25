atoms = int(input())
res = []

index = 1
while atoms > 0:
    rule = 2 * index ** 2

    if atoms <= rule:
        res.append(atoms)
    else:
        res.append(rule)

    index += 1
    atoms -= rule

print(res)
