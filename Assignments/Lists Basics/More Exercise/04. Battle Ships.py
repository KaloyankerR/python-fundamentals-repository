ships = []
destroyed_ships = 0
n = int(input())
# rows = [ships.append([]) for i in range(n)]

for i in range(n):
    col = input().split(' ')
    ships.append(col)

attacked_squares = input().split(' ')

for j in attacked_squares:
    row = int(j[0])
    col = int(j[2])
    ships_health = int(ships[row][col])
    condition = (ships_health - 1 == 0)

    if ships_health != 0:
        ships_health -= 1
        if ships_health == 0:
            destroyed_ships += 1
            ships[row][col] = str(ships_health)
        else:
            ships[row][col] = str(ships_health)

print(destroyed_ships)
