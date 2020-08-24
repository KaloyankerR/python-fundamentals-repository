def is_perfect(number):
    number_sum = 0
    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            number_sum += i
    return number_sum == number


num = int(input())
if is_perfect(num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
