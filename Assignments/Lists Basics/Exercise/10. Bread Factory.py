working_day_events = input().split('|')
energy = 100
coins = 100
is_open = True

for events in working_day_events:
    events = events.split('-')
    event_or_ingredient = events[0]
    number = int(events[1])

    if event_or_ingredient == 'rest':
        if (energy + number) >= 100:
            print(f'You gained {energy - 100} energy.')
            energy = 100
        else:
            print(f'You gained {number} energy.')
            energy += number

        print(f'Current energy: {energy}.')

    elif event_or_ingredient == 'order':
        if (energy - 30) >= 0:
            print(f'You earned {number} coins.')
            coins += number
            energy -= 30
        else:
            print(f'You had to rest!')
            energy += 50

    else:
        if (coins - number) > 0:
            print(f'You bought {event_or_ingredient}.')
            coins -= number
        else:
            print(f'Closed! Cannot afford {event_or_ingredient}.')
            is_open = False
            break

if is_open:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
