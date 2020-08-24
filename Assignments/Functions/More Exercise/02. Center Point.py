def closest_point(x1, y1, x2, y2):
    first_point = abs(x1) + abs(y1)
    second_point = abs(x2) + abs(y2)

    if first_point == second_point:
        return f'({int(num1)}, {int(num2)})'
    elif first_point > second_point:
        return f'({int(num3)}, {int(num4)})'
    elif first_point < second_point:
        return f'({int(num1)}, {int(num2)})'


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
print(closest_point(num1, num2, num3, num4))
