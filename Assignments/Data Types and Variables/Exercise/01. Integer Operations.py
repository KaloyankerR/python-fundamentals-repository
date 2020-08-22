total_sum = 0

for number in range(4):
    num = int(input())

    if number == 0 or number == 1:
        total_sum += num
    elif number == 2:
        total_sum //= num
    else:
        total_sum *= num

print(total_sum)
