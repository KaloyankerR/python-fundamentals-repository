queue = list(reversed(input().split(', ')))
wolf_found = False

if queue[0] == 'wolf':
    print('Please go away and stop eating my sheep')
    wolf_found = True

if not wolf_found:
    for animal in range(len(queue) - 1, -1, -1):
        if queue[animal] == 'wolf':
            print(f'Oi! Sheep number {animal}! You are about to be eaten by a wolf!')
