def closest_point_1(x1, y1, x2, y2):
    global total_1
    first_point = abs(x1) + abs(y1)
    second_point = abs(x2) + abs(y2)
    total_1 = first_point + second_point

    if first_point == second_point:
        return f'({int(num1)}, {int(num2)})({int(num3)}, {int(num4)})'
    elif first_point > second_point:
        return f'({int(num3)}, {int(num4)})({int(num1)}, {int(num2)})'
    elif first_point < second_point:
        return f'({int(num1)}, {int(num2)})({int(num3)}, {int(num4)})'


def closest_point_2(x1, y1, x2, y2):
    global total_2
    first_point = abs(x1) + abs(y1)
    second_point = abs(x2) + abs(y2)
    total_2 = first_point + second_point

    if first_point == second_point:
        return f'({int(num5)}, {int(num6)})({int(num7)}, {int(num8)})'
    elif first_point > second_point:
        return f'({int(num7)}, {int(num8)})({int(num5)}, {int(num6)})'
    elif first_point < second_point:
        return f'({int(num5)}, {int(num6)})({int(num7)}, {int(num8)})'


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

num5 = float(input())
num6 = float(input())
num7 = float(input())
num8 = float(input())

total_1 = 0
total_2 = 0

line_1 = closest_point_1(num1, num2, num3, num4)
line_2 = closest_point_2(num5, num6, num7, num8)

if total_1 == total_2:
    print(line_1)
elif total_1 < total_2:
    print(line_2)
else:
    print(line_1)
