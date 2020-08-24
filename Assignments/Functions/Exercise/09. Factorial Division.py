import math


def fact(num1, num2):
    num1 = math.factorial(num1)
    num2 = math.factorial(num2)
    result = num1 / num2
    return result


numbers_factorial = fact(num1=int(input()), num2=int(input()))
print(f'{numbers_factorial:.2f}')
