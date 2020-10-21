names = set()

for _ in range(int(input())):
    name = input()
    if name not in names:
        print(name)
        names.add(name)
