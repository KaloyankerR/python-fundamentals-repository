def smallest_number(num1, num2, num3):
    smallest = min(num1, num2, num3)
    return smallest


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(smallest_number(number_1, number_2, number_3))
