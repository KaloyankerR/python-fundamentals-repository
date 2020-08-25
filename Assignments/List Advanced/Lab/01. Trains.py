wagons = int(input()) * [0]

while True:
    tokens = input().split(' ')
    command = tokens[0]

    if command == 'End':
        break
    elif command == 'add':
        people = int(tokens[1])
        wagons[-1] += people
    elif command == 'insert':
        index = int(tokens[1])
        people = int(tokens[2])
        wagons[index] += people
    elif command == 'leave':
        index = int(tokens[1])
        people = int(tokens[2])
        wagons[index] -= people

print(wagons)
