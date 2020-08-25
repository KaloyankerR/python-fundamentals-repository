numbers_str = input().split(', ')
numbers = list(map(lambda x: int(x), numbers_str))

even_numbers_indexes = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
print(even_numbers_indexes)
