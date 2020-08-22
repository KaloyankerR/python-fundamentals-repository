size = int(input())
current = 1
step = 1

for row in range(size * 2):
    for col in range(0, current):
        print('*', end='')

    if current == size:
        step = -1
    current += step
    print()
