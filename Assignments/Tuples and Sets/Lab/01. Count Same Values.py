from collections import defaultdict

numbers_dict = defaultdict(int)
# numbers_dict = {}
numbers = map(float, input().split())

for num in numbers:
    numbers_dict[num] += 1
    # if num not in numbers_dict:
    #     numbers_dict[num] = 0
    # numbers_dict[num] += 1

[print(f"{x} - {y} times") for (x, y) in numbers_dict.items()]
