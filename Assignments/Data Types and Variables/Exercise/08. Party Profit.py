companions = int(input())
days = int(input())

coins = 0
for day in range(1, days + 1):
    if day % 15 == 0:
        companions += 5

    if day % 10 == 0:
        companions -= 2

    if day % 5 == 0:
        coins += (companions * 20)
        if day % 3 == 0:
            coins -= (companions * 2)

    if day % 3 == 0:
        coins -= (companions * 3)

    coins += 50 - (companions * 2)

companions_coins = int(coins // companions)
print(f"{companions} companions received {companions_coins} coins each.")
