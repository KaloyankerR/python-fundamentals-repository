guests = set()

for _ in range(int(input())):
    guests.add(input())

while True:
    cmd = input()

    if cmd == "END":
        break
    else:
        try:
            guests.remove(cmd)
        except KeyError:
            pass

sorted_guests = '\n'.join(sorted(guests))
print(len(guests))
print(f"{sorted_guests}")
