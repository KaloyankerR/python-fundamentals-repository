def fire(index: int, damage: int):
    ship = int(war_ship_status[index])
    ship -= damage

    if ship <= 0:
        return None
    else:
        war_ship_status[index] -= damage
        return war_ship_status


def defend(start_index: int, end_index: int, damage: int):
    ship = pirate_ship_status
    ship_damaged = list(map((lambda x: x - damage), ship[start_index:end_index]))
    ship = ship[:start_index] + ship_damaged + ship[end_index:]
    condition = list(filter((lambda x: x <= 0), ship_damaged))

    if len(condition) > 0:
        return None
    else:
        return ship


def repair(index: int, health: int):
    ship = pirate_ship_status[index]
    ship += health

    if ship > max_health_capacity:
        ship = max_health_capacity

    return ship


def status():
    health_percent = max_health_capacity * 0.2
    count = list(filter((lambda x: x < health_percent), pirate_ship_status))

    return len(count)


pirate_ship_status = input().split('>')
pirate_ship_status = list(map(int, pirate_ship_status))
pirate_ship_len = len(pirate_ship_status)

war_ship_status = input().split('>')
war_ship_status = list(map(int, war_ship_status))
war_ship_len = len(war_ship_status)

max_health_capacity = int(input())

stalemate = True
while True:
    tokens = input().split(' ')
    command = tokens[0]
    res = 0

    if command == 'Retire':
        break

    elif command == 'Fire':
        if 0 <= int(tokens[1]) < war_ship_len:
            res = fire(index=int(tokens[1]), damage=int(tokens[2]))

            if res is None:
                print('You won! The enemy ship has sunken.')
                stalemate = False
                break

    elif command == 'Defend':
        if 0 <= int(tokens[1]) < pirate_ship_len and \
                0 <= int(tokens[2]) < pirate_ship_len and int(tokens[1]) <= int(tokens[2]):
            res = defend(start_index=int(tokens[1]), end_index=int(tokens[2]) + 1, damage=int(tokens[3]))

            if res is None:
                print('You lost! The pirate ship has sunken.')
                stalemate = False
                break
            else:
                pirate_ship_status = res

    elif command == 'Repair':
        if 0 <= int(tokens[1]) < pirate_ship_len:
            res = repair(int(tokens[1]), int(tokens[2]))

            pirate_ship_status[int(tokens[1])] = res

    elif command == 'Status':
        res = status()
        print(f'{res} sections need repair.')

if stalemate:
    print(f'Pirate ship status: {sum(pirate_ship_status)}')
    print(f'Warship status: {sum(war_ship_status)}')
