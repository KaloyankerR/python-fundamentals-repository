numbers = input().split(' ')

sorted_numbers = sorted(numbers)
reversed_numbers = list(reversed(sorted_numbers))

result = [print(x, end='') for x in reversed_numbers]
