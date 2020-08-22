num = float(input())

if num == 0:
    print('zero')
else:
    if abs(num) < 1:
        print('small', end=' ')
    elif abs(num) > 1_000_000:
        print('large', end=' ')
    if num > 0:
        print('positive')
    elif num < 0:
        print('negative')
