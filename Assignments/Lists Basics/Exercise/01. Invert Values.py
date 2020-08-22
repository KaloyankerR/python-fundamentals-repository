numbers = input().split(' ')
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for j in range(len(numbers)):
    numbers[j] = int(numbers[j]) * -1

print(numbers)
