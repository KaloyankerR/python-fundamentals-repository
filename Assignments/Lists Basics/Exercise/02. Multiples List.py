factor = int(input())
count = int(input())

numbers = []
counter = 1
while count != len(numbers):
    numbers.append(counter * factor)
    counter += 1

print(numbers)
