def odd_even_sum(number):
    even_sum = 0
    odd_sum = 0
    for index in range(len(number)):
        if int(number[index]) % 2 == 0:
            even_sum += int(number[index])
        else:
            odd_sum += int(number[index])
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


odd_even_sum(number=input())
