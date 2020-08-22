n = int(input())
capacity = 255

for quantities in range(n):
    poured_water = int(input())
    if poured_water > capacity:
        print("Insufficient capacity!")
    else:
        capacity -= poured_water

print(255 - capacity)
