command = input()
coffees_count = 0

while command != 'END' and coffees_count <= 5:
    if command.islower():
        if command == 'coding':
            coffees_count += 1
        elif command == 'dog' or command == 'cat':
            coffees_count += 1
        elif command == 'movie':
            coffees_count += 1

    elif command.isupper():
        if command == 'CODING':
            coffees_count += 2
        elif command == 'DOG' or command == 'CAT':
            coffees_count += 2
        elif command == 'MOVIE':
            coffees_count += 2

    command = input()

if coffees_count > 5:
    print('You need extra sleep')
else:
    print(coffees_count)
