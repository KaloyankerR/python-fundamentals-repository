numbers = input().split(', ')
beggars = int(input())

beggars_list = []
for i in range(beggars):
    beggars_list.append([])

counter = 0
for number in numbers:
    beggars_list[counter].append(int(number))

    counter += 1
    if counter == beggars:
        counter = 0

result = []
for _ in beggars_list:
    result.append(sum(_))

print(result)
