n = int(input())

for i in range(1, n + 1):
    digit = i

    sum = 0
    while i:
        sum += i % 10
        i //= 10

    if sum == 5 or sum == 7 or sum == 11:
        print(f'{digit} -> True')
    else:
        print(f'{digit} -> False')
