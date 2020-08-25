import math

numbers = input().split(', ')
numbers = list(map(int, numbers))

max_number = math.ceil((max(numbers) / 10))

for index in range(1, max_number + 1):
    group = list(filter((lambda x: (index * 10) - 10 < x <= index * 10), numbers))
    print(f'Group of {index * 10}\'s: {group}')
